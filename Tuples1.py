#qn1
x = ('samsung', 'iphone', 'tecno', 'redmi')
print(x[1])

#qn2
print(x[-2])

#qn3
list1 = list(x)
list1[list1.index('iphone')] = 'itel'
x = tuple(list1)
print(x)

#qn4
#using lists
list1.append('huawei')
x = tuple(list1)
print(x)

#using tuples concatenated
x = x + ('huawei',)
print(x)


#qn5
for item in x:
    print(item)
    

#qn6
#using slicicng
x = x[1:]
print(x)

#using lists
x2 = ('samsung', 'iphone', 'tecno', 'redmi')
list2 = list(x2)
del list2[0]
x2 = tuple(list2)
print(x2)



#qn7
cities = ["kla", "ebbs", "jinja", "gulu"]
print(cities)
ug = tuple(cities)
print(ug)


#qn8
a, b, c, d = ug
print(a)
print(b)
print(c)
print(d)

