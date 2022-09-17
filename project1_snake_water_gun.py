import random
def game(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you=='w':
            return False
        elif you=='s':
            return True                    

print("comp turn: snake(s) water(w) gun(g)???")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
            
b= input("player's turn: snake(s) water(w) gun(g)???")
a=game(comp,b)
print(f"computer choose:{comp}")
print(f"player choose:{b}")
if a==None:
    print("tie")
elif a:
    print("you loose") 
else:
    print("you win")                  