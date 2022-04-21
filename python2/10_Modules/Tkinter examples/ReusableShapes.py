"""A wrapper to show line numbers for Tkinter Text widgets.

Features:

 - Line numbers are displayed in a seperate Text widget.

 - Line number display is entirely automatic.

 - Text in the main Text widget can be manipulated normally,
   without regard to line numbers.

 - Line numbers are displayed correctly for wrapped lines.

Drawbacks:

 - The height of each line in the main Text widget must all
   be the same.

 - The height of the lines in the line number display Text
   widget must be the same as for the main Text widget.

 - There is a slight delay in line numbers catching up with reality.
   This is most noticable when fast scrolling is taking place.

"""

__version__ = 0.2
__date__    = '2009-07-25'
__author__  = 'robert@pytrash.co.uk'
__licence__ = 'Public Domain'


__changelog__ = (

('2009-07-25', '0.2', 'PyTrash',

"""Fixed bugs, improved efficiency, added PanedWindow to demo."""),

('2009-07-24', '0.1', 'PyTrash',

"""Initial version."""),

)


from Tkinter import *

root = Tk()

class EditorClass(object):

    UPDATE_PERIOD = 100 #ms

    editors = []
    updateId = None

    def __init__(self, master):

        self.__class__.editors.append(self)

        self.lineNumbers = ''

        # A frame to hold the three components of the widget.
        self.frame = Frame(master, bd=2, relief=SUNKEN)

        # The widgets vertical scrollbar
        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vScrollbar.pack(fill='y', side=RIGHT)

        # The Text widget holding the line numbers.
        self.lnText = Text(self.frame,
                width = 4,
                padx = 4,
                highlightthickness = 0,
                takefocus = 0,
                bd = 0,
                background = 'lightgrey',
                foreground = 'magenta',
                state='disabled'
        )
        self.lnText.pack(side=LEFT, fill='y')

        # The Main Text Widget
        self.text = Text(self.frame,
                width=16,
                bd=0,
                padx = 4,
                undo=True,
                background = 'white'
        )
        self.text.pack(side=LEFT, fill=BOTH, expand=1)

        self.text.config(yscrollcommand=self.vScrollbar.set)
        self.vScrollbar.config(command=self.text.yview)

        if self.__class__.updateId is None:
            self.updateAllLineNumbers()

    def getLineNumbers(self):

        x = 0
        line = '0'
        col= ''
        ln = ''

        # assume each line is at least 6 pixels high
        step = 6

        nl = '\n'
        lineMask = '    %s\n'
        indexMask = '@0,%d'

        for i in range(0, self.text.winfo_height(), step):

            ll, cc = self.text.index( indexMask % i).split('.')

            if line == ll:
                if col != cc:
                    col = cc
                    ln += nl
            else:
                line, col = ll, cc
                ln += (lineMask % line)[-5:]

        return ln

    def updateLineNumbers(self):

        tt = self.lnText
        ln = self.getLineNumbers()
        if self.lineNumbers != ln:
            self.lineNumbers = ln
            tt.config(state='normal')
            tt.delete('1.0', END)
            tt.insert('1.0', self.lineNumbers)
            tt.config(state='disabled')

    @classmethod
    def updateAllLineNumbers(cls):

        if len(cls.editors) < 1:
            cls.updateId = None
            return

        for ed in cls.editors:
            ed.updateLineNumbers()

        cls.updateId = ed.text.after(
            cls.UPDATE_PERIOD,
            cls.updateAllLineNumbers)


def demo(noOfEditors, noOfLines):

    pane = PanedWindow(root, orient=HORIZONTAL, opaqueresize=True)

    for e in range(noOfEditors):
        ed = EditorClass(root)
        pane.add(ed.frame)

    s = 'line ................................... %s'
    s = '\n'.join( s%i for i in xrange(1, noOfLines+1) )

    for ed in EditorClass.editors:
        ed.text.insert(END, s)

    pane.pack(fill='both', expand=1)

    root.title('Example - Line Numbers For Text Widgets')


if __name__ == '__main__':

    demo(3, 9999)
    mainloop()
