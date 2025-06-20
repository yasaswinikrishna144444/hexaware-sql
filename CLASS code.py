# Student Class
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
print("------ Student Info ------")
student1 = Student(101, "Yasaswini Krishna")
student2 = Student(102, "Anika singh")
student3 = Student(104, "vimala sharma")
student4 = Student(105, "Greeshma Reddy")
student1.display()
student2.display()
student3.display()
student4.display()

#  Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width
    
print("\n------ Rectangle Area ------")
rect = Rectangle(5, 4)
print("Length:", rect.length)
print("Width:", rect.width)
print("Area:", rect.compute_area())

#  Employee Class with Overtime
class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_overtime(self, hours, rate_per_hour):
        return hours * rate_per_hour

print("\n------ Employee Overtime ------")
emp1 = Employee(201, "Shreya", 50000, "HR")
overtime_pay = emp1.calculate_overtime(5, 200)
print("Employee Name:", emp1.name)
print("Overtime Pay:", overtime_pay)


#  Sum and Product of a List
def sum_and_product(numbers):
    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total_sum, product

print("\n------ Sum & Product of List ------")
numbers = [2, 3, 4]
sum_result, product_result = sum_and_product(numbers)
print("Numbers:", numbers)
print("Sum:", sum_result)
print("Product:", product_result)


#  String Reversal
def reverse_string(s):
    return s[::-1]
print("\n------ String Reversal ------")
text = "Hexaware"
print("Original String:", text)
print("Reversed String:", reverse_string(text))




