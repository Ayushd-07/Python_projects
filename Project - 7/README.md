# 🧰 Multi-Utility Toolkit

<div align="center">

### A Powerful Menu-Driven Python Utility Application

A beginner-friendly Python project that combines multiple useful operations such as **Date & Time Operations, Mathematical Calculations, Random Data Generation, UUID Generation, File Handling, and Module Exploration** into one command-line application.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Multi--Utility%20Toolkit-success)
![Type](https://img.shields.io/badge/Type-CLI%20Application-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner%20Friendly-purple)

</div>

---

## 📖 About the Project

The **Multi-Utility Toolkit** is a menu-driven command-line application developed using Python.

The main purpose of this project is to combine different Python concepts and built-in modules into a single application. Instead of creating separate programs for every operation, this toolkit provides a centralized menu where users can select the utility they want to use.

The application includes multiple categories such as:

- 🕒 Datetime and Time Operations
- 🧮 Mathematical Operations
- 🎲 Random Data Generation
- 🆔 UUID Generation
- 📁 File Operations
- 🔍 Module Attribute Exploration

This project is useful for understanding how different Python modules, functions, loops, conditions, custom modules, and file operations can work together in a complete application.

---

# ✨ Features

## 🕒 1. Datetime and Time Operations

The Datetime section provides multiple utilities related to dates and time.

### Available Operations

#### 📅 Display Current Date & Time

Displays the current system date and time using Python's `datetime` module.

Example:

```text
Current Date & Time : 2026-07-22 15:34:54.089667
```

---

#### 📆 Calculate Difference Between Two Dates

The user can enter two dates in the following format:

```text
YYYY-MM-DD
```

The program calculates the difference between the two dates in days.

Example:

```text
Enter the first date (YYYY-MM-DD) : 2026-07-01
Enter the second date (YYYY-MM-DD) : 2026-07-22

Difference : 21
```

---

#### 🗓️ Format a Date

The program converts a date from:

```text
YYYY-MM-DD
```

into:

```text
DD/MM/YYYY
```

Example:

```text
Enter the date (YYYY-MM-DD) : 2026-07-22

Formatted date : 22/07/2026
```

---

#### ⏱️ Stopwatch

The stopwatch allows the user to:

1. Press Enter to start
2. Wait for any amount of time
3. Press Enter again to stop

The program then calculates the total elapsed time.

Example:

```text
Press Enter to start stopwatch:

Stopwatch running... Press Enter to stop:

Total time : 5.42 seconds
```

---

#### ⏳ Countdown Timer

The user enters the number of seconds, and the program starts counting down until it reaches zero.

Example:

```text
Enter second : 5

5
4
3
2
1

Time's up!
```

---

# 🧮 2. Mathematical Operations

The Mathematical Operations section provides multiple useful calculations using Python's built-in `math` module.

## Available Operations

### 🔢 Calculate Factorial

The program calculates the factorial of a given number.

Example:

```text
Enter a number : 6

Factorial of 6 is 720
```

---

### 💰 Compound Interest Calculation

The user enters:

- Principal amount
- Rate of interest
- Time in years

The application then calculates the compounded amount.

Example:

```text
Enter principal amount : 5000
Enter rate of interest (%) : 7
Enter time (in year) : 3

Compound Interest : 6125.22
```

---

### 📐 Trigonometric Calculations

The application supports three trigonometric calculations:

```text
1. Sin
2. Cos
3. Tan
```

The user enters an angle in degrees, and the program converts it into radians before performing the selected calculation.

Example:

```text
Enter angle in degrees: 45

1. Sin
2. Cos
3. Tan

Enter your choice: 1

Sin = 0.7071067811865475
```

---

### 📏 Area of Geometric Shapes

The program can calculate the area of different geometric shapes.

Supported shapes:

```text
1. Circle
2. Rectangle
3. Square
```

#### Circle

```text
Area = 3.14 × radius × radius
```

#### Rectangle

```text
Area = length × width
```

#### Square

```text
Area = side × side
```

---

# 🎲 3. Random Data Generation

The Random Data Generation section uses Python's built-in `random` module.

It provides several useful random data generation utilities.

## Available Operations

### 🎯 Generate Random Number

The user enters a starting and ending number.

The program generates a random number within that range.

Example:

```text
Enter starting number: 1
Enter ending number: 10

Random Number : 8
```

---

### 📋 Generate Random List

The program generates a list containing random numbers.

Example output:

```text
Random List = [42, 17, 83, 5, 61]
```

---

### 🔐 Create Random Password

The user enters the required password length.

The application generates a password containing:

- Uppercase letters
- Lowercase letters
- Numbers

Example:

```text
Enter password length : 7

Password : 1Imtgm8
```

> **Note:** This password generator is created for learning purposes. For security-sensitive applications, Python's `secrets` module is generally preferred.

---

### 🔢 Generate Random OTP

The program generates a random 6-digit OTP.

Example:

```text
OTP = 379693
```

---

# 🆔 4. UUID Generator

The application can generate a Universally Unique Identifier using Python's built-in `uuid` module.

The program uses:

```python
uuid.uuid4()
```

Example output:

```text
Generate Unique Identifiers :

UUID : cd62eea3-2340-4120-9e53-57719bbb1354
```

Every generated UUID is designed to be unique.

---

# 📁 5. File Operations

The project includes a separate custom module for performing file operations.

The file operation functionality is organized inside:

```text
utilities/file_operations.py
```

This helps demonstrate how custom Python modules can be created and imported into another Python file.

## Available File Operations

### 📄 Create a New File

Creates a new file using the filename entered by the user.

Example:

```text
Enter file name : data.txt

✅ File created successfully!
```

---

### ✍️ Write Data to a File

The user enters:

1. File name
2. Data to write

The program writes the provided data into the file.

Example:

```text
Enter file name : data.txt

Enter data to write : Hello! Python World

✅ Data written successfully!
```

---

### 📖 Read Data From a File

The application opens and displays the content of a selected file.

Example:

```text
Enter file name : data.txt

File content :

Hello! Python World

✅ File read successfully!
```

If the file does not exist, the application handles the error using:

```python
except FileNotFoundError:
```

Example:

```text
❌ File not found
```

---

### ➕ Append Data to a File

The append operation adds new content to an existing file without deleting the previous content.

The file is opened using:

```python
open(file_name, "a")
```

---

# 🔍 6. Explore Module Attributes

One of the interesting features of this project is the **Module Attribute Explorer**.

It uses Python's built-in:

```python
dir()
```

function.

The user can explore the available attributes, classes, functions, and methods of different modules.

## Supported Modules

```text
math
datetime
random
uuid
file_op
```

Example:

```text
Available Modules:

math | datetime | random | uuid | file_op

Enter module name : random
```

The program then displays all available attributes of the selected module.

This feature is useful for learning and exploring Python modules.

---

# 📋 Main Menu

When the application starts, the following main menu is displayed:

```text
+------------------------------------------------+
|                  MAIN MENU                     |
+------------------------------------------------+
|  1. Datetime and Time Operations               |
|  2. Mathematical Operations                    |
|  3. Random Data Generation                     |
|  4. Generate Unique Identifiers (UUID)         |
|  5. File Operations (Custom Module)            |
|  6. Explore Module Attributes (dir())          |
|  7. Exit                                       |
+------------------------------------------------+
```

The user enters a number from `1` to `7` to select an operation.

---

# ❌ Invalid Choice Handling

The application also handles invalid menu choices.

For example:

```text
Enter your choice : 9

❌ Invalid choice! Please choose from 1 to 7.
```

The program then displays the menu again instead of immediately terminating.

---

# 📂 Project Structure

The recommended project structure is:

```text
Project-7/
│
├── main.py
├── data.txt
│
└── utilities/
    │
    ├── __init__.py
    └── file_operations.py
```

### File Description

| File | Description |
|------|-------------|
| `main.py` | Main program containing all menus and utility operations |
| `file_operations.py` | Custom module containing file handling functions |
| `__init__.py` | Makes the `utilities` folder a Python package |
| `data.txt` | Example text file used for file operations |

---

# 📦 Python Modules Used

The project uses the following Python modules:

```python
import datetime as dt
import time
import math
import random
import uuid
from utilities import file_operations as fo
```

## Module Purposes

| Module | Purpose |
|--------|---------|
| `datetime` | Date and time operations |
| `time` | Stopwatch and countdown timer |
| `math` | Mathematical calculations |
| `random` | Random numbers, passwords, lists, and OTPs |
| `uuid` | Generate unique identifiers |
| `file_operations` | Custom file handling operations |

---

# 🧠 Python Concepts Used

This project demonstrates several important Python concepts.

### Core Python

- Variables
- User input
- Data types
- Type conversion
- Operators
- Conditional statements
- Nested conditions
- Loops
- Nested loops

### Advanced Beginner Concepts

- `match-case`
- Functions
- Built-in modules
- Custom modules
- Packages
- Import statements
- Exception handling
- File handling
- String operations
- Lists
- Random data generation
- Date formatting
- Module exploration

---

# ⚙️ Requirements

Before running the project, make sure Python is installed on your computer.

Recommended version:

```text
Python 3.10 or later
```

Python 3.10+ is recommended because the project uses the `match-case` statement.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external Python packages are required because the project uses Python's standard library.

---

# 🚀 Installation & Setup

## Step 1: Download the Project

Download or clone the project files to your computer.

---

## Step 2: Open the Project Folder

Open the project folder using:

- Visual Studio Code
- PyCharm
- Any Python-supported code editor

---

## Step 3: Check the Folder Structure

Make sure the custom module is inside the `utilities` folder.

```text
Project-7/
├── main.py
└── utilities/
    ├── __init__.py
    └── file_operations.py
```

---

## Step 4: Open Terminal

Open the terminal inside the project directory.

---

## Step 5: Run the Program

Run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

---

# 🔄 Application Workflow

```text
Start Program
      │
      ▼
Display Main Menu
      │
      ▼
User Selects an Option
      │
      ├── 1 → Datetime Operations
      │
      ├── 2 → Mathematical Operations
      │
      ├── 3 → Random Data Generation
      │
      ├── 4 → Generate UUID
      │
      ├── 5 → File Operations
      │
      ├── 6 → Explore Module Attributes
      │
      └── 7 → Exit Program
```

Most sections contain their own submenus that allow users to perform multiple operations and return to the main menu.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Practice Python's built-in modules
2. Understand menu-driven program development
3. Learn how to create custom Python modules
4. Practice importing modules and functions
5. Understand basic file handling
6. Learn exception handling
7. Practice loops and conditional statements
8. Understand `match-case`
9. Generate random data using Python
10. Work with date and time values
11. Explore Python modules using `dir()`
12. Combine multiple concepts into one complete application

---

# 📚 Learning Outcomes

After completing this project, you can better understand:

- How to structure a larger beginner-level Python project
- How to organize different features using menus
- How to use Python's standard library
- How to create reusable functions
- How to separate functionality into custom modules
- How to work with files
- How to handle missing files using exceptions
- How to generate random values
- How to generate UUIDs
- How to work with dates and time
- How to create interactive CLI applications

---

# 🔮 Future Improvements

The project can be improved further by adding:

- Better input validation using `try-except`
- Calculator operations
- Temperature converter
- Currency converter
- Unit converter
- Age calculator
- Strong password generator
- Password strength checker
- Multiple file format support
- File deletion and renaming
- JSON data storage
- Logging system
- Colored terminal output
- User authentication
- Graphical User Interface using Tkinter
- Database integration using SQLite
- Object-Oriented Programming structure

---

# 👨‍💻 Author

## **Ayush Donga**

🎓 Student at **P P Savani University**  
🐍 Python Developer  
🤖 Learning **AI, Machine Learning & Automation**  
💻 Interested in Software Development and AI Projects  
📍 Surat, Gujarat, India

### 🎥 Project Demo Video

▶️ [**Watch the Multi-Utility Toolkit Project Demo Video**](https://drive.google.com/file/d/1wOnYc54Oue9cmXYhEoJw0YjQniBEKrWg/view?usp=drive_link)

---

# 🙏 Thank You

Thank you for checking out the **Multi-Utility Toolkit** project!

If you found this project useful for learning Python, feel free to explore the code, modify the features, and add your own utilities.

<div align="center">

### ⭐ If you like this project, consider giving the repository a star!

### 🐍 Keep Learning • Keep Coding • Keep Building

**Made with ❤️ using Python**

</div>
