import statistics

def load_files(diary, filename1, filename2, filename3):
    with open(filename1) as file:
        for line in file:
            student_data = line.strip("\n").split(' ')
            create_student(diary, int(student_data[0]), student_data[1], student_data[2])
     
    with open(filename2) as file:
        for line in file:
            grades_data = line.strip("\n").split(' ')
            add_grade(diary, int(grades_data[0]), grades_data[1], int(grades_data[2]))

    with open(filename3) as file:
        for line in file:
            attendance_data = line.strip("\n").split(' ')
            add_attendance(diary, int(attendance_data[0]), attendance_data[1], int(attendance_data[2]))

def create_diary():
    diary = {
        "students" : {},
    }
    return diary

def create_student(diary, id:int, name:str, surname:str):
    diary["students"][id] = {
        "name" : name,
        "surname" : surname,
        "grades" : {},
        "attendance": {}
    }

def add_grade(diary, id:int, subject:str, grade:int):
    student = diary["students"][id]
    if subject not in student["grades"]:
        student["grades"][subject] = []
    student["grades"][subject].append(grade)

def add_attendance(diary, id:int, subject:str, presence):
    student = diary["students"][id]
    if subject not in student["attendance"]:
        student["attendance"][subject] = []
    student["attendance"][subject].append(presence)

def average_subject_score(diary, subject_name:str, id:int):
    student = diary["students"][id]
    avg = statistics.mean(student["grades"][subject_name])
    return avg

def total_average_score(diary, id:int):
    student = diary["students"][id]
    avg = statistics.mean([grade for grades in student["grades"].values() for grade in grades])
    return avg

def total_attendance(diary, id:int):
    student = diary["students"][id]
    avg = statistics.mean([presence for attendance in student["attendance"].values() for presence in attendance])
    return avg * 100

def average_subject_attendance(diary, subject_name:str, id:int):
    student = diary["students"][id]
    avg = statistics.mean(student["attendance"][subject_name])
    return avg * 100

def load_to_file(diary, filename):
    with open(filename, "w") as file:
        for student_id, student in diary["students"].items():
            file.write(f'{student["name"]} {student["surname"]}\nGrades:\n')
            for subject, grades in student["grades"].items():
                file.write(f'{subject}: {grades}, average: {average_subject_score(diary, subject, student_id):3.2f}\n')
            file.write(f'Total average score: {total_average_score(diary, student_id):3.2f}\n')

            file.write("\nAttendance:\n")
            for subject, presence in student["attendance"].items():
                file.write(f'{subject}: {presence}, average: {average_subject_attendance(diary, subject, student_id):3.2f}%\n')
            file.write(f'Total attendance: {total_attendance(diary, student_id):3.2f}%\n\n')

if __name__ == "__main__":
    diary = create_diary()
    load_files(diary, "students.txt", "grades.txt", "attendance.txt")
    load_to_file(diary, "result.txt")