# first cal
print (" calculator PROGRAM  \n")
print ( " Help " )
print ("for ADD write + ")
print ("for SUBTRACT write - ")
print ("for MULTIPLY write * ")
print ("for DIVIDE write / ")
print ("for QUIT write q ")
while True :
    op = str(input ("\nPlease input OPRATION : "))
    if op == "q" :
        print ("\n *******BYE********")
        break
    elif op == "+":
        a = int (input("print first NUMBER : "))
        b = int (input("print second NUMBER : "))        
        resoult = a + b
        print ("Your answer is " + str(resoult))
    elif op == "-" :
        a = int (input("print first NUMBER : "))
        b = int (input("print second NUMBER : "))        
        resoult = a - b
        print ("Your answer is " + str(resoult))
    elif op == "*" :
        a = int (input("print first NUMBER : "))
        b = int (input("print second NUMBER : "))        
        resoult = a * b
        print ("Your answer is " + str(resoult))
    elif op == "/" :
        a = int (input("print first NUMBER : "))
        b = int (input("print second NUMBER : "))        
        resoult = a / b
        print ("Your answer is " + str(resoult))
    else :
        print ("it is't correct, please try again")

