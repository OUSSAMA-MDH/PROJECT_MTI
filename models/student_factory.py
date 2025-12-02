class Student:
    def __init__(self, student_id, nom, prenom, niveau, classe, suras=0, email=""):
        self.student_id = student_id
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau
        self.classe = classe
        self.suras = suras
        self.email = email

    def __str__(self):
        return f"{self.student_id} | {self.prenom} {self.nom} - {self.niveau}, Classe: {self.classe}, Suras: {self.suras}"


class StudentFactory:
    @staticmethod
    def create_student(student_id, nom, prenom, niveau, classe, suras=0, email=""):
        niveau_lower = niveau.lower()
        if niveau_lower == "prépa":
            return PrepaStudent(student_id, nom, prenom, classe)
        elif niveau_lower == "hafiz":
            return HafizStudent(student_id, nom, prenom, classe, suras)
        elif niveau_lower == "online":
            return OnlineStudent(student_id, nom, prenom, classe)
        else:
            return Student(student_id, nom, prenom, niveau, classe, suras, email)


class PrepaStudent(Student):
    def __init__(self, student_id, nom, prenom, classe):
        super().__init__(student_id, nom, prenom, "Prépa", classe)


class HafizStudent(Student):
    def __init__(self, student_id, nom, prenom, classe, suras):
        super().__init__(student_id, nom, prenom, "Hafiz", classe, suras)


class OnlineStudent(Student):
    def __init__(self, student_id, nom, prenom, classe):
        super().__init__(student_id, nom, prenom, "Online", classe)
