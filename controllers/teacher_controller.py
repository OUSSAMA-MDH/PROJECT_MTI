from models.teacher_model import TeacherModel

class TeacherController:
    def __init__(self):
        self.model = TeacherModel()

    def add_teacher(self, nom, prenom, matiere, classes=None):
        teacher = self.model.add_teacher(nom, prenom, matiere, classes)
        print(f"Enseignant ajouté: {prenom} {nom} | ID: {teacher.teacher_id}")

    def list_teachers(self):
        teachers = self.model.list_teachers()
        for t in teachers:
            print(t)

    def remove_teacher(self, teacher_id):
        teacher = self.model.find_teacher(teacher_id)
        if teacher:
            self.model.remove_teacher(teacher_id)
            print(f"Enseignant supprimé: {teacher.prenom} {teacher.nom}")
        else:
            print("ID introuvable.")
