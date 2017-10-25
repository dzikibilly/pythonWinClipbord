import win32clipboard


win32clipboard.OpenClipboard()

data = win32clipboard.GetClipboardData()

print("%r" %data)
