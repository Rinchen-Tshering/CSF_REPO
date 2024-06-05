class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Creating objects
student1 = Student(name="Alice", age=20, cid_number="S12345", student_id="1001", course="Computer Science", year=2, gpa=3.8)
teacher1 = Teacher(name="Mr. Smith", age=45, cid_number="T67890", subject="Mathematics", salary=50000, department="Science", designation="Professor")

# Demonstrating behaviors
student1.walk()
student1.talk()
student1.eat()
student1.sleep()
student1.study()
student1.attend_class()
student1.write_exam()

teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()
