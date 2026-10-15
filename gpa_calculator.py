number_of_courses = int(input("How many classes are you entering? "))
total_quality_points = 0
total_credits = 0
for course_number in range(number_of_courses):
    course = input("Enter the course name: ")
    grade = input("Enter your letter grade: ")
    credits = float(input("Enter the credit hours: "))

    grade = grade.upper()
    if grade == "A":
        points = 4.0
    elif grade == "B":
        points = 3.0
    elif grade == "C":
        points = 2.0
    elif grade == "D":
        points = 1.0
    elif grade == "F":
        points = 0.0
    else:
        print("Please enter A, B, C, D, or F.")
    if grade in ["A", "B", "C", "D", "F"]:
        quality_points = points * credits
        total_quality_points = total_quality_points + quality_points
        total_credits = total_credits + credits
        print("Quality points:", quality_points)
if total_credits > 0:
    gpa = total_quality_points / total_credits
    print("Your GPA:", round(gpa, 2))
else:
    print("No GPA calculated because total credit hours are zero.")