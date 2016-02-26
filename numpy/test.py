import numpy as np

persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})

a = np.array([("Zhang", 32, 75.5), ('Wang', 24, 65.2)], dtype=persontype)

c = a[1]

c['name'] = 'Li'

a.tofile("test.bin")
