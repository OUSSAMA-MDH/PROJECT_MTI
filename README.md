


🌟 Overview

Managing student information efficiently is crucial for specialized institutions like Quranic schools. This system allows administrators and teachers to:

Organize and centralize student and teacher information.

Manage classes and assign teachers.

Track memorized suras for Hafiz students.

Export student and class data in CSV format.

Filter students by level or memorization progress.

✅ Features

Student Management: Add, edit, delete, and view student records.

Teacher Management: Add, edit, delete, and view teacher records.

Class Management: Assign students and teachers to classes.

Tracking Hafiz Progress: Monitor memorized suras for each student.

Data Export: Export student and teacher data to CSV.

Search & Filter: Easily find students or classes based on criteria.

Secure Authentication: Login system for administrators.

🛠 Technologies

Python 3.x – Core programming language

XML – Data storage for students, teachers, and classes

CSV – Data export

MVC Architecture – Clear separation of models, views, and controllers

Design Patterns – Factory Method & Abstract Factory



📂 Project Structure

ECOLE_QURANIYA_COMPLETE/
│
├── controllers/
│   ├── student_controller.py
│   ├── teacher_controller.py
│   └── classe_controller.py
│
├── models/
│   ├── student_factory.py
│   ├── student_model.py
│   ├── teacher_model.py
│   └── classe_model.py
│
├── utils/
│   ├── auth.py
│   ├── csv_export.py
│   └── xml_handler.py
│
├── data/
│   ├── students.xml
│   ├── teachers.xml
│   └── classes.xml
│
└── main.py


⚙ Installation

Clone the repository:

git clone https://github.com/OUSSAMA-MDH/HOME_WORK.git
cd ECOLE_QURANIYA_COMPLETE


Install dependencies (if any):

pip install -r requirements.txt


Run the application:

python main.py

🖥 Usage

Log in as an administrator.

Navigate through the menu to manage students, teachers, and classes.

Track memorized suras for Hafiz students.

Export data to CSV for reporting.



🧩 Design Patterns

Factory Method: Creates student objects based on type (e.g., Hafiz, Regular).

Abstract Factory: Creates families of related objects like Student, Teacher, Class without specifying concrete classes.

Ensures a clean, modular, and maintainable codebase.
