#!/usr/bin/python
import SocketServer
import re
import socket

class ClientError(Exception):
    "An exception thrown because the client gave bad input to the server."
    pass

class PythonChatServer(SocketServer.ThreadingTCPServer):
    "The server class."

    def __init__(self, server_address, RequestHandlerClass):
        """Set up an initially empty mapping between a user's nickname
        and the file-like object used to send data to that user."""
        SocketServer.ThreadingTCPServer.__init__(self, server_address,
                                                 RequestHandlerClass)
        self.users = {}

class RequestHandler(SocketServer.StreamRequestHandler):
    """Handles the life cycle of a user's connection to the chat
    server: connecting, chatting, running server commands, and
    disconnecting."""

    NICKNAME = re.compile('^[A-Za-z0-9_-]+$') #Regex for a valid nickname

    def handle(self):
        """Handles a connection: gets the user's nickname, then
        processes input from the user until they quit or drop the
        connection."""
        self.nickname = None

        self.privateMessage('Who are you?')
        nickname = self._readline()
        done = False
        try:
            self.nickCommand(nickname)
            self.privateMessage('Hello %s, welcome to the Python Chat Server.'\
                                % nickname)
            self.broadcast('%s has joined the chat.' % nickname, False)
        except ClientError, error:
            self.privateMessage(error.args[0])        
            done = True
        except socket.error:
            done = True

        #Now they're logged in; let them chat.
        while not done:
            try:
                done = self.processInput()
            except ClientError, error:
                self.privateMessage(str(error))
            except socket.error, e:
                done = True

    def finish(self):                        
        "Automatically called when handle() is done."
        if self.nickname:
            #The user successfully connected before disconnecting. 
            #Broadcast that they're quitting to everyone else.
            message = '%s has quit.' % self.nickname
            if hasattr(self, 'partingWords'):
                message = '%s has quit: %s' % (self.nickname,
                                               self.partingWords)
            self.broadcast(message, False)

            #Remove the user from the list so we don't keep trying to
            #send them messages.
            if self.server.users.get(self.nickname):
                del(self.server.users[self.nickname])
        self.request.shutdown(2)
        self.request.close()

    def processInput(self):
        """Reads a line from the socket input and either runs it as a
        command, or broadcasts it as chat text."""
        done = False
        l = self._readline()
        command, arg = self._parseCommand(l)
        if command:
            done = command(arg)
        else:            
            l = '<%s> %s\n' % (self.nickname, l)
            self.broadcast(l)
        return done

    #Below are implementations of the server commands.

    def nickCommand(self, nickname):
        "Attempts to change a user's nickname."
        if not nickname:
            raise ClientError, 'No nickname provided.'
        if not self.NICKNAME.match(nickname):
            raise ClientError, 'Invalid nickname: %s' % nickname
        if nickname == self.nickname:
            raise ClientError, 'You are already known as %s.' % nickname
        if self.server.users.get(nickname, None):
            raise ClientError, 'There\'s already a user named "%s" here.' % nickname
        oldNickname = None
        if self.nickname:
            oldNickname = self.nickname
            del(self.server.users[self.nickname])
        self.server.users[nickname] = self.wfile
        self.nickname = nickname
        if oldNickname:
            self.broadcast('%s is now known as %s' % (oldNickname, self.nickname))

    def quitCommand(self, partingWords):
        """Tells the other users that this user has quit, then makes
        sure the handler will close this connection."""
        if partingWords:
            self.partingWords = partingWords
        #Returning True makes sure the user will be disconnected.
        return True

    def namesCommand(self, ignored):
        "Returns a list of the users in this chat room."
        self.privateMessage(', '.join(self.server.users.keys()))

    def msgCommand(self, nicknameAndMsg):
        "Send a private message to another user."
        if not ' ' in nicknameAndMsg:
            raise ClientError('No message specified.')
        nickname, msg = nicknameAndMsg.split(' ', 1)
        if nickname == self.nickname:
            raise ClientError('What, send a private message to yourself?')
        user = self.server.users.get(nickname)
        if not user:
            raise ClientError('No such user: %s' % nickname)
        msg = '[Private from %s] %s' % (self.nickname, msg)
        user.write(self._ensureNewline(msg))

    # Below are helper methods.
    
    def broadcast(self, message, includeThisUser=True):
        """Send a message to every connected user, possibly exempting the
        user who's the cause of the message."""
        message = self._ensureNewline(message)
        for user, output in self.server.users.items():
            if includeThisUser or user != self.nickname:
                output.write(message)

    def privateMessage(self, message):
        "Send a private message to this user."
        self.wfile.write(self._ensureNewline(message))

    def _readline(self):
        "Reads a line, removing any whitespace."
        return self.rfile.readline().strip()

    def _ensureNewline(self, s):
        "Makes sure a string ends in a newline."
        if s and s[-1] != '\n':
            s += '\r\n'
        return s

    def _parseCommand(self, input):
        """Try to parse a string as a command to the server. If it's an
        implemented command, run the corresponding method."""
        commandMethod, arg = None, None
        if input and input[0] == '/':
            if len(input) < 2:
                raise ClientError, 'Invalid command: "%s"' % input
            commandAndArg = input[1:].split(' ', 1)
            if len(commandAndArg) == 2:
                command, arg = commandAndArg
            else:
                command, = commandAndArg
            commandMethod = getattr(self, command + 'Command', None)
            if not commandMethod:
                raise ClientError, 'No such command: "%s"' % command
        return commandMethod, arg

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Usage: %s [hostname] [port number]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    PythonChatServer((hostname, port), RequestHandler).serve_forever()
