class Delivery:
    def send_package(self, name = None, address = None, type = None, time = None):
        if name and address and type and time:
            print(f"Sending a {type} {name}, to {address} at {time}")
        elif name and address and time:
            print(f"Sending a {name}, to {address} at {time}")
        elif address and time:
            print(f"Sending to {address} at {time}")
        elif address:
            print(f"Sending to {address}")
        else:
            print("No delivery details provided")
           
        
        
delivery1 = Delivery()
delivery1.send_package(name = "Cup", address = "Kampala", type = "Fragile", time = "09:00 AM")
delivery1.send_package(name = "Cup", address = "Kampala", time = "09:00 AM")
delivery1.send_package(address = "Kampala", time ="09:00 AM")
delivery1.send_package(address = "Kampala")
delivery1.send_package()



