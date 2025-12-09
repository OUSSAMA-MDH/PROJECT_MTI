from abc import ABC, abstractmethod

# -------------------
# Adapter pour niveaux
# -------------------
class Student:
    def __init__(self, student_id, nom, prenom, niveau, classe, suras=0):
        self.student_id = student_id
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau
        self.classe = classe
        self.suras = suras

    def __str__(self):
        return f"{self.student_id} | {self.prenom} {self.nom} - {self.niveau}, Classe: {self.classe}"

class PrepaStudent(Student):
    def __init__(self, student_id, nom, prenom, classe):
        super().__init__(student_id, nom, prenom, "Prépa", classe)

class HafizStudent(Student):
    def __init__(self, student_id, nom, prenom, classe, suras):
        super().__init__(student_id, nom, prenom, "Hafiz", classe, suras)

class OnlineStudent(Student):
    def __init__(self, student_id, nom, prenom, classe):
        super().__init__(student_id, nom, prenom, "Online", classe)

class StudentFactory:
    @staticmethod
    def create(student_id, nom, prenom, niveau, classe, suras=0):
        niveau_lower = niveau.lower()
        if niveau_lower == "prépa":
            return PrepaStudent(student_id, nom, prenom, classe)
        elif niveau_lower == "hafiz":
            return HafizStudent(student_id, nom, prenom, classe, suras)
        elif niveau_lower == "online":
            return OnlineStudent(student_id, nom, prenom, classe)
        else:
            return Student(student_id, nom, prenom, niveau, classe, suras)

# -------------------
# Observer pour notifications
# -------------------
class Subject:
    def __init__(self):
        self._observers = set()
        self._state = None

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class StudentObserver(Observer):
    def __init__(self, student):
        self.student = student
        self.last_state = None

    def update(self, state):
        self.last_state = state
        print(f"[Notification] {self.student.prenom} {self.student.nom} a reçu : {state}")

# -------------------
# Strategy pour calculs
# -------------------
class Strategy(ABC):
    @abstractmethod
    def execute(self, student):
        pass

class PromotionStrategy(Strategy):
    def execute(self, student):
        print(f"{student.prenom} {student.nom} est promu au niveau supérieur.")

class RepeatStrategy(Strategy):
    def execute(self, student):
        print(f"{student.prenom} {student.nom} doit répéter l'année.")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, student):
        self._strategy.execute(student)

# -------------------
# Proxy pour accès sécurisé
# -------------------
class RealStudentAccess:
    def get_grades(self, student):
        print(f"Accès aux notes de {student.nom} {student.prenom}: 18/20")

class StudentAccessProxy:
    def __init__(self, real_access, role):
        self._real_access = real_access
        self._role = role

    def get_grades(self, student):
        if self._role in ["admin", "teacher"]:
            self._real_access.get_grades(student)
        else:
            print("Accès refusé: rôle insuffisant")

# -------------------
# Facade pour l'école
# -------------------
class SchoolFacade:
    def __init__(self):
        self.students = []
        self.subject = Subject()

    def add_student(self, student):
        self.students.append(student)
        observer = StudentObserver(student)
        self.subject.attach(observer)
        print(f"Étudiant ajouté: {student}")

    def notify_all(self, message):
        self.subject.set_state(message)
