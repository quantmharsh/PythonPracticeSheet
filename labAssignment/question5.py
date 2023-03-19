marks = []
sd_cal = []
sd_cal2 = []
total_students = int(input("Enter the total number of students : "))
total_marks = 0
total_mark_sqr = 0
mrks = 0

for i in range (0,total_students):
    student_marks = int(input("Enter the marks of student "+ str(int(i + 1)) +": "))
    marks.append(student_marks)

for i in range (0,total_students):
    total_marks = total_marks + marks[i]

avg_marks = int(total_marks / total_students)

for i in range (0,total_students):
    mark = marks[i] - avg_marks
    sd_cal.append(mark)
    mark_sqr = mark * mark
    sd_cal2.append(mark_sqr)

for i in range (0, total_students):
    mrks = mrks + sd_cal[i]

for i in range (0, total_students):
    total_mark_sqr = total_mark_sqr + sd_cal2[i]


variance = total_mark_sqr / (total_students - 1)

sd = variance**0.5

md = mrks / total_students

md_by_mean = md / avg_marks

print(sd_cal)
print(sd_cal2)
print(sd)
print(mrks)
print(md)
print(md_by_mean)