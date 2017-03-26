import win32gui
import win32ui
import win32con
import win32api

#grap a handle of the main desktop window
hdesktop = win32gui.GetDesktopWindow()

#determine the size of all monitors in pixels
width = win32api.GetSystemMeterics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMeterics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMeterics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMeterics(win32con.SM_YVIRTUALSCREEN)

#create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32gui.CreateDFormHandle(desktop_dc)

#create a memory based device context
mem_dc = img_dc.CreateCompatibleDC()

#create a bitmap object
screenshot = win32gui.CreateBitmap()
screenshot.CreateCompatibleBitmap()
mem_dc.SelectObject(screenshot)

#copy the screen into our memory device context
mem_dc.BitBlt((0,0), (width, height), img_dc, (left,top), win32con.SRCOPY)

#save the bitmap to a file
screenshot.SaveBitmapFile(mem_dc, 'c:\\Windows\\Temp\\screenshot.bmp')

#free our objects
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
