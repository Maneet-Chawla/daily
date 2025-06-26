class car:
    def __init__(self,brand,color):  #init is special method used in class .
        #self helps  in creating new object
        # #constructor special method to initialize object
        self.brand =brand #these are the parameter
        self.color =color
    def start(self):
        print("{self.brand} car in {self.color} color is starting...")

        #creaing an object
my_car = car("Toyota","red")
my_car2 = car("bmw","blue")
my_car.start() #with this new object we can create methods
my_car2.start()