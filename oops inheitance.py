class Animal: # inheitance allow one class to inheit the property of other
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("dog barks")

#creating object
dog = Dog()
dog.speak()   #otput : dog barks