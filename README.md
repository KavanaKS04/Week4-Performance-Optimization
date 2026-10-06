# Student Performance Analyzer

## Week 4 - Performance Optimization in Python Applications

### Project Overview

This project demonstrates performance optimization of a Python application.

The application generates data for 5000 students, calculates their average marks, and identifies the top 10 students.

Two implementations are provided:

* Original implementation
* Optimized implementation

### Files

| File                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `original_code.py`      | Original implementation with inefficient processing |
| `optimized_code.py`     | Optimized implementation                            |
| `benchmark.py`          | Compares execution times                            |
| `test_functionality.py` | Verifies correctness                                |
| `profile_original.txt`  | cProfile results for original code                  |
| `profile_optimized.txt` | cProfile results for optimized code                 |
| `performance_report.md` | Detailed performance report                         |

### Optimization

The main optimization was replacing repeated nested comparisons with a single sorting operation.

The average calculation was also simplified using Python's built-in `sum()` function.

### Results

* Original average execution time: **1.0883 seconds**
* Optimized average execution time: **0.0097 seconds**
* Performance improvement: **99.11%**
* Speedup: **112.43×**

### Correctness

The optimized implementation was tested using `test_functionality.py`.

The test passed successfully and produced the same student average results as the original implementation.

### How to Run

Run the original version:

```bash
python original_code.py
```

Run the optimized version:

```bash
python optimized_code.py
```

Run the benchmark:

```bash
python benchmark.py
```

Run the functionality test:

```bash
python test_functionality.py
```

Generate profiling data:

```bash
python -m cProfile -s cumulative original_code.py > profile_original.txt
python -m cProfile -s cumulative optimized_code.py > profile_optimized.txt
```

### Conclusion

The optimized implementation significantly reduces execution time while maintaining the required functionality. The benchmark demonstrates a **99.11% performance improvement** and approximately **112.43× speedup**.
