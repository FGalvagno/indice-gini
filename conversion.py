#conversion.py

from msl.loadlib import Server32
import ctypes
class MyServer(Server32):
    """Wrapper around a 32-bit C++ library 'my_lib.dll' that has an 'add' and 'version' function."""
    def __init__(self, host, port, **kwargs):
        # Load the 'my_lib' shared-library file using ctypes.CDLL
        super(MyServer, self).__init__('./bin/libconversion.so', 'cdll', host, port)

    def convert_and_increment(self, n):
        self.lib.convert_and_increment.argtypes = [ctypes.c_float]
        self.lib.convert_and_increment.restype = ctypes.c_int
        return self.lib.convert_and_increment(n)