


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

Design Patterns – Factory Method & Abstract Factory& Adapter & Observer & Strategy &  Proxy & Facade 



📂 Project Structure

ECOLE_QURANIYA_COMPLETE/
│
├── controllers/                     # Contient les contrôleurs pour gérer les entités
│   ├── student_controller.py        # Gestion des étudiants (CRUD)
│   ├── teacher_controller.py        # Gestion des enseignants
│   └── classe_controller.py         # Gestion des classes
│
├── models/                          # Contient les modèles de données
│   ├── student_model.py             # Modèle étudiant avec lecture/écriture XML
│   ├── student_factory.py           # Factory pour créer différents types d'étudiants (Adapter)
│   ├── teacher_model.py             # Modèle enseignants
│   └── classe_model.py              # Modèle classes
│
├── utils/                           # Contient les utilitaires
│   ├── auth.py                      # Authentification des utilisateurs
│   ├── csv_exporter.py              # Export CSV et JSON
│   └── xml_utils.py                 # Fonctions utilitaires XML
│
├── patterns_school.py               # Contient tous les Patterns:
│                                     # Adapter (StudentFactory)
│                                     # Observer (Subject / StudentObserver)
│                                     # Strategy (Context / PromotionStrategy / RepeatStrategy)
│                                     # Proxy (StudentAccessProxy / RealStudentAccess)
│                                     # Facade (SchoolFacade)
├── main.py                          # CLI principal et tests des Patterns
├── data/                             # Stockage des données
│   ├── students.xml
│   ├── students.csv
│   └── students.json
└── README.md                         # Documentation du projet


⚙ Installation

Clone the repository:

git clone https://github.com/OUSSAMA-MDH/PROJECT_MTI.git
cd ECOLE_QURANIYA_COMPLETE


Install dependencies (if any):

pip install -r requirements.txt


Run the application:

python main.py
