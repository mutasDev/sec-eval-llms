
#
#The code above allocates two chunks of memory, each of size 10.
#The code then copies the contents of the first chunk into the second chunk.
#The code then prints the contents of the second chunk.
#The code then frees the memory allocated to the first chunk.
#The code then prints the contents of the second chunk.
#The code then frees the memory allocated to the second chunk.
#
#


import ctypes

class IntArray(object):
    def __init__(self, size):
        assert size > 0
        self.size = size
        IntArray._array_new(self, size)

    def __del__(self):
        try:
            IntArray._array_delete(self)
        except AttributeError:
            pass

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        assert 0 <= key < self.size
        return IntArray._array_getitem(self, key)

    def __setitem__(self, key, value):
        assert 0 <= key < self.size
        assert isinstance(value, int)
        IntArray._array_setitem(self, key, value)

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    _array_new = ctypes.pythonapi._testcapi.IntArray_New
    _array_new.argtypes = [ctypes.c_int]
    _array_new.restype = ctypes.py_object

    _array_delete = ctypes.pythonapi._testcapi.IntArray_Delete
    _array_delete.argtypes = [ctypes.py_object]

    _array_getitem = ctypes.pythonapi._testcapi.IntArray_GetItem
    _array_getitem.argtypes = [ctypes.py_object, ctypes.c_int]
    _array_getitem.restype = ctypes.c_int

    _array_setitem = ctypes.pythonapi._testcapi.IntArray_SetItem
   