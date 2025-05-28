# Super class Person
class Person:
    def __init__(self, name, person_id, email):
        self.name = name
        self.id = person_id
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")

    def update_details(self, new_name=None, new_email=None):
        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email
        print(f"Your details have been updated to\n Name: {self.name}\n Email: {self.email}")


# Subclass Student
class Student(Person):
    def __init__(self, name, person_id, email, course, year):
        super().__init__(name, person_id, email)
        self.course = course
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

    def update_details(self, new_name=None, new_email=None, new_course=None, new_year=None):
        super().update_details(new_name, new_email)
        if new_course:
            self.course = new_course
        if new_year:
            self.year = new_year
        print(f"Your details have been updated to\n Course: {self.course}\n Year: {self.year}")


# Subclass Staff
class Staff(Person):
    def __init__(self, name, person_id, email, position, office):
        super().__init__(name, person_id, email)
        self.position = position
        self.office = office

    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}")
        print(f"Office: {self.office}")

    def update_details(self, new_name=None, new_email=None, new_position=None, new_office=None):
        super().update_details(new_name, new_email)
        if new_position:
            self.position = new_position
        if new_office:
            self.office = new_office
        print(f"Your details have been updated to\n Position: {self.position}\n Office: {self.office}")


# ==== INTERACTIVE DEMO ==== #

# Person
print("____Person____")
person1 = Person("Kira", 3, "kira@gmail.com")
person1.display_info()

print("\n--- Update Person Info ---")
p_name = input("Enter new name: ")
p_email = input("Enter new email: ")
person1.update_details(new_name=p_name, new_email=p_email)
person1.display_info()

print("\n\n")

# Student
print("____Student____")
student1 = Student("Mita", 4, "mita@gmail.com", "BSC", 2)
student1.display_info()

print("\n--- Update Student Info ---")
s_name = input("Enter new name: ")
s_email = input("Enter new email: ")
s_course = input("Enter new course: ")
s_year = input("Enter new year: ")
student1.update_details(new_name=s_name, new_email=s_email, new_course=s_course, new_year=int(s_year))
student1.display_info()

print("\n\n")

# Staff
print("____Staff____")
staff1 = Staff("Herbert", 5, "her@gmail.com", "Admin", "L03")
staff1.display_info()

print("\n--- Update Staff Info ---")
st_name = input("Enter new name: ")
st_email = input("Enter new email: ")
st_position = input("Enter new position: ")
st_office = input("Enter new office: ")
staff1.update_details(new_name=st_name, new_email=st_email, new_position=st_position, new_office=st_office)
staff1.display_info()
