mystuff = {'apple' = "I AM APPLES!"}
print(mystuff['apple'])

# Imagine I have a module named mystuff and I put a function in it called apple.
# Here's my module mystuff.py
# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

# Once I have this code, I can use module MyStuff with import and then access the apple function
import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# I could also put a variable in it named tangerine
# this is just a variable
tangerine = "Living reflection of a dream"

# I can access that the same way
import mystuff()

mystuff.apple()
print(mystuff.tangerine)

# If I were to create a class just like the mystuff module, I'd do something like this:
class MyStuff(object):

    def _init_(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
