def grade_calculator(exam_scores_list):
    if len(exam_scores_list) == 0:
        return "No scores to calculate", None

    total_points = 0
    for score in exam_scores_list:
        total_points += score

    average_score = total_points / len(exam_scores_list)

    if average_score >= 90:
        letter_result = "A"
    elif average_score >= 80:
        letter_result = "B"
    elif average_score >= 70:
        letter_result = "C"
    elif average_score >= 60:
        letter_result = "D"
    else:
        letter_result = "F"

    return round(average_score, 2), letter_result


print("Welcome to Grade Calculator ")
user_input = input("Enter exam scores separated by commas (e.g. 78,85,90): ")
exam_scores = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]
average, grade = grade_calculator(exam_scores)

print("────────────────────────────")
print("Average Score:", average)
print("Final Grade:", grade)