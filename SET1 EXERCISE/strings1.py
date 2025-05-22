#qn1
#normal conactenation
name = "Jesus"
age = 34
print(name + " is " + str(age) + " years old.")
#using f-strings
message = f"{name} is {age} years old."
print(message)
#using format method
message2 = "{} is {} years old".format(name, age)
print(message2)


#qn2
txt = "      Hello,       Uganda!       "
txt = txt.replace(" ", "")
print(txt)

#qn3
text = txt.upper()
print(text)

#qn4
text = text.replace("U", "V")
print(text)

#qn5
y = "I am proudly Ugandan"
result = y[1:4]
print(result)

#qn6
#using single quotes outside
x = 'All "Data Scientists" are cool'
print(x)
#using backslahes
x = "All \"Data Scientists\" are cool"
print(x)
