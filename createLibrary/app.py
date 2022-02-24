from F1.fOne import addFunction
from fTwo import subFunction
from fThree import mulFunction
from fFour import divFunction

lalalam = True
while lalalam:
    oprt = int(input("pick an operation 1.(+) 2.(-) 3.(*) 4.(/): "))
    if(oprt < 4 or oprt > 0):
        if(oprt == 1):
            print(addFunction(15,3))
        if(oprt == 2):
            print(subFunction(15,3))
        if(oprt == 3):
            print(mulFunction(15,3))
        if(oprt == 4):
            print(divFunction(15,3))
        lalalam = False


