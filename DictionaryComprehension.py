import random
import pandas

names = ['Alice', 'Bob', 'Charlie']
student_scores = {item:random.randint(1,100) for item in names }
print(student_scores)
passed_students = {item:score for (item, score) in student_scores.items() if score >= 60}
print(passed_students)

for (key, value) in student_scores.items():
    print(f"{key}: {value}")

student_data_frame = pandas.DataFrame(student_scores.items(), columns=['Student', 'Score'])
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.Score >= 60:
        print(f"{row.Student} passed the exam with a score of {row.Score}")