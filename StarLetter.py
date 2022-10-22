'''
This line is just for the design of this program
''' 
print("\033[1;37;40m╔════ \033[1;35;40m ❀•°❀°•❀\033[1;37;40m ══════ \033[1;35;40m❀•°❀°•❀\033[1;37;40m ══════╗\n")
print ("              \033[1;33;40m     Good Day!  ")
print ("      \033[2;36;40m      This is Jezell's nickname \n")
print ("\033[1;37;40m╚════\033[1;35;40m ❀•°❀°•❀\033[1;37;40m ═══════\033[1;35;40m ❀•°❀°•❀\033[1;37;40m ═════╝\n")

name=("ZEL")
name_z= (" " for i in range(6) for j in range (6))
name_e= (" " for i in range(6) for j in range (7))
name_l= (" " for i in range(5) for j in range (7))

#Letter Z
def first(): 
    for row in range(6):
        for col in range(6):
            if (row==0 or row==5) or col+row==5:
                print('*',end='')
            else:
                print(end=' ')
        print()

    
#Letter E
def second():
    for row in range(7):
        for col in range(6):
            if col==0 or row%3==0:
                print("*", end='')
            else:
                print(end=" ")
        print()
  
#Letter L  

def third():
    for row in range(7):
        for col in range(5):
            if col==0 or (row==6 and col>0):
                print("*", end='')
            else:
                print(end=" ")
        print()

first()
second()
third()

print(" \n\033[1;32;40m October 22, 2022 - Saturday \n\033[1;37;40m There are 65 more days to go until Christmas Day 2022. \n Thank You for viewing.") 