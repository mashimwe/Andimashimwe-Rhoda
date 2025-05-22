# #qn1
# people = ["Fabrice", "Esther", "Nelly", "Emma", "Ange"]
# print(people[1])

# #qn2
# people[0] = "Nyirinkindi"
# print(people)

# #qn3
# people.append("Kansiime")
# print(people)

# #qn4
# people.insert(2, "Bathel")
# print(people)

# #qn5
# del people[3]
# print(people)

# #qn6
# print(people[-1])

# #qn7
# new_people = ["ann", "lia", "nina", "mia", "kia", "kate", "bec"]
# print(new_people[2:5])

# #qn8
# countries = ["Usa", "UK", "China"]
# print(countries)
# copy = countries[:]
# print(copy)
# copy.append("Algeria")
# print(copy)
# print(countries)

# #qn9
# for cntry in countries:
#     print(cntry)
    
# #qn10
# #using sort()
# ani_names = ["pig", "dog", "rat"]
# ani_names.sort()
# print(ani_names)
# ani_names.sort(reverse=True)
# print(ani_names)

# #using sorted()
# anima_names = ["gira", "ele", "lio"]
# new_anis = sorted(anima_names)
# print(anima_names)
# print(new_anis)
# new_anis2 = sorted(anima_names, reverse=True)
# print(new_anis2)

# #qn11
# anima_names = ["gira", "ele", "lio"]
# letter = "l"
# with_letter_l = [name for name in anima_names if letter.lower() in name.lower()]
# print(with_letter_l)

#qn12
#using + operator
first_names = ["rhoda", "Anna"]
last_names = ["Andimashimwe", "Uwimana"]
combined = first_names + last_names
print(combined)

#using .extend() method
first_names2 = ["rho", "Ann"]
last_names2 = ["Andimwe", "Uwa"]
first_names2.extend(last_names2)
print(first_names2)

#using unpacking
first_names3 = ["rda", "na"]
last_names3 = ["Ashimwe", "Uwi"]
combined2 = [*first_names3, *last_names3]
print(combined2)