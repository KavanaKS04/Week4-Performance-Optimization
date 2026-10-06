from original_code import process_students as original_process
from optimized_code import process_students as optimized_process


def test_same_functionality():
    students = [
        {"id": 1, "name": "Student_1", "marks": [80, 85, 90, 75, 95]},
        {"id": 2, "name": "Student_2", "marks": [70, 75, 80, 85, 90]},
        {"id": 3, "name": "Student_3", "marks": [90, 92, 88, 95, 94]},
        {"id": 4, "name": "Student_4", "marks": [60, 65, 70, 75, 80]},
        {"id": 5, "name": "Student_5", "marks": [85, 88, 90, 92, 87]}
    ]

    original_result = original_process(students)
    optimized_result = optimized_process(students)

    original_averages = sorted(
        [round(student["average"], 2) for student in original_result],
        reverse=True
    )

    optimized_averages = sorted(
        [round(student["average"], 2) for student in optimized_result],
        reverse=True
    )

    assert original_averages == optimized_averages

    print("Functionality test passed!")
    print("Original averages:", original_averages)
    print("Optimized averages:", optimized_averages)


if __name__ == "__main__":
    test_same_functionality()