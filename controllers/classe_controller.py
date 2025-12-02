from models.classe_model import ClasseModel

class ClasseController:
    def __init__(self):
        self.model = ClasseModel()

    def add_classe(self, nom):
        cls = self.model.add_classe(nom)
        print(f"Classe ajoutée: {cls.nom} | ID: {cls.classe_id}")

    def assign_student(self, classe_id, student_id):
        self.model.assign_student(classe_id, student_id)
        print(f"Étudiant {student_id} assigné à la classe {classe_id}")

    def assign_teacher(self, classe_id, teacher_id):
        self.model.assign_teacher(classe_id, teacher_id)
        print(f"Enseignant {teacher_id} assigné à la classe {classe_id}")

    def record_attendance(self, classe_id, student_id, present=True):
        self.model.record_attendance(classe_id, student_id, present)
        print(f"Présence enregistrée pour {student_id} dans {classe_id}")

    def list_classes(self):
        classes = self.model.list_classes()
        for c in classes:
            print(c)
