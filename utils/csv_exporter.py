import csv
import json

def export_students_csv(students, filepath='data/students.csv'):
    with open(filepath, 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Nom","Prenom","Niveau","Classe","Suras"])
        for s in students:
            writer.writerow([s.student_id, s.nom, s.prenom, s.niveau, s.classe, s.suras])

def export_students_json(students, filepath='data/students.json'):
    data = []
    for s in students:
        data.append({
            "id": s.student_id,
            "nom": s.nom,
            "prenom": s.prenom,
            "niveau": s.niveau,
            "classe": s.classe,
            "suras": s.suras
        })
    with open(filepath, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
