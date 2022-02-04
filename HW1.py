import unittest

def classifyTriangle(a,b,c):
    if a + b > c and b + c > a and a + c > b and min(a,b,c) > 0:
        if a == b == c :
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isoceles Triangle"
        else:
            if max(a,b,c) ** 2 == ((a + b + c) - max(a,b,c) - min(a,b,c)) ** 2 + min(a,b,c) ** 2:
                return 'Right Triangle'
            else:
                return "Scalene Triangle"  
    else:
        return 'Not A Triangle'

def printClassifyTriangle(a,b,c):
    print('classifyTriangle(',a, ',', b, ',', c, ')= ' + classifyTriangle(a,b,c))

class TestTriangles(unittest.TestCase):
    def test_NotATriangle(self):
        """ test not a triangle detection """
        self.assertEqual(classifyTriangle(3,3,7), 'Not A Triangle')
        self.assertEqual(classifyTriangle(3,0,7), 'Not A Triangle')
        self.assertNotEqual(classifyTriangle(3,3,3), "Not A Triangle")


    def test_Equilateral(self):
        """ test equilateral triangle detection """  
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral Triangle')
        self.assertNotEqual(classifyTriangle(3,4,3), 'Equilateral Triangle')  

    def test_Isoceles(self):
        """ test isoceles triangle detection """
        self.assertEqual(classifyTriangle(3,5,5), 'Isoceles Triangle')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Isoceles Triangle')

    def test_Scalene(self):
        """ test scalene triangle detection """
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene Triangle')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Scalene Triangle')
        
    def test_Right(self):
        """ test rest triangle detection """
        self.assertEqual(classifyTriangle(3,4,5), 'Right Triangle')
        self.assertNotEqual(classifyTriangle(6,10,6), 'Right Triangle')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

    printClassifyTriangle(6,10,6)
    printClassifyTriangle(1,3,0)
    printClassifyTriangle(2,6,6)
    printClassifyTriangle(6,4,5)
    printClassifyTriangle(2,2,2)
    printClassifyTriangle(1,3,5)
    printClassifyTriangle(1,12,5)
    printClassifyTriangle(3,4,5)

    unittest.main(exit=True)