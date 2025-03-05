data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])  
print(view)