#!/usr/bin/env python3

# class Dog:
#     def __init__(self, name):
#         print(f"{name} is born!")
        
#         def bark(self):
#             print("Woof!")
            
#         def showing_self(self):
#             return self

# fido = Dog("Fido")
# fido is fido.showing_self()

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed =  breed
        print (f"A {breed} named {name} is born!.")
        
fido = Dog("Fido") 
fido.breed      
        

pass















# __init__
# Every time we initialize a new object,
# the Python interpreter calls a magic 
# method called __init__. Magic methods 
# (also called dunder methods due to 
#  their double underscores) are special 
# methods that are not meant to be called 
# by developers but are invoked by different 
# cues and operators that act on their objects.