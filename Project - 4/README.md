<div align="center">

# 📊 Data Analyzer & Transformer Program

### *Interactive Python Console Application for Data Analysis and Transformation*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/Console-CLI-4CAF50?style=for-the-badge)](https://www.python.org/)
[![Data Analysis](https://img.shields.io/badge/Project-Data%20Analyzer-orange?style=for-the-badge)](https://www.python.org/)

<br>

> *"Analyze your data, transform your insights."*

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Features](#-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📚 Functions Explained](#-functions-explained)
- [💻 Sample Outputs](#-sample-outputs)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Learning](#-results--learning)
- [🏆 Advantages](#-advantages)
- [🚀 Future Improvements](#-future-improvements)
- [📄 License](#-license)
- [👤 Author](#-author)

---

# 📌 Overview

The **Data Analyzer & Transformer Program** is a menu-driven Python console application that performs various data analysis and transformation operations on a dataset entered by the user.

The project demonstrates several important Python concepts including:

- Functions
- Recursion
- Lambda Functions
- Built-in Functions
- Lists
- Sorting
- `*args`
- `**kwargs`
- Function Documentation (`__doc__`)
- Statistical Analysis

---

# 🎯 Problem Statement

## Objective

Develop a Python application that allows users to:

- Input numerical data
- Analyze the dataset
- Calculate factorials
- Filter values using Lambda
- Sort data
- Display unique values
- Calculate statistics
- Demonstrate *args and **kwargs
- Display function documentation

---

# ✨ Features

| Feature | Description |
|----------|-------------|
| 📥 Input Data | Accept multiple numbers |
| 📊 Data Summary | Built-in statistics |
| 🔢 Factorial Calculator | Recursive factorial |
| 🔍 Lambda Filter | Filter values above threshold |
| 🔃 Sorting | Ascending & Descending |
| 🎯 Unique Values | Display unique numbers |
| 📈 Dataset Statistics | Min, Max, Average & Total |
| ⭐ *args Demo | Variable arguments |
| ⭐ **kwargs Demo | Keyword arguments |
| 📖 Function Documentation | Display docstrings |
| ❌ Invalid Choice Handling | Error handling |

---

# 🏗️ Project Structure

```text
📦 Data-Analyzer-Transformer
│
├── 📄 index.py
├── 📄 README.md
└── 📂 Screenshots
```

---

# 🔄 Project Workflow

```text
Start
 │
 ▼
Input Dataset
 │
 ▼
Main Menu
 │
 ├── Data Summary
 ├── Factorial
 ├── Lambda Filter
 ├── Sort Data
 ├── Unique Values
 ├── Statistics
 ├── *args
 ├── **kwargs
 ├── Documentation
 └── Exit
```

---

# 📚 Functions Explained

## 📥 Input Data

Stores multiple integers inside a list.

```python
arr = list(map(int, input().split()))
```

---

## 📊 Data Summary

Displays

- Total Elements
- Minimum
- Maximum
- Sum
- Average

---

## 🔢 Factorial

Uses Recursion

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

---

## 🔍 Lambda Filter

Filters values greater than a threshold.

```python
filter(lambda x: x > threshold, arr)
```

---

## 🔃 Sorting

Supports

- Ascending
- Descending

using

```python
sorted()
```

---

## 🎯 Unique Values

Uses

```python
set(arr)
```

to remove duplicate values.

---

## 📈 Dataset Statistics

Calculates

- Minimum
- Maximum
- Total
- Average

---

## ⭐ *args

Displays all values using variable positional arguments.

---

## ⭐ **kwargs

Displays summary using keyword arguments.

---

## 📖 Function Documentation

Uses

```python
function.__doc__
```

to display function descriptions.

---

# 💻 Sample Outputs

### Input Data

```text
Enter data :
2 4 3 5 7 9 2 4 1

Data Stored Successfully
```

---

### Data Summary

```text
Total Elements : 9
Minimum : 1
Maximum : 9
Sum : 37
Average : 4.11
```

---

### Factorial

```text
Enter Number : 5

Factorial = 120
```

---

### Lambda Filter

```text
Threshold : 4

Filtered Data

5
7
9
```

---

### Sorting

```text
Ascending

1 2 2 3 4 4 5 7 9
```

```text
Descending

9 7 5 4 4 3 2 2 1
```

---

### Unique Values

```text
1 2 3 4 5 7 9
```

---

### Statistics

```text
Minimum : 1
Maximum : 9
Total : 37
Average : 4.11
```

---

### Function Documentation

Displays all function docstrings.

---

# 🛠️ Tech Stack

| Tool | Purpose |
|--------|---------|
| 🐍 Python 3.x | Programming Language |
| 📋 List | Store Dataset |
| 🔁 Functions | Modular Programming |
| 🔄 Recursion | Factorial |
| 🔍 Lambda | Filtering |
| ⭐ *args | Variable Arguments |
| ⭐ **kwargs | Keyword Arguments |
| 📖 Docstrings | Documentation |

---

# 📈 Results & Learning

This project demonstrates:

✅ Functions

✅ Recursion

✅ Lambda Functions

✅ Built-in Functions

✅ List Operations

✅ Sorting

✅ Sets

✅ Statistics

✅ *args

✅ **kwargs

✅ Function Documentation

---

# 🏆 Advantages

- Beginner Friendly
- Easy to Understand
- Menu Driven
- No External Libraries
- Reusable Functions
- Practical Data Analysis
- Well Structured Code

---

# 🚀 Future Improvements

- CSV File Support
- Data Visualization
- Graph Generation
- Median & Mode Calculation
- Search Feature
- Export Report
- GUI Version using Tkinter
- NumPy Integration

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👤 Author

<div align="center">

## Ayush Donga

🎓 Student at P P Savani University

🐍 Python Developer | Programming Enthusiast

### 🌐 Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-Ayushd--07-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayushd-07)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ayush%20Donga-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-donga-141aa63b3/)

### 🎥 Project Demo Video

[![Google Drive](https://img.shields.io/badge/Watch%20Demo-Google%20Drive-34A853?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1CuH03wn8AuYTfWj_XM4DTVGomGBRJ2a2?usp=drive_link)

📍 Surat, Gujarat, India

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python

</div>
