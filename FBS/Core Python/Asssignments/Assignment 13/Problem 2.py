student = {'name': 'nilesh', 'age': 20, 'course': 'python'}

emp = {'name': 'rohit', 'salary': 50000, 'department': 'IT'}

# data = {**student, **emp}
student.update(emp)

print(student)