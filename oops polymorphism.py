class Bird:#same method name ,different behaviour.
    def sound(self):
        print("some generic bird soound ")
class parrot(Bird):
    def sound(self):
        print("parrot says:squawk!")
class sparrow(Bird):
    def sound(self):
        print("sparrow says: chirp!")

#using polymorphism
for bird in[parrot(), sparrow()]: bird.sound()