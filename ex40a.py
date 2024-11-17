#dict style
mystuff['apples']
 
# #module style 
import mystuff
mystuff.apple() #get apple from module
print(mystuff.tangerine) # mystuff.tangerine - same thing, its just a variable

#class
class MyStuff(object):

    def __init__(self): #with self it is directly referring its attribute. 
        #without self it doesnt know that you are referring variable or attribute
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

#class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)