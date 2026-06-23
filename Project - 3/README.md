<div align="center">

# 🎓 Student Data Organizer

### *Menu-Driven Python Console Application for Managing Student Records*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/CLI-Console-4CAF50?style=for-the-badge)](https://www.python.org/)
[![Data Structures](https://img.shields.io/badge/Data%20Structures-List%20%7C%20Dictionary%20%7C%20Set-orange?style=for-the-badge)](https://www.python.org/)

<br>

> *"Organized data leads to better decisions."*

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [👨‍🎓 Student Management System](#-student-management-system)
- [💾 Data Structures Used](#-data-structures-used)
- [💻 Sample Outputs](#-sample-outputs)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Learning](#-results--learning)
- [🏆 Advantages](#-advantages)
- [🚀 Future Improvements](#-future-improvements)
- [📄 License](#-license)
- [👤 Author](#-author)

---

# 📌 Overview

The **Student Data Organizer** is a menu-driven Python console application designed to manage student records efficiently.

The application allows users to:

- Add Student Records
- Display All Students
- Update Student Information
- Delete Student Records
- Display Subjects Offered
- Exit the System

The project demonstrates practical use of Python data structures such as **Lists, Dictionaries, Tuples, and Sets** while implementing CRUD (Create, Read, Update, Delete) operations.

---

# 🎯 Problem Statement

### Objective

Develop a student management system that:

- Stores student information
- Allows adding new records
- Displays student details
- Updates existing information
- Deletes records
- Maintains a unique list of subjects
- Provides a menu-driven interface

---

# ✨ Key Features

| Feature | Description |
|----------|------------|
| ➕ Add Student | Add new student records |
| 📋 Display Students | Show all stored student records |
| ✏️ Update Student | Modify student information |
| ❌ Delete Student | Remove student records |
| 📚 Subjects Offered | Display all unique subjects |
| 🔄 Menu Driven | Easy navigation |
| 🐍 Pure Python | No external libraries required |

---

# 🏗️ Project Structure

```text
📦 Student-Data-Organizer
│
├── 📄 P-3.py
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
 ┌──────────────┬──────────────┬──────────────┐
 │              │              │              │
 ▼              ▼              ▼              ▼
Add         Display       Update        Delete
Student     Student       Student       Student
 │              │              │              │
 └──────────────┴──────────────┴──────────────┘
                    │
                    ▼
          Display Subjects Offered
                    │
                    ▼
                 Exit
```

---

# 👨‍🎓 Student Management System

## 1️⃣ Add Student

The system collects:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

### Example

```text
Enter Student ID : 1
Enter Name : ayush
Enter Age : 19
Enter Grade : A
Enter Date Of Birth : 2007-05-16
Enter Subjects : python,sql,excel
```

---

## 2️⃣ Display All Students

Displays all stored student records in a formatted manner.

### Example

```text
Student ID : 1
Name : ayush
Age : 19
Grade : A
DOB : 2007-05-16
Subjects : excel, python, sql
```

---

## 3️⃣ Update Student Information

Allows updating:

- Name
- Age
- Subjects

### Example

```text
1. Update Name
2. Update Age
3. Update New Subject
4. Back
```

---

## 4️⃣ Delete Student

Removes a student record using Student ID.

### Example

```text
Enter Delete ID : 2

✅ Delete Record Successfully...
```

---

## 5️⃣ Display Subjects Offered

Displays all unique subjects using a Set.

### Example

```text
Subjects Offered
--------------------
python
sql
excel
c
c++
```

---

# 💾 Data Structures Used

## 📋 List

Stores all student records.

```python
students = []
```

---

## 📖 Dictionary

Stores student information.

```python
student = {
    "ID": id,
    "Name": name,
    "Age": age,
    "Grade": grade
}
```

---

## 📦 Tuple

Stores fixed student details.

```python
info = (id, dob)
```

---

## 🎯 Set

Stores unique subjects.

```python
subjects = set(sub.split(","))
```

---

# 💻 Sample Outputs

## Add Student

```text
✅ Student Added Successfully...
```

---

## Display Student

```text
Student ID : 1 | Name : ayush | Age : 19
```

---

## Display Subjects

```text
Subjects Offered
--------------------
python
sql
excel
c
c++
```

---

## Delete Student

```text
✅ Delete Record Successfully...
```

---

## Invalid Choice

```text
❌ Invalid Choice! Please Try Again.
```

---

## Exit

```text
Thank You for Using Student Data Organizer! 😊
Visit Again. Have a Great Day!
```

---

# 🛠️ Tech Stack

| Tool | Purpose |
|--------|---------|
| 🐍 Python 3.x | Programming Language |
| 📋 List | Store Student Records |
| 📖 Dictionary | Store Student Data |
| 📦 Tuple | Store Fixed Information |
| 🎯 Set | Store Unique Subjects |
| 🔄 While Loop | Menu Control |
| 🎯 Match Case | Decision Making |

---

# 📈 Results & Learning

Through this project, the following concepts were successfully implemented:

✅ Lists

✅ Dictionaries

✅ Tuples

✅ Sets

✅ CRUD Operations

✅ Menu-Driven Programming

✅ Match-Case Statements

✅ User Input Handling

✅ Data Management

---

# 🏆 Advantages

| Advantage | Description |
|------------|-------------|
| 🎓 Beginner Friendly | Easy to understand |
| 📚 Educational | Covers major Python data structures |
| ⚡ Lightweight | No dependencies |
| 🔄 Expandable | Easy to add more features |
| 🖥️ Console Based | Runs on any machine with Python |

---

# 🚀 Future Improvements

- File Handling Support
- CSV Export
- Database Integration
- Search Student Feature
- Sorting Records
- Grade Analysis
- GUI Version using Tkinter
- Student Report Generation

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👤 Author

<div align="center">

## Ayush Donga

🎓 Student at P P Savani University

🐍 Python Developer | Programming Enthusiast

### Connect With Me

GitHub: https://github.com/Ayushd-07

LinkedIn: https://www.linkedin.com/in/ayush-donga-141aa63b3/

📍 Surat, Gujarat, India

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python

</div>
