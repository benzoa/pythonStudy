import win32api 
from win32api import GetSystemMetrics, GetLocalTime, GetSystemTime, GetComputerName, GetUserName
import win32con
import win32gui
from pathlib import Path
import win32file
import win32clipboard

# ref : https://github.com/mhammond/pywin32, http://codetorial.net/pywin32/index.html

# Beep
win32api.Beep(500, 3000)	# frequency(37Hz ~ 32,767kHz), duration

# Get cursor positon
pos = win32api.GetCursorPos()
print(pos)

# move cursor to specific position
pos = (200, 200)
win32api.SetCursorPos(pos)


def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
	
	# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


mouse_click(300, 300)

# restrict the position of the cursor
win32api.ClipCursor((200, 200, 700, 700))

# release restriction
win32api.ClipCursor((0, 0, 0, 0))
# win32api.ClipCursor()

# get screen resolution
print('Width:', GetSystemMetrics(0))
print('Height:', GetSystemMetrics(1))

# get pixcel color as hex
color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)
print(hex(color))

# get pixcel color as rgb
def rgbint2rgbtuple(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255

    return (red, green, blue)

print(rgbint2rgbtuple(color))


# get local time
# https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime
# year, month, dayOfWeek, day, hour, minute, second, milliseconds 
print(GetLocalTime())

# get system time
# https://docs.microsoft.com/ko-kr/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtime
print(GetSystemTime())

# computer name
print(GetComputerName())

# user name
print(GetUserName())

# create empty file
Path('test.txt').touch()

# create dirctory
Path('new_folder').mkdir()

# copy file
win32api.CopyFile('test.txt', 'test_copied.txt')

# change file name
win32api.MoveFile('test_copied.txt', 'test_new.txt')

# move file
win32api.MoveFile('test_new.txt', './new_folder/test_new.txt')

# delete file
win32api.DeleteFile('test.txt')

# create directory
win32file.CreateDirectory('new_folder2', None)

# delete directory
win32file.RemoveDirectory('new_folder2')

# create directory and then move it
win32file.CreateDirectory('upper_folder', None)
win32file.SetCurrentDirectory('upper_folder')

win32file.CreateDirectory('new_folder', None)

# open clipboard
win32clipboard.OpenClipboard()
# empty clipboard
win32clipboard.EmptyClipboard()
# set text in the clipboard
win32clipboard.SetClipboardText('Text to Clipboard')
# close clipboard
win32clipboard.CloseClipboard()


# get data in the clipboard
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(data)
