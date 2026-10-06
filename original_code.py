import random
import time


def generate_student_data(num_students):
    students = []

    for i in range(num_students):
        marks = [
            random.randint(40, 100),
            random.randint(40, 100),
            random.randint(40, 100),
            random.randint(40, 100),
            random.randint(40, 100)
        ]

        students.append({
            "id": i + 1,
            "name": "Student_" + str(i + 1),
            "marks": marks
        })

    return students


def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def process_students(students):
    results = []

    for student in students:
        average = calculate_average(student["marks"])

        # Store the calculated result
        results.append({
            "id": student["id"],
            "name": student["name"],
            "average": average
        })

    # Inefficient repeated searching
    top_students = []

    for student in results:
        count = 0

        for other_student in results:
            if other_student["average"] > student["average"]:
                count += 1

        if count < 10 and len(top_students) < 10:
           top_students.append(student)

    return top_students


def main():
    start_time = time.time()

    students = generate_student_data(5000)

    top_students = process_students(students)

    end_time = time.time()

    print("Student Performance Analyzer")
    print("----------------------------")
    print("Total students:", len(students))
    print("Top students found:", len(top_students))
    print("Execution time:", round(end_time - start_time, 4), "seconds")


if __name__ == "__main__":
    main()