# base class
class Appliances:
    def connect_to_socket(self):
        print("Connecting to socket...")
        
    # method to be overridden
    def turn_on(self):
        print("Turning on the appliance")
        
        
# subclass1
class Microwave(Appliances):
    def turn_on(self):
        print ("Microwave turning on..\nFirst light then start the timer.")
        
        

# subclass2
class Washing_Machine(Appliances):
    def turn_on(self):
        print("Washing Machine turning on..\nPrepare drum and select cycle")
        
        
app = Appliances()
app.connect_to_socket()
app.turn_on()

micro = Microwave()
micro.connect_to_socket()
micro.turn_on()

wmach = Washing_Machine()
wmach.connect_to_socket()
wmach.turn_on()
