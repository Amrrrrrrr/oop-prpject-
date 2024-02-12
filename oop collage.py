#!/usr/bin/env python
# coding: utf-8

# In[184]:


# oop collage proj
class person :
    def __init__(self,name,gender,age,iid):
        self.name=name
        self.age=age
        self.gender=gender
        self.iid=iid
    def displayinfo(self):
        print(f" Name: {self.name}   age:{self.age}  Gender: {self.gender}  id:{self.iid}")


# In[185]:


class course :
    def __init__(self,name,specialization,credithour):
        self.name=name
        self.specialization=specialization
        self.credithour=credithour
    def displayinfo(self):
        print(f" course Name: {self.name} specialization:{self.specialization}  credit hour: {self.credithour}")
        


# In[186]:


class student (person):
    def __init__(self,name,gender,age,iid,specialization,gpa,passedhours):
        super().__init__(name,age,gender,iid)
        self.gpa=gpa
        self.specialization=specialization
        self.passedhours=passedhours
        self.course=[]
    def displayinfo(self):
        super().displayinfo()
        print(f"speciallization:{self.specialization}  gpa: {self.gpa}   passed hours : {self.passedhours}")
       
            
        
              
            


# In[187]:


class Doctor(person):
    def __init__(self, name, gender, age, iid,salary):
        super().__init__(name, age, gender, iid)
        self.salary =salary
        self.courses = []

    def displayinfo(self):
        super().displayinfo()
        print(f"Salary is: {self.salary}")
        print("Courses are:")
        for course in self.courses:
            print(course.name)

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.name}' assigned to Doctor: {self.name}")
    def add_assistant(self, assistant):
        self.assistants.append(assistant)
        print(f"Doctor {assistant.name}  assigned to doctor")

    
    


# In[197]:


class Assistant (person):
    def __init__(self,name,age,gender,iid,salary):
        super().__init__(name,gender,age,iid)
        self.salary=salary
        self.courses=[]
    def add_course(self,course):
        self.courses.append(course)
        print(f"Course '{course.name}' assigned to assistant: {self.name}")
    def displayinfo(self):
        super().displayinfo()
        print(f"Salary is: {self.salary}")
        for course in self.courses:
            print(course.name)
        
        
        


# In[193]:


class collage:
    def __init__(self, name, location, study_period, university):
        self.name = name
        self.location = location
        self.study_period = study_period
        self.university = university
        self.doctors = []
        self.assistants=[]

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} is assigned to collage")
    def add_assistant(self, assistant):
        self.assistants.append(assistant)
        print(f"assitant {assistant.name} is assigned to collage")

    def display_info(self):
        print(f"University: {self.university}, Name of collage: {self.name}, Location: {self.location}")
        print("Doctors:")
        for doctor in self.doctors:
            print(doctor.name)
        print("assistants:")
        for assistant in self.assistants:
            print(assistant.name)


# In[198]:


student1 =student("ahmed", 20, "Male", 12345, "CS", 3.5, 55)
student2 =student("Alice", 22, "Female", 54321, "Engineering", 3.8, 66)
uni = "o6u"
my_college =collage("cs ", "giza", "80 hour", uni)
doctor1=Doctor("emad",55,"male",201,4000)
doctor2=Doctor("ahmed",545,"male",209,8000)
doctor3=Doctor("sara",33,"female",100,9000)
course1=course("os", "cs",4)
course2=course("it","nt",3)
course3=course("sys analysis","is",3)
assistant1=Assistant("noha",25,"female",1000,2000)
assistant2=Assistant("amr",29,"male",1200,3000)
assistant3=Assistant("mariam",22,"female",1010,1500)


course1.displayinfo()
course2.displayinfo()
student1.displayinfo()
student2.displayinfo()


my_college.add_doctor(doctor1)
my_college.add_doctor(doctor2)
my_college.add_doctor(doctor3)
my_college.add_assistant(assistant1)
my_college.add_assistant(assistant2)
my_college.add_assistant(assistant3)
my_college.display_info()


assistant1.add_course(course1)
assistant2.add_course(course2)
assistant3.add_course(course3)

doctor1.add_course(course1)
doctor2.add_course(course2)
doctor3.add_course(course3)

doctor1.displayinfo()
doctor2.displayinfo()
doctor3.displayinfo()

assistant1.add_course(course1)
assistant2.add_course(course2)
assistant3.add_course(course3)

assistant1.displayinfo()







# In[ ]:





# In[ ]:





# In[ ]:




