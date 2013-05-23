import unittest

def geradorLista():
     
    return range(1,101)


def isFizz(valor):
    if valor % 3 == 0:
        return  True
    else:
        return False

def isBuzz(valor):
    if valor % 5 == 0:
        return  True
    else:
        return False

def isFizzBuzz(valor):
    if valor % 5 == 0 and valor % 3  == 0 :
        return  True
    else:
        return False
def printLista(lista):
    for i in lista:
        if(isFizzBuzz(i)):
            print('FizzBuzz')
        elif(isFizz(i)):
            print('Fizz')
        elif(isBuzz(i)):
            print('Buzz')
        else:
            print(i)

printLista(geradorLista())

class FizzTest(unittest.TestCase):
    
    def testTamanho(self):
        lista  = geradorLista()
        lenght = len(lista)
        self.assertEqual(lenght,100)

    def testFizz(self):        
        self.assertEqual(True, isFizz(3))
    
    def testBuzz(self):
        self.assertEqual(True, isBuzz(5))

    def testFizzBuzz(self):
        self.assertEqual(True, isFizzBuzz(15))

        
"""
    def testFizz(self):
        for x in range(1,101):
            fizz = (x % 3) == 0
            if(fizz):
                self.assertEqual(fizz, True)

    def testBuzz(self):
        for x in range(1,101):
            buzz = (x % 5) == 0
            if(buzz):
                self.assertEqual(buzz, True)

    def testFizzBuzz(self):
        for x in
"""
if __name__=="__main__":
    unittest.main()