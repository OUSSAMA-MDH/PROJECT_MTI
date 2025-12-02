from controllers.student_controller import StudentController
from utils.auth import login
from utils.csv_exporter import export_students_csv, export_students_json

def main():
    username = input("Nom d'utilisateur: ")
    password = input("Mot de passe: ")
    role = login(username, password)
    if not role:
        print("Échec de l'authentification.")
        return

    student_ctrl = StudentController()

    while True:
        print("\n=== École Coranique CLI ===")
        print("1. Gestion des étudiants")
        print("2. Export CSV/JSON")
        print("0. Quitter")
        choice = input("Choisissez une option: ")

        if choice == "1":
            sub = input("a: Liste, b: Ajouter, c: Supprimer, d: Chercher, e: Filtrer: ")
            if sub == "a":
                student_ctrl.list_students()
            elif sub == "b":
                nom = input("Nom: ")
                prenom = input("Prénom: ")
                niveau = input("Niveau: ")
                classe = input("Classe: ")
                suras = int(input("Suras mémorisées: "))
                student_ctrl.add_student(nom, prenom, niveau, classe, suras)
            elif sub == "c":
                sid = input("ID étudiant: ")
                student_ctrl.remove_student(sid)
            elif sub == "d":
                sid = input("ID étudiant: ")
                student_ctrl.find_student(sid)
            elif sub == "e":
                niveau = input("Niveau: ")
                student_ctrl.filter_students(niveau)
            else:
                print("Option invalide")
        elif choice == "2":
            students = student_ctrl.model.get_all_students()
            export_students_csv(students)
            export_students_json(students)
            print("Export terminé.")
        elif choice == "0":
            print("Au revoir 👋")
            break
        else:
            print("Option invalide")

if __name__ == "__main__":
    main()
