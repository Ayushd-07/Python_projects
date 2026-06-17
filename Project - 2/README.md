<div align="center">

# 🔺 Pattern Generator & Number Analyzer

### *Interactive Python Console Application for Pattern Printing and Number Analysis*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/CLI-Console-4CAF50?style=for-the-badge)](https://www.python.org/)
[![Loops](https://img.shields.io/badge/Concept-Loops-orange?style=for-the-badge)](https://www.python.org/)

<br>

> *"Master loops and conditions, and you unlock the power to build logic."*

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🔺 Pattern Generation Module](#-pattern-generation-module)
- [🔢 Number Analysis Module](#-number-analysis-module)
- [💻 Sample Outputs](#-sample-outputs)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Learning](#-results--learning)
- [🏆 Advantages](#-advantages)
- [🚀 Future Improvements](#-future-improvements)
- [📄 License](#-license)
- [👤 Author](#-author)

---

# 📌 Overview

The **Pattern Generator & Number Analyzer** is a menu-driven Python console application that combines two important beginner programming concepts:

1. Pattern Printing using Nested Loops
2. Number Analysis using Conditional Statements

The application allows users to generate star patterns and analyze a range of numbers to determine whether they are even or odd while also calculating their total sum.

---

# 🎯 Problem Statement

### Objective

Build an interactive console-based application that:

- Generates star patterns using nested loops
- Analyzes a range of numbers
- Identifies even and odd numbers
- Calculates the sum of all numbers within a range
- Uses menu-driven programming
- Handles invalid user choices gracefully

---

# ✨ Key Features

| Feature | Description |
|----------|------------|
| 🔺 Right Triangle Pattern | Generates right-aligned triangle |
| 🔻 Left Triangle Pattern | Generates left-aligned triangle |
| 🔢 Number Analysis | Determines even and odd numbers |
| ➕ Sum Calculation | Calculates total of a number range |
| 🔄 Menu Driven Interface | Interactive user experience |
| ❌ Invalid Choice Handling | Displays error messages |
| 🐍 Pure Python | No external libraries required |

---

# 🏗️ Project Structure

```text
📦 Pattern-Generator-And-Number-Analyzer
│
├── 📄 P-2.py
│
├── 📄 README.md
│
└── 📂 Screenshots
```

---

# 🔄 Project Workflow

```text
Start Program
      │
      ▼
Display Main Menu
      │
      ▼
 ┌───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
Pattern      Analysis         Exit
Generator    Module
 │               │
 ▼               ▼
Select       Enter Start
Pattern      & End Number
 │               │
 ▼               ▼
Print       Even/Odd Check
Pattern     + Sum Calculation
 │               │
 └───────┬───────┘
         ▼
     Show Result
         │
         ▼
     Return Menu
```

---

# 🔺 Pattern Generation Module

The Pattern Generator allows users to create different star-based patterns using nested loops.

## 1️⃣ Right Side Triangle

### Logic

```python
for i in range(1,n+1):
    for _ in range(n-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()
```

### Output

```text
      *
    * *
  * * *
* * * *
```

---

## 2️⃣ Left Side Triangle

### Logic

```python
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
```

### Output

```text
*
* *
* * *
* * * *
```

---

# 🔢 Number Analysis Module

The Number Analysis feature:

- Identifies Even Numbers
- Identifies Odd Numbers
- Calculates Total Sum

### Logic

```python
for i in range(start,end+1):

    if i % 2 == 0:
        print(f"{i} is Even Number.")
    else:
        print(f"{i} is Odd Number.")

    total += i
```

### Example Output

```text
7 is Odd Number.
8 is Even Number.
9 is Odd Number.
10 is Even Number.
11 is Odd Number.
12 is Even Number.

Sum of all numbers : 57
```

---

# 💻 Sample Outputs

## Main Menu

```text
1. Pattern generate
2. Number analysis
3. Exit
```

### Pattern Generation

```text
Enter triangle shape : 1
Enter number of rows : 4

      *
    * *
  * * *
* * * *
```

### Number Analysis

```text
Enter start number : 7
Enter end number : 12

7 is Odd Number.
8 is Even Number.
9 is Odd Number.
10 is Even Number.
11 is Odd Number.
12 is Even Number.

Sum of all numbers : 57
```

### Invalid Choice

```text
❌ Invalid choice! Please try again.
```

---

# 🛠️ Tech Stack

| Tool | Purpose |
|--------|---------|
| 🐍 Python 3.x | Programming Language |
| 🔄 While Loop | Menu Control |
| 🔁 For Loop | Pattern & Analysis Logic |
| 🎯 Match Case | Menu Navigation |
| 📥 Input Function | User Input |
| 🖨️ Print Function | Output Display |

---

# 📈 Results & Learning

Through this project, the following concepts were successfully implemented:

✅ Nested Loops

✅ Conditional Statements

✅ Match-Case Statements

✅ Range Functions

✅ Menu-Driven Programming

✅ Pattern Printing

✅ Number Analysis

✅ User Interaction

---

# 🏆 Advantages

| Advantage | Description |
|------------|-------------|
| 🎓 Beginner Friendly | Easy to understand |
| 📚 Educational | Covers multiple Python concepts |
| ⚡ Lightweight | Runs instantly |
| 🔄 Reusable Logic | Easy to expand |
| 🖥️ Cross Platform | Works on all systems with Python |

---

# 🚀 Future Improvements

- Add Pyramid Pattern
- Add Diamond Pattern
- Add Prime Number Checker
- Add Armstrong Number Checker
- Add Number Statistics
- Add Pattern Preview Menu
- Add Input Validation

---

# 📄 License

This project is licensed under the **MIT License**.

```text
MIT License

Free to use, modify, and distribute with attribution.
```

---

# 👤 Author

<div align="center">

## Ayush Donga

🎓 Student at P P Savani University

🐍 Python Developer | Programming Enthusiast

### Connect With Me

**GitHub**  
https://github.com/Ayushd-07

**LinkedIn**  
https://www.linkedin.com/in/ayush-donga-141aa63b3/

📍 Surat, Gujarat, India

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python

</div>
