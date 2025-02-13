# Practical Python Scripts

This repository contains various practical Python scripts for different tasks. Below is a description of each script included in the `practical.py` file.

## Code Descriptions

### Code 1: Find the Maximum Number
This script takes three numbers as input and returns the maximum number among them.
```python
def max_no(a, b, c):
    return max(a, b, c)
```

### Code 2: Multiplication Table
This script prints the multiplication table of a given number.
```python
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
```

### Code 3: Number Triangle
This script prints a triangle of numbers in a sequential manner.
```python
def tri(n):
    count = 1
    for i in range(1, n):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()
```

### Code 4: Inverted Number Triangle
This script prints an inverted triangle of numbers.
```python
def invert(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
```

### Code 5: Right-Angled Star Triangle
This script prints a right-angled triangle of stars.
```python
def tri(n):
    for i in range(1, n):
        for j in range(1, n - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()
```

### Code 6: Inverted Star Triangle
This script prints an inverted triangle of stars.
```python
def tri(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(" ", end=" ")
        for k in range(2 * (n - i) - 1):
            print("*", end=" ")
        print()
```

## How to Run
1. Clone the repository.
2. Navigate to the directory containing the `practical.py` file.
3. Run the script using Python:
   ```bash
   python practical.py
   ```

## Future Updates
More practical Python scripts will be added to this repository in the future. Stay tuned for updates!

## License
This project is licensed under the MIT License.

## Author
S.R
```
Thank You! (Arigato)
Team,
SR
```