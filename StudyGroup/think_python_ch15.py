# Think Python 15 
"""
Created on Sat Apr 20 00:42:57 2019

@author: Aaron
"""
import copy

def print_point(point, p_name = "p"):
    print("%s, %s = (%f, %f)" %(point, p_name, point.x, point.y))


## 15.1 自定義類別
## 15.2 属性
"""
如何建class
實體化class 也就是配置記憶體
"""
class TestPoint():
    """represents a point in 2-D space"""
    x = 1
    y = 2
    
def test1():
    p1 = TestPoint()
    p2 = TestPoint()
    print("%s, p1 = (%f, %f)" %(p1, p1.x, p1.y))
    print("%s, p2 = (%f, %f)" %(p2, p2.x, p2.y))
    print("Reset p1")
    p1.x = 3
    p1.y = 4
    print("%s, p1 = (%f, %f)" %(p1, p1.x, p1.y))
    print("%s, p2 = (%f, %f)" %(p2, p2.x, p2.y))
    
## 15.3 Rectangle
    
class TestRectangle():
    """represents a rectangel in 2-D space"""
    height = 10
    width = 5
    corner = TestPoint()

def test2():
    rect1 = TestRectangle()
    print("%s , h = %f, w = %f, cornor = (%f, %f)" 
          %(rect1, rect1.height, rect1.width, rect1.corner.x, rect1.corner.y))

## class 可以是回傳值 也可以是引數

def find_center(box):
    """
    Args:
        box: TestRectangle
        
    Returns:
        TestPoint
    """
    p = TestPoint()
    p.x = box.corner.x + box.width / 2.0
    p.y = box.corner.y + box.height / 2.0
    return p


def test3():
    rect1 = TestRectangle()
    print("%s , h = %f, w = %f, cornor = (%f, %f)" 
          %(rect1, rect1.height, rect1.width, rect1.corner.x, rect1.corner.y))
    
    p1 = find_center(rect1)
    print("%s, p1 = (%f, %f)" %(p1, p1.x, p1.y))

    
## 複製class

"""
p2 = p1
"""
def test4():
    p1 = TestPoint()
    p2 = p1
    print_point(p1, "p1")
    print_point(p2, "p2")
    
    p2.x = 0
    p2.y = 0
    print_point(p1, "p1")
    print_point(p2, "p2")
    
"""
p2 = copy.copy(p1)
"""  
def test5():
    p1 = TestPoint()
    p2 = copy.copy(p1)
    print_point(p1, "p1")
    print_point(p2, "p2")
    
    p2.x = 0
    p2.y = 0
    print_point(p1, "p1")
    print_point(p2, "p2")


## 屬性測試
    
def test6():
    p1 = TestPoint()
    print(p1.z)

"""用來測試是否在class內
hasattr(p1, 'z')
"""
def test7():
    p1 = TestPoint()
    print("if z in p1:", hasattr(p1, 'z'))
    if(hasattr(p1, 'z')):
        print("p1.z = ", p1.z)
        
    print("if x in p1:", hasattr(p1, 'x'))
    if(hasattr(p1, 'x')):
        print("p1.x = ", p1.x)



## 注意

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
class Circle():
    def __init__(self, p = Point(), radius = 0):
        self.center = p
        self.radius = radius

def print_circle(circle, circle_name = "circle"):
    print("%s: radius = %f, center = (%f, %f)" 
          %(circle_name, circle.radius, circle.center.x, circle.center.y))

def test8():
    p = Point(10, 10)
    circle1 = Circle(p, 99)    
    print_circle(circle1, "circle1")
    
    p.x = 5
    print_circle(circle1, "circle1")
    

def test9():
    p = Point(10, 10)
    circle1 = Circle(copy.copy(p), 99)    
    print_circle(circle1, "circle1")
    
    p.x = 5
    print_circle(circle1, "circle1")
    
def test10():
    p = Point(10, 10)
    circle1 = Circle(Point(10, 10), 99)    
    print_circle(circle1, "circle1")
    
    p.x = 5
    print_circle(circle1, "circle1")    
