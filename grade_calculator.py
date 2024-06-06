def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Patrick Allen")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("90")
    science_score = input("80")
    english_score = input("70")
    math_score = int(math_score)
    science_score = int(science_score)
    english_score = int(english_score)
    # Calculate the average grade
    average_grade = (math_score + science_score +english_score) / 3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"Student Name: {student_name}")
    print(f"Average Grade: {average_grade}")