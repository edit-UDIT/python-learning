
class Doctor: 

    raise_amount = 1.07
    num_of_emps = 0

    def __init__(self, name, age , specialization, pay): 

        self.name = name 
        self.age = age 
        self.specialization = specialization 
        self.pay = pay

        Doctor.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

        #we can use Doctor.raise_amount instead of self.raise_amount but it is not a good practice because if we change the raise_amount for a specific instance then it will affect the other instances. So it is better to use self.raise_amount.

Doctor1 = Doctor("Dr. Jhatka", 45, "Cardiologist", 50000)
Doctor2 = Doctor("Dr. bottle", 50, "Neurologist", 60000)
Doctor3 = Doctor("Dr. earbuds", 40, "Dermatologist", 40000) 
Doctor4 = Doctor("Dr. book", 35, "Dentist", 45000)


# Number of Doctors
print(Doctor.num_of_emps)

# Doctor names
print(Doctor1.name)
print(Doctor2.name)

# Applying raise
Doctor1.apply_raise()

print(Doctor1.pay)
