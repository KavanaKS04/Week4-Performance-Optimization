# Week 4 Task - Performance Optimization in Python Applications

## 1. Project Title

**Student Performance Analyzer - Python Performance Optimization**

## 2. Objective

The objective of this project is to identify performance bottlenecks in a Python application, optimize the inefficient parts of the program, and measure the improvement using profiling and benchmarking techniques.

## 3. Application Description

The application generates data for 5000 students. Each student has five subject marks.

The application:

* Generates student data.
* Calculates the average marks of each student.
* Identifies the top 10 students.
* Displays the total number of students, number of top students, and execution time.

Two versions were developed:

1. Original implementation
2. Optimized implementation

## 4. Original Implementation

The original implementation used nested loops to find the top students.

For every student, the program compared that student's average with every other student's average.

This resulted in a large number of repeated comparisons and caused a significant performance bottleneck.

The average calculation also used a manual loop to add all marks.

## 5. Performance Bottleneck Identification

The original program was analyzed using Python's `cProfile` module.

The main bottleneck was the `process_students()` function.

The profiling showed that the nested comparison operation consumed most of the execution time.

The original implementation performed approximately O(n²) comparisons when ranking students.

For 5000 students, this results in approximately 25 million pairwise comparisons.

## 6. Optimization Techniques Applied

### 6.1 Replaced Manual Summation

Original implementation:

```python
total = 0

for mark in marks:
    total += mark

return total / len(marks)
```

Optimized implementation:

```python
return sum(marks) / len(marks)
```

The Python built-in `sum()` function is simpler and more efficient.

### 6.2 Removed Repeated Comparisons

The original implementation repeatedly compared every student with every other student.

The optimized implementation sorts the results once:

```python
results.sort(key=lambda student: student["average"], reverse=True)
```

Then the first 10 students are selected:

```python
top_students = results[:10]
```

This changes the ranking operation from approximately O(n²) to O(n log n).

### 6.3 Reduced Redundant Processing

The optimized implementation avoids repeated searching and comparison operations and performs the ranking in a single sorting operation.

## 7. Profiling Results

Python's `cProfile` module was used to analyze both implementations.

### Original Version

The original `process_students()` function was the main performance bottleneck.

The nested comparison operation consumed the majority of the program's execution time.

### Optimized Version

After optimization, the `process_students()` function required significantly less processing time.

The sorting operation completed much faster than the repeated nested comparisons.

The profiling results are included in:

* `profile_original.txt`
* `profile_optimized.txt`

## 8. Benchmark Method

The application was executed five times for both versions.

The average execution time was calculated from the five runs.

### Original Execution Times

* 1.0585 seconds
* 1.0871 seconds
* 1.0958 seconds
* 1.1159 seconds
* 1.0842 seconds

**Average: 1.0883 seconds**

### Optimized Execution Times

* 0.0099 seconds
* 0.0095 seconds
* 0.0094 seconds
* 0.0094 seconds
* 0.0102 seconds

**Average: 0.0097 seconds**

## 9. Performance Comparison

| Metric                  |       Original |      Optimized |
| ----------------------- | -------------: | -------------: |
| Average execution time  | 1.0883 seconds | 0.0097 seconds |
| Performance improvement |              — |         99.11% |
| Speedup                 |             1× |        112.43× |
| Students processed      |           5000 |           5000 |
| Top students returned   |             10 |             10 |

The optimized application achieved a **99.11% reduction in execution time** and was approximately **112.43 times faster** than the original implementation.

## 10. Correctness Verification

A separate functionality test was created in `test_functionality.py`.

The test used the same student data for both implementations and compared their calculated average results.

The test produced:

```text
Functionality test passed!
Original averages: [91.8, 88.4, 85.0, 80.0, 70.0]
Optimized averages: [91.8, 88.4, 85.0, 80.0, 70.0]
```

Therefore, the optimized implementation produces the same calculated results as the original implementation for the test data.

## 11. Files Included

The project contains the following files:

* `original_code.py` - Original inefficient implementation
* `optimized_code.py` - Optimized implementation
* `benchmark.py` - Benchmarking script
* `test_functionality.py` - Correctness verification script
* `profile_original.txt` - Profiling data for the original version
* `profile_optimized.txt` - Profiling data for the optimized version
* `performance_report.md` - Detailed performance optimization report

## 12. Conclusion

The performance optimization successfully improved the Student Performance Analyzer.

The main bottleneck was identified using profiling and was caused by the O(n²) nested comparison approach.

By replacing repeated comparisons with sorting and replacing manual summation with the built-in `sum()` function, the application became significantly faster.

The benchmark showed:

**99.11% performance improvement**

and

**112.43× speedup**

while maintaining the required functionality and producing the same calculated results in the correctness test.

This demonstrates that appropriate algorithmic and code-level optimizations can substantially improve Python application performance.
