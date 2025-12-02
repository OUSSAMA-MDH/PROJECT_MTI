class Teacher:
    def __init__(self, teacher_id, nom, prenom, matiere, classes=None):
        self.teacher_id = teacher_id
        self.nom = nom
        self.prenom = prenom
        self.matiere = matiere
        self.classes = classes if classes else []

    def __str__(self):
        cls = ", ".join(self.classes) if self.classes else "Aucune"
        return f"{self.teacher_id} | {self.prenom} {self.nom} - Matière: {self.matiere} | Classes: {cls}"

class TeacherModel:
    def __init__(self):
        self.teachers = []
        self.next_id = 1

    def generate_id(self):
        teacher_id = f"T{self.next_id:03d}"
        self.next_id += 1
        return teacher_id

    def add_teacher(self, nom, prenom, matiere, classes=None):
        teacher_id = self.generate_id()
        teacher = Teacher(teacher_id, nom, prenom, matiere, classes)
        self.teachers.append(teacher)
        return teacher

    def remove_teacher(self, teacher_id):
        self.teachers = [t for t in self.teachers if t.teacher_id != teacher_id]

    def find_teacher(self, teacher_id):
        for t in self.teachers:
            if t.teacher_id == teacher_id:
                return t
        return None

    def list_teachers(self):
        return self.teachers
