import teacher
import student

student_list = list()
teacher_list = list()

student2 = student.Student("Ayça", "Güven", 21, "Yazılım Kalite ve Test")
student_list.append(student2)
student.Student.printdetails(student2)

student3 = student.Student("Hilal", "Cebel", 21, "Yazılım Kalite ve Test")
student_list.append(student3)
student.Student.printdetails(student3)

student4 = student.Student("Nisanur", "Baş", 21, "Yazılım Kalite ve Test")
student_list.append(student4)
student.Student.printdetails(student4)

student5 = student.Student("Eray", "Koç", 21, "Yazılım Kalite ve Test")
student_list.append(student5)
student.Student.printdetails(student5)

student6 = student.Student("Serpil Nur","Karaman", 21, "Yazılım Kalite ve Test")
student_list.append(student6)
student.Student.printdetails(student6)

teacher1= teacher.Teacher("İrem", "Balcı", 25, "Yazılım Kalite ve Test")
teacher_list.append(teacher)
teacher.Teacher.printdetails(teacher1)
