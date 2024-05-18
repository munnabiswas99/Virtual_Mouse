from Eye1 import *
from Hand1 import *

x = int(input('Enter 1 for eye control\n2 for hand control\n'))
obj1 = Eye()
obj2 = Hand()
if x == 1:
    obj1.run()
if x == 2:
    obj2.run()