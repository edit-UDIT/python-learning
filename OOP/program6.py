#here in this programm ive implemented setter , getter method and skipped deleter method ; Also we used @property decorator which allows methods to be accessed like normal attributed ( we dont need to use "()" these to call a method which is under property decoration )
#With the help of getter methods, we can access and retrieve the value of an attribute through a property while keeping the actual stored value internally 
#With setter methods, we can control what values are assigned to an attribute and validate them before storing.
#OOPs i actually went high on this :3

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
        #in formal - If you use self.raise_amount inside the method: Python looks for an instance-specific attribute first. If Doctor1 has a custom rate (1.20), it uses 1.20. If no custom rate exists on the instance, it falls back to the class default (1.07).

    @classmethod
    def from_str(cls, doc_str):
        name, age, specialization, pay = doc_str.split('-')
        return cls(name, int(age), specialization, int(pay))

    #here if we try Doctor1.pay = -50000 it will set this negative value without any error 
    #so to read the pay we will use method in property decorator
    #and to fix this problem of negative value we will assign setter method , to control what happens when someone assign a value weather valid or invalid

    @property
    def pay(self):
        return self._pay #here we have to set _pay instead of pay because if we use pay there also this will make a infinite loop and crash the memory 
                         #so here the _pay will store the actually value inside the python and whenever we fetch pay it will get the "_pay" value which is stored inside the python 
                         #Writing self.pay = value inside the setter tells Python to run the setter function again.

    @pay.setter  #using setter function here to block invalid inputs 
    def pay(self , value ):
        if value < 0 : #if value is less than 0 then it will raise an error
            raise ValueError("Pay can't be in negative")
        self._pay = value # "_pay" is the inside variable which actually holds the value and the pay is what we use and which will tell the output by fetching real value from _pay 

    @property
    def age(self):
        return self._age 

    @age.setter 
    def age(self,input):
        if input < 0 : #if input is less than 0 then it will raise an error
            raise ValueError("Age can't be negative")
        self._age = input 

    #here we can make a full_info getter too but we already did it by __str__ method where we are already getting the full info 
    #but yea to make it like normal attribute we can do it like - 
    @property
    def full_info(self):
        return '{} - {} - {} years old - {} ' .format(self.name , self.specialization , self.age , self.pay )
    #here we can direcly go for full info like - "Doctor1.full_info" and it will give the output 
    #well , this will give the same output as print(Doctor1) because we defined __str__ in this programm too 

    #another major thing is deleter , which we are not going to use it here cause we are not deleting any of full list here 
    #while we already have a .removeDoctor() method for removing the single Doctor 

#DUNDER METHODS ____________ OR WE CAN SAY MAGIC METHODS _______ OR WE CAN SAY SPECIAL METHODS 

    def __repr__(self): #this will give the developer friendly output like print(Doctor1) will give - Doctor('Dr. Jhatka', 45, 'Cardiologist', 50000)  , (also used for debugging)
        return "Doctor('{}', {}, '{}', {})".format(self.name, self.age, self.specialization, self.pay)

        #there's a difference i saw here in repr we have to use "Doctor('{}', {}, '{}', {})" 
        #while in str we dont have to use doctor there's direct format without the class name
        #because str is user friendly and rept is developer friendly also repr manually give output with class name and str is just the output of the instance of the class without the class name.

    def __str__(self): #this will give the user friendly output like print(Doctor1) will give - Dr. Jhatka - Cardiologist - 45 years old - 50000
        return '{} - {} - {} years old - {}'.format(self.name, self.specialization, self.age, self.pay)

    def __add__(self, other): #this will define what to add when we add two instances of the class Doctor , here we are adding the pay of two doctors.
        return self.pay + other.pay 

    def __len__(self): #this will give the length of the string passed in method . 
        return len(self.specialization) #here we are passing the specialization of the doctor and we are returning the length of that string.



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
 
    def __init__(self, name, age , specialization, pay, years_of_experience , Jdoctors=None): #we can provide list rather than none here 
        super().__init__(name, age , specialization, pay)                    # here the doctors list contains the list of junior doctors working under the senior doctor. If the list is not provided then it will be an empty list.
        self.years_of_experience = years_of_experience
        self.Jdoctors = Jdoctors if Jdoctors is not None else [] #if the doctors list is not provided then it will be an empty list.

    def addDoctor(self , doc):
        if doc not in self.Jdoctors:
            self.Jdoctors.append(doc) #adding a new doctor to the list of doctors working under the senior doctor. 

    def removeDoctor(self , doc):
        if doc in self.Jdoctors:
            self.Jdoctors.remove(doc) #removing a doctor who's working under the senior doctor 

