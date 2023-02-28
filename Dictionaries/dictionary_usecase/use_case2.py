student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88,
  "Ewan": 79,
  "Park": 62,
}
def covert_grades(p_dict):
    student_grades = {}
    for key in p_dict:
        score = p_dict[key]
        if score >=85:
            student_grades[key] = "Outstanding"
        elif score >=65:
            student_grades[key] = "Good"
        elif score >= 50:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"

    return student_grades




print(covert_grades(student_scores))