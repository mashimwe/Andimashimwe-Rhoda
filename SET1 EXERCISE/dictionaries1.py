#qn1
Shoes = {
	"brand" : "Nick",
	"color" : "black",
	"size" : 40
	}
print(Shoes["size"])

#qn2
Shoes["brand"] = "Adidas"
print(Shoes)
print(Shoes["brand"] )

#qn3
Shoes["type"] = "sneakers"
print(Shoes)

#qn4
all_keys = Shoes.keys()
print(all_keys)

#qn5
all_values = Shoes.values()
print(all_values)

#qn6
size_in = "size" in Shoes
print(size_in)

#qn7
#looping through keys
for key in Shoes:
    print(key)
#values
for value in Shoes.values():
    print(value)
#both
for key, value in Shoes.items():
    print(f"{key}: {value}")
    

#qn8
#using del
del Shoes["color"]
print(Shoes)
# using pop
avalue = Shoes.pop("size")
print(avalue)
print(Shoes)


#qn9
Shoes.clear()
print(Shoes)


#qn10
#using the dict constructor
presido = {"country": "Uganda", "reign": 40 }
new_presido = dict(presido)
print(new_presido)
#using the copy() method
new_pre = presido.copy()
print(new_pre)


#qn11
cars = {
    "car1": {
        "name": "mercedes",
        "mileage": 40
    },
    "car2": {
        "name": "toyota",
        "mileage": 56
    }
}

print(cars)