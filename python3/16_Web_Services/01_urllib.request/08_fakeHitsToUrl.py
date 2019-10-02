import time
import webbrowser

# how much views you want

totalBreaks = 30
countBreaks = 0

print("Enjoy your Time\n" + time.ctime())
while (countBreaks < totalBreaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=ZeN4a0GNNRc")
    time.sleep(5)

    countBreaks += 1
