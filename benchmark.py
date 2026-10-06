import subprocess
import re
import statistics


def run_program(filename, runs=5):
    times = []

    for _ in range(runs):
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True
        )

        match = re.search(r"Execution time:\s*([\d.]+)", result.stdout)

        if match:
            times.append(float(match.group(1)))

    return times


def main():
    original_times = run_program("original_code.py")
    optimized_times = run_program("optimized_code.py")

    original_average = statistics.mean(original_times)
    optimized_average = statistics.mean(optimized_times)

    improvement = (
        (original_average - optimized_average)
        / original_average
    ) * 100

    speedup = original_average / optimized_average

    print("Performance Comparison")
    print("======================")
    print()
    print("Original times:", original_times)
    print("Optimized times:", optimized_times)
    print()
    print("Average original time:",
          round(original_average, 4), "seconds")
    print("Average optimized time:",
          round(optimized_average, 4), "seconds")
    print()
    print("Performance improvement:",
          round(improvement, 2), "%")
    print("Speedup:",
          round(speedup, 2), "x")


if __name__ == "__main__":
    main()