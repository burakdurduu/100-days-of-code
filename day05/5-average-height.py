# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

items = 0
result = 0
for num in student_heights:
    result += num
    items += num / num
    final_result = result / items
print(round(final_result))
