# 📊 NumPy Data Analyzer

<div align="center">

## 🚀 A Powerful Menu-Driven NumPy Toolkit Built with Python

**NumPy Data Analyzer** is a Python command-line application that demonstrates the practical implementation of the **NumPy** library. The project provides an interactive menu-driven interface where users can create arrays, perform mathematical operations, manipulate arrays, search and sort data, and calculate statistical measures.

This project is designed for students and beginners who want hands-on experience with NumPy while understanding how numerical computing works in Python.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Library-blue)
![CLI](https://img.shields.io/badge/Application-Command%20Line-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 📑 Table of Contents

- About Project
- Objectives
- Features
- Main Menu
- Technologies Used
- Project Structure
- Installation
- Running the Project
- Detailed Features
- NumPy Concepts Covered
- NumPy Functions Used
- Learning Outcomes
- Future Improvements
- Requirements
- Contributing
- Author
- Acknowledgements

---

# 📖 About the Project

NumPy is one of the most popular Python libraries used for numerical computing and data analysis. Instead of writing separate programs for every NumPy concept, this project combines many useful operations into a single menu-driven application.

The application enables users to:

- Create one-dimensional arrays
- Create two-dimensional arrays
- Create three-dimensional arrays
- Perform mathematical operations
- Manipulate arrays
- Search data
- Sort data
- Filter values
- Compute statistical information

The project is completely terminal-based and provides an easy-to-understand interface suitable for beginners.

---

# 🎯 Objectives

The main objectives of this project are:

- Learn NumPy practically
- Understand multidimensional arrays
- Practice array manipulation
- Perform numerical computations
- Explore statistical operations
- Improve Python programming skills
- Build a real-world command-line application

---

# ✨ Features

## 📌 Array Creation

Create arrays of different dimensions.

✔ 1D Arrays

✔ 2D Arrays

✔ 3D Arrays

---

## 🔍 Indexing

Access array elements using indexes.

Supports:

- Single Index
- Row Index
- Column Index
- Multi-dimensional Indexing

---

## ✂️ Slicing

Extract portions of arrays.

Supports:

- 1D Array Slicing
- 2D Array Slicing
- 3D Array Slicing

---

## ➕

### Mathematical Operations

Perform element-wise operations between two arrays.

Available operations include:

- Addition
- Subtraction
- Multiplication
- Division

---

## 🔗 Combine Arrays

Combine multiple arrays using NumPy functions.

Useful for joining datasets.

---

## ✂️ Split Arrays

Split arrays into smaller arrays.

Supports:

- Vertical Split
- Horizontal Split

---

## 🔎 Search Operations

Search values inside arrays.

Uses NumPy searching techniques.

---

## 📊 Sort Arrays

Sort arrays efficiently.

Supports row-wise sorting.

---

## 🎯 Filter Values

Filter array values based on conditions.

---

## 📈 Aggregate Functions

Compute:

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Correlation Coefficient

---

# 🖥️ Main Menu

```text
MAIN MENU

1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| NumPy | Numerical Computing |
| OOP | Project Structure |
| CLI | User Interface |

---

# 📂 Project Structure

```text
NumPy-Data-Analyzer/

│
├── main.py
├── main.ipynb
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/NumPy-Data-Analyzer.git
```

Go to the project directory

```bash
cd NumPy-Data-Analyzer
```

Install NumPy

```bash
pip install numpy
```

---

# ▶️ Run the Project

Execute the Python file

```bash
python main.py
```

or

Open the notebook

```bash
jupyter notebook
```

Run

```text
main.ipynb
```

---

# 📚 Detailed Features

## 1️⃣ Create Arrays

Create arrays of different dimensions.

- 1D Array
- 2D Array
- 3D Array

---

## 2️⃣ Mathematical Operations

Perform arithmetic calculations.

- Addition
- Subtraction
- Multiplication
- Division

---

## 3️⃣ Combine or Split Arrays

Array manipulation using NumPy.

- Combine Arrays
- Horizontal Split
- Vertical Split

---

## 4️⃣ Search, Sort & Filter

Search values inside arrays.

Sort arrays.

Filter arrays using conditions.

---

## 5️⃣ Aggregate & Statistics

Calculate:

- Sum
- Average
- Median
- Variance
- Standard Deviation
- Maximum
- Minimum
- Correlation

---

# 📦 NumPy Concepts Covered

This project demonstrates the following NumPy concepts:

- ndarray
- Multi-dimensional Arrays
- Indexing
- Slicing
- Broadcasting
- Element-wise Operations
- Array Manipulation
- Searching
- Sorting
- Filtering
- Aggregation
- Statistical Analysis

---

# 🧮 NumPy Functions Used

### Array Creation

```python
np.array()
reshape()
```

---

### Mathematical Operations

```python
+
-
*
/
```

---

### Combine Arrays

```python
np.concatenate()
```

---

### Split Arrays

```python
np.vsplit()

np.hsplit()

np.split()
```

---

### Search

```python
np.where()
```

---

### Sort

```python
np.sort()
```

---

### Aggregate Functions

```python
np.sum()

np.mean()

np.median()

np.std()

np.var()

np.min()

np.max()

np.corrcoef()
```

---

# 💡 Sample Workflow

```text
Start Program
      │
      ▼
Create NumPy Array
      │
      ▼
Choose Operation
      │
      ├── Indexing
      ├── Slicing
      ├── Mathematics
      ├── Combine Arrays
      ├── Split Arrays
      ├── Search
      ├── Sort
      ├── Filter
      └── Statistics
      │
      ▼
Display Result
```

---

# 🎓 Learning Outcomes

After completing this project you will understand:

- Creating NumPy Arrays
- Multi-dimensional Arrays
- Indexing
- Slicing
- Mathematical Operations
- Combining Arrays
- Splitting Arrays
- Searching Elements
- Sorting Data
- Filtering Data
- Aggregate Functions
- Statistical Analysis
- Menu Driven Applications
- Practical NumPy Programming

---

# 🔮 Future Improvements

Future versions may include:

- Matrix Multiplication
- Matrix Inverse
- Determinant
- Eigen Values
- Eigen Vectors
- CSV File Support
- Excel File Support
- Pandas Integration
- Matplotlib Graphs
- Data Visualization
- Better Exception Handling
- Colored Console Output
- Save Results to Files
- Export Analysis Report

---

# 📋 Requirements

- Python 3.10+
- NumPy

Install dependencies

```bash
pip install numpy
```

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Create a Pull Request.

---

# 👨‍💻 Author

### **Ayush Donga**

🎓 B.Sc. IT Student

💻 Python Developer

🤖 AI & Machine Learning Enthusiast

---

# 🙏 Acknowledgements

Special thanks to:

- Python Documentation
- NumPy Documentation
- Open Source Community
- Python Developers

These resources helped in understanding NumPy concepts and building this project.

---

<div align="center">

## ⭐ If you found this project helpful, please give it a Star!

### Made with ❤️ using Python & NumPy

</div>
