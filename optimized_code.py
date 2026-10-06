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
    return sum(marks) / len(marks)


def process_students(students):
    results = []

    for student in students:
        average = calculate_average(student["marks"])

        results.append({
            "id": student["id"],
            "name": student["name"],
            "average": average
        })

    # Optimized: sort once instead of comparing every student
    results.sort(key=lambda student: student["average"], reverse=True)

    top_students = results[:10]

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