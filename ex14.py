from sys import argv

script = input("ENTER SCRIPT NAME: ")
user_name = input("enter user name: ")
prompt = '> '
#san = '@ '

print(f"Hi {user_name}, I'm the {script} script.")

print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?")
likes = input(prompt)
# likes = input("san")

print(f"Where do you live {user_name}?")
lives = input(prompt)
# lives = input(san)

print("What kind of computer do you have?")
computer = input(prompt)
#computer = input()


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")