class JuniorDoctor(Doctor):
    raise_amount = 1.05

    def __init__(self, name, age , specialization, pay, mentor = None ,): #we can provide a mentor rather than none here 
        super().__init__(name, age , specialization, pay)
        self.mentor = mentor #if the mentor is not provided then it will be None.

    @property #here this property will help and we wont get attribute error even if we pass mentor = none , but without this it will give error because when print funtion calss the name None is not a specified string
    def mentor_name(self):
        return self.mentor.name if self.mentor else "None"

SD1 = SeniorDoctor( 'Dr. Umangasauras' , 1735 , 'life' , 0.22 , 1700 )
SD2 = SeniorDoctor( 'Dr. Sinchansauras' , 6 , 'mental health' , 10 , 2 )

        #something important - here if we create a new instance let's say JD3 then the JD3 will not be stored in the class JuniorDoctor , a class never stores the data its just a template or we can say blueprint for creating the instances. So if we want to store the data of the instances then we have to create a list and store the instances in that list.

JD1 = JuniorDoctor( 'Dr. cupcake' , 30 , 'pediatrics' , 50000 , SD1 )
JD2 = JuniorDoctor( 'Dr. frooti' , 35 , 'dentistry' , 60000 , None )

SD1.addDoctor(JD1) #adding a new doctor to the list of doctors working under the senior doctor.

#outputs of ---- DUNDER METHODS ____________ OR WE CAN SAY MAGIC METHODS _______ OR WE CAN SAY SPECIAL METHODS 

print(repr(Doctor1))
        # Output:Doctor('Dr. Jhatka', 45, 'Cardiologist', 50000) also we can call the same output by print(Doctor1.__repr__()) 
print(Doctor1)
        # Output: Dr. Jhatka - Cardiologist - 45 years old - 50000 , Also print(str(Doctor1)) or print(Doctor1.__str__()) gives the exact same output: Dr. Jhatka - Cardiologist - 45 years 
print(Doctor1 + Doctor2)
        # Output: 110000 , Also  print(Doctor1.__add__(Doctor2)) gives the exact same output: 110000
print(len(Doctor1))
        # Output: 12 , Also print(Doctor1.__len__()) gives the exact same output: 12 , which shows the number of character in specialization


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
print("Before:", [doctor.name for doctor in SD1.Jdoctors])
SD1.removeDoctor(JD1)
print("After:", [doctor.name for doctor in SD1.Jdoctors])

#here -- Before: ['Dr. cupcake']
#        After: []
#here the doctor is removed from the list of doctors working under the senior doctor.
#but the object will still remain there , just the connection is breaked ,also we can the object JD1 is no longer a part of list "doctors" under Senior doctor . 


#ADDING DOCTOR TO THE LIST OF DOCTORS WORKING UNDER THE SENIOR DOCTOR.
# Testing addDoctor() and duplicate prevention

print("\n--- Testing addDoctor() ---")
print("Before:", [doctor.name for doctor in SD1.Jdoctors])

SD1.addDoctor(JD1) #applying addDoctor method to add a junior doctor in Jdoctors's list working under Senior doctor 
SD1.addDoctor(JD1)

print("After:", [doctor.name for doctor in SD1.Jdoctors])

#--- Testing addDoctor() ---
#   Before: ['Dr. cupcake']   ,-- on line 76 -- since i already added JD1 to the list of doctors working under the senior doctor SD1 
#   After: ['Dr. cupcake']

print(help(SeniorDoctor))
# this help() function will give us the information about the class SeniorDoctor and its methods and attributes. It will also give us the information about the parent class Doctor and its methods and attributes.
