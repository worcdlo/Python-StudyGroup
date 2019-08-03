from enum import Enum

class MyEnumData(Enum):
    a = '1'
    b = '2'
    c = '3'

    @classmethod
    def has_member(cls, member_name):
        return any(member_name == key.value for key in cls)

    @classmethod
    def traversal_member(cls):
        for key in cls:
            print(key.value)
            
"""
In [57]: MyEnumData.has_member('1')
Out[57]: True

In [58]: MyEnumData.has_member('4')
Out[58]: False

In [59]: MyEnumData.traversal_member()
1
2
3
"""
