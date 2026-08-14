#class for doctors in hospital with name , age , specialization , pay 
#class instances are included in this programm 

class Doctor: 
    def __init__(self, name, age , specialization, pay): 
        self.name = name 
        self.age = age 
        self.specialization = specialization 
        self.pay = pay

    def display(self): 
        print("Name:", self.name) 
        print("Age:", self.age) 
        print("Specialization:", self.specialization) 
        print("Pay:", self.pay)

    def display_specialization(self):
        print("Specialization:", self.specialization)

    def display_pay_per_year(self):
        print("Pay per year:", self.pay * 12)

Doctor1 = Doctor("Dr. Jhatka", 45, "Cardiologist", 50000)
Doctor2 = Doctor("Dr. bottle", 50, "Neurologist", 60000)
Doctor3 = Doctor("Dr. earbuds", 40, "Dermatologist", 40000) 
Doctor4 = Doctor("Dr. book", 35, "Dentist", 45000)

print(Doctor1.display_specialization())
print(Doctor.display_specialization(Doctor1))
  #if we dont use '()' then it will not call the function and will return the memory location of the function 


print("-----------------------------------")




print(Doctor2.display_pay_per_year())




print("-----------------------------------")



print(Doctor3.display_specialization())



print("-----------------------------------")




Doctor.display(Doctor1)




print("-----------------------------------")



Doctor.display_pay_per_year(Doctor4)



