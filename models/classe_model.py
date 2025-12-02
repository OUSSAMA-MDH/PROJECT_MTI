class Classe:
    def __init__(self, classe_id, nom):
        self.classe_id = classe_id
        self.nom = nom
        self.students = []
        self.teachers = []
        self.attendance = {}

    def __str__(self):
        return f"{self.classe_id} | Classe {self.nom} | Étudiants: {len(self.students)} | Enseignants: {len(self.teachers)}"

class ClasseModel:
    def __init__(self):
        self.classes = []
        self.next_id = 1

    def generate_id(self):
        classe_id = f"C{self.next_id:03d}"
        self.next_id += 1
        return classe_id

    def add_classe(self, nom):
        classe_id = self.generate_id()
        cls = Classe(classe_id, nom)
        self.classes.append(cls)
        return cls

    def assign_student(self, classe_id, student_id):
        cls = self.find_classe(classe_id)
        if cls and student_id not in cls.students:
            cls.students.append(student_id)

    def assign_teacher(self, classe_id, teacher_id):
        cls = self.find_classe(classe_id)
        if cls and teacher_id not in cls.teachers:
            cls.teachers.append(teacher_id)

    def record_attendance(self, classe_id, student_id, present=True):
        cls = self.find_classe(classe_id)
        if cls:
            if student_id not in cls.attendance:
                cls.attendance[student_id] = []
            cls.attendance[student_id].append(present)

    def find_classe(self, classe_id):
        for cls in self.classes:
            if cls.classe_id == classe_id:
                return cls
        return None

    def list_classes(self):
        return self.classes
