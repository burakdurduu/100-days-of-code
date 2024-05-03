student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆


student_grades = {}
for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Exceeds Expectations"    
    elif student_scores[i] > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
