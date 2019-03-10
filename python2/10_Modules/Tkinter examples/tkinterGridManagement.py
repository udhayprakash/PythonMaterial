#-Guilherme H. Polo Goncalves

from Tkinter import Tk, Button, Checkbutton, Label, Entry, Frame

class App:
    def __init__(self, master):
        column0_padx = 24
        row_pady = 36

        #Label 1
        lbl_testcase_exec = Label(master, text="Test case execution",
                                  wraplength=100, anchor='w', justify='left')
        lbl_results_cmp = Label(master, text="Results comparison",
                                wraplength=100, justify='left')
        lbl_tolerance = Label(master, text="Tolerance (5%)", wraplength=100)
        testcase_exec = Checkbutton(master)
        results_cmp = Checkbutton(master)
        tolerance = Entry(master, width=4)
        lbl_analysis = Label(master, text="Analysis Library")
        analysis_lib = Entry(master, width=30)

        lbl_testcase_exec.grid(row=0, column=2, padx=20, pady=12, sticky='w')
        lbl_results_cmp.grid(row=0, column=3, pady=12, sticky='w')
        lbl_tolerance.grid(row=0, column=4, padx=20, pady=12, sticky='wn')
        lbl_analysis.grid(row=1, column=0, sticky='w', padx=column0_padx)
        analysis_lib.grid(row=1, column=1, sticky='w')
        testcase_exec.grid(row=1, column=2, padx=20, sticky='w')
        results_cmp.grid(row=1, column=3, sticky='w')
        tolerance.grid(row=1, column=4, padx=20, sticky='w')

        #Label 2
        lbl_ref_analysis = Label(
            master, text="Reference Analysis Libary Version",
            wraplength=150, justify='left', pady=row_pady)
        ref_analysis_lib = Entry(master, width=30)
        lbl_ref_analysis.grid(row=2, column=0, sticky='w', padx=column0_padx)
        ref_analysis_lib.grid(row=2, column=1, sticky='w')

        # version
        lbl_version = Label(master, text="Version under Test")
        version = Label(master, text="vA.B.C.D")
        lbl_version.grid(row=3, column=0, sticky='w', padx=column0_padx)
        version.grid(row=3, column=1, sticky='w')

        # test all
        lbl_testall = Label(master, text="Test All")
        testall = Checkbutton(master)
        lbl_testall.grid(row=4, column=0, pady=row_pady, padx=column0_padx,
                         sticky='w')
        testall.grid(row=4, column=1, sticky='w')

        # buttons
        bottom_frame = Frame(master)
        bottom_frame.grid(row=5, column=1, columnspan=3, sticky='w')

        btn_start = Button(bottom_frame, text = "Go", width=7)
        btn_start.pack(side='left')
        btn_commit = Button(bottom_frame, text="Commit", width=7)
        btn_commit.pack(side='left', padx=80)
        btn_exit = Button(bottom_frame, text="Exit", width=7)
        btn_exit.pack(side='left')

root = Tk()
root.title("Test Automation")
root.minsize(800, 400)
app = App(root)
root.mainloop()