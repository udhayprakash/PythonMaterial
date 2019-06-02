# Program that will stop common Windows applications and shut the computer down
# For the truly lazy. :-)

print ("Stopping applications now")
# import the operating system module
# allows user to run operating system commands from Python
import os
# Run the command "taskkill" to stop applications in Windows
os.system("taskkill /f /im notepad.exe")
os.system("taskkill /f /im winword.exe")
os.system("taskkill /f /im excel.exe")
os.system("taskkill /f /im powerpnt.exe")
os.system("taskkill /f /im outlook.exe")
os.system("taskkill /f /im chrome.exe")
os.system("taskkill /f /im calc.exe")
os.system("taskkill /f /im iexplore.exe")
os.system("taskkill /f /im powershell.exe")
os.system("taskkill /f /im wordpad.exe")

# use the template below to add more applications
# os.system("taskkill /f /im [executable name].exe")
# shutdown the computer in 1 second
os.system("shutdown /s /t 1")
