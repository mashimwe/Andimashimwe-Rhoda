#qn1
bevs = set(["water", "juice", "milkshake"])
print(bevs)

#qn2
bevs.add("chocolate tea")
print(bevs)

bevs.update(["caraeml tea", "coffe"])
print(bevs)

#qn3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

#qn4
mySet.remove("kettle")
print(mySet)

#qn5
for item in mySet:
    print(item)

#qn6
set1 = {7, 5, 3, 4}
list1 = [1, 2]

set1.update(list1)
print(set1)

#qn7
ages = {12, 34, 78, 45}
fnames1 = {"anna", "nelly", "esther", "mama"}

joinedd = ages.union(fnames1)
print(joinedd)