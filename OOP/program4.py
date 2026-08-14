
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

    @classmethod
    def from_str(cls, doc_str):
        name, age, specialization, pay = doc_str.split('-')
        return cls(name, int(age), specialization, int(pay))



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


#MAKING A NEW SUBCLASS 

class SeniorDoctor(Doctor):
    raise_amount = 1.10
 
    def __init__(self, name, age , specialization, pay, years_of_experience , doctors=None): #we can provide list rather than none here 
        super().__init__(name, age , specialization, pay)                    # here the doctors list contains the list of junior doctors working under the senior doctor. If the list is not provided then it will be an empty list.
        self.years_of_experience = years_of_experience
        self.doctors = doctors if doctors is not None else [] #if the doctors list is not provided then it will be an empty list.

    def addDoctor(self , doc):
        if doc not in self.doctors:
            self.doctors.append(doc) #adding a new doctor to the list of doctors working under the senior doctor. 

    def removeDoctor(self , doc):
        if doc in self.doctors:
            self.doctors.remove(doc) #removing a doctor who's working under the senior doctor 



class JuniorDoctor(Doctor):
    raise_amount = 1.05

    def __init__(self, name, age , specialization, pay, mentor = None ,): #we can provide a mentor rather than none here 
        super().__init__(name, age , specialization, pay)
        self.mentor = mentor #if the mentor is not provided then it will be None.


SD1 = SeniorDoctor( 'Dr. Umangasauras' , 1735 , 'life' , 0.22 , 1700 )
SD2 = SeniorDoctor( 'Dr. Sinchansauras' , 6 , 'mental health' , 10 , 2 )

#something important - here if we create a new instance let's say JD3 then the JD3 will not be stored in the class JuniorDoctor , a class never stores the data its just a template or we can say blueprint for creating the instances. So if we want to store the data of the instances then we have to create a list and store the instances in that list.

JD1 = JuniorDoctor( 'Dr. cupcake' , 30 , 'pediatrics' , 50000 , SD1 )
JD2 = JuniorDoctor( 'Dr. frooti' , 35 , 'dentistry' , 60000 , None )

SD1.addDoctor(JD1) #adding a new doctor to the list of doctors working under the senior doctor.

# Number of Doctors
print(Doctor.num_of_emps)

# Doctor names
print(Doctor1.name)
print(Doctor2.name)

#getting mentor names -
print("\n--- Junior Doctor Mentors ---")
print(JD1.name, "-> Mentor:", JD1.mentor.name)
print(JD2.name, "-> Mentor:", JD2.mentor)


#Removing doctor from the list of doctors working under the senior doctor.
print("\n--- Removing Doctor ---")
print("Before:", [doctor.name for doctor in SD1.doctors])
SD1.removeDoctor(JD1)
print("After:", [doctor.name for doctor in SD1.doctors])

#here -- Before: ['Dr. cupcake']
#        After: []
#here the doctor is removed from the list of doctors working under the senior doctor.
#but the object will still remain there , just the connection is breaked ,also we can the object JD1 is no longer a part of list "doctors" under Senior doctor . 


#ADDING DOCTOR TO THE LIST OF DOCTORS WORKING UNDER THE SENIOR DOCTOR.
# Testing addDoctor() and duplicate prevention

print("\n--- Testing addDoctor() ---")
print("Before:", [doctor.name for doctor in SD1.doctors])

SD1.addDoctor(JD1)
SD1.addDoctor(JD1)

print("After:", [doctor.name for doctor in SD1.doctors])

#--- Testing addDoctor() ---
#   Before: ['Dr. cupcake']   ,-- on line 76 -- since i already added JD1 to the list of doctors working under the senior doctor SD1 
#   After: ['Dr. cupcake']

help(SeniorDoctor) 
# this help() function will give us the information about the class SeniorDoctor and its methods and attributes. It will also give us the information about the parent class Doctor and its methods and attributes.
