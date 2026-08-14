
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
        self.pay = int(self.pay * self.raise_amount) # #we can use Doctor.raise_amount instead of self.raise_amount but it is not a good practice because if we change the raise_amount for a specific instance then it will affect the other instances. So it is better to use self.raise_amount
      
    @classmethod # #we are using classmethod to get the info of doctor from string to to list format and will add them to Doctor class 
    def from_str(cls, doc_str):
      name, age , specialization, pay = doc_str.split('-')
      return cls(name , age , specialization, pay)
  
        

Doctor1 = Doctor("Dr. Jhatka", 45, "Cardiologist", 50000)
Doctor2 = Doctor("Dr. bottle", 50, "Neurologist", 60000)
Doctor3 = Doctor("Dr. earbuds", 40, "Dermatologist", 40000) 
Doctor4 = Doctor("Dr. book", 35, "Dentist", 45000)



new_docstr_1 = 'Dr. gorrila-44-zoologist-80000' #new doctors as string format 
new_docstr_2 = 'Dr.porcupine-55-icecreamian-90000'
new_docstr_3 = 'Dr. vanilla-33-chocolateologist-70000'

new_doc1 = Doctor.from_str(new_docstr_1)    # here with the help of @classmethod we created we adding new doctor's data of string format to the Doctor class and creating new instance of Doctor class with the help of from_str method.
new_doc2 = Doctor.from_str(new_docstr_2) 
new_doc3 = Doctor.from_str(new_docstr_3)
    
# Number of Doctors
print(Doctor.num_of_emps)

# Doctor names
print(Doctor1.name)
print(Doctor2.name)

# Applying raise
Doctor1.apply_raise()

print(Doctor1.pay)
