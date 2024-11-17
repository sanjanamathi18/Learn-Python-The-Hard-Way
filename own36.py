from sys import exit

def the_mummy():
    print("Enter your box choice.")
    box = int(input('>'))
    
    if box == 1:
       print("Your reward is skeleton.")
    elif box == 2:
       print("Your reward is gold.")
    elif box == 3:
       dead("Biten by insect. RIP")
    else:
       print(f"the value should be 1,2,3. but you entered wrong value {box}")
       the_mummy()

   
def the_annabella():
    print('''What do you want to do?
    Choose one from the three options:
    1.Say hi
    2.Attack  
    3.Runaway\n''')
    option = input('>').casefold()

    if option == "say hi":
       print("You and Annabella are friends now.")
       dead("Good job.")
    elif option == "attack":
        dead("Not a good idea.")
    elif option == "runaway":
        print("You escaped.")
    else:
        print("You're a ghost now.")
        start()

         
def dead(why):
   print(why)
   exit(0)
   
def start():
   print("You've two rooms.") 
   print("Which room you want to choose?")
   print("Choose left or right")
   choice = input('>')

   if choice == "right":
        print("Welcome to The Mummy room.")
        the_mummy()
   elif choice == "left":
        print("Welcome to Annabella room.")
        the_annabella()
   else:
        dead("Go and do homework.")

start()


