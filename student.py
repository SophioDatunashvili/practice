class Student:
	current_id = 0
	
	def __init__(self, first_name, last_name, age, course):
		self.id = Student.current_id
		Student.current_id += 1
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.course = course


class StudentManager:
	def __init__(self):
		self.students = {}
	
	def add_student(self, *args, **kwargs):
		student = Student(*args, **kwargs)
		self.students[student.id] = student
	
	def delete_student(self, id):
		if id in self.students:
			del self.students[id]
	
	def update_student(self, id, **kwargs):
		if id in self.students:
			student = self.students[id]
			for key, value in kwargs.items():
				student.key = value
	
	def display(self):
		for id, student in self.students.items():
			print(f"{student.id=},{student.first_name=}, {student.last_name=}, {student.age=}, {student.course=}")
	
	def find_student(self, id):
		if id in self.students:
			student = self.students[id]
			print(f"{student.id=},{student.first_name=}, {student.last_name=}, {student.age=}, {student.course=}")


sm = StudentManager()
sm.add_student("sopo", "da", 24, "comp")
# # print(sm.students)
# # sm.display()
sm.update_student(1, first_name="ako")
sm.add_student("sopo", "dhlc", 45, "csldbv")
sm.update_student(1, first_name="ako")
sm.find_student(1)

sm1 = StudentManager()

print(sm.students)
print(sm1.students)