from models.student_model import StudentModel

class StudentController:
    def __init__(self):
        self.model = StudentModel()

    def add_student(self, nom, prenom, niveau, classe, suras=0):
        student_id = self.model.add_student(nom, prenom, niveau, classe, suras)
        print(f"Étudiant ajouté: {prenom} {nom} - {niveau} | ID: {student_id}")

    def remove_student(self, student_id):
        student = self.model.find_student_by_id(student_id)
        if student:
            self.model.remove_student(student_id)
            print(f"Étudiant supprimé: {student.prenom} {student.nom}")
        else:
            print("ID introuvable.")

    def list_students(self):
        students = self.model.get_all_students()
        if not students:
            print("Aucun étudiant trouvé.")
        for s in students:
            print(s)

    def find_student(self, student_id):
        student = self.model.find_student_by_id(student_id)
        if student:
            print(student)
        else:
            print("ID introuvable.")

    def filter_students(self, niveau):
        filtered = self.model.filter_by_niveau(niveau)
        if not filtered:
            print(f"Aucun étudiant trouvé pour le niveau {niveau}.")
        for s in filtered:
            print(s)
