student_scores = {
    "Harry"   : 81,
    "Ron"     : 78,
    "Hermione": 99,
    "Draco"   : 74,
    "Neville" : 62,
}

student_grades = {}

grade_list = ["Outstanding", "Exceeds Expectations", "Acceptable", "Fail"]

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = grade_list[0]
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = grade_list[1]
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = grade_list[2]
    elif student_scores[key] <= 70:
        student_grades[key] = grade_list[3]

for key in student_grades:
    print(f"{key}: {student_grades[key]}")