# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {student:random.randint(1,100) for student in names}
# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_student)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# result = {word:len(word) for word in sentence.split(' ')}

# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:

# weather_f = {day:c*9/5+32 for (day, c) in weather_c.items()}

# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Looping through a data frame:
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame:
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)