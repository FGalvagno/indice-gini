from msl.loadlib import Client64

class conversion(Client64):
    """Call a function in 'my_lib.dll' via the 'MyServer' wrapper."""

    def __init__(self):
        # Specify the name of the Python module to execute on the 32-bit server (i.e., 'my_server')
        super(conversion, self).__init__(module32='conversion.py')
    
    def convert_and_increment(self,n):
        # The Client64 class has a 'request32' method to send a request to the 32-bit server
        return self.request32('convert_and_increment', n)


lib=conversion()

#print(lib.convert_and_increment(44.7))

