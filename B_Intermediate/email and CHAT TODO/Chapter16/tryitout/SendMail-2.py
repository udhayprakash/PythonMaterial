from SendMail import SmartMessage, MailServer
msg = SmartMessage("Me <me@example.com",
                   "You <you@example.com>",
                   "Your picture",
                   "Here's that picture I took of you.")
msg.addAttachment(open("photo.jpg").read(), "photo.jpg")
MailServer("localhost").sendMessage(msg)
