from xml.dom import minidom
from models.student_factory import StudentFactory
import os

class StudentModel:
    def __init__(self, xml_path='data/students.xml'):
        self.xml_path = xml_path
        self.students = self.load_students()
        self.next_id = self.get_next_id()

    def get_next_id(self):
        if not self.students:
            return 1
        ids = [int(s.student_id[1:]) for s in self.students if s.student_id.startswith("S")]
        return max(ids) + 1

    def generate_id(self):
        student_id = f"S{self.next_id:03d}"
        self.next_id += 1
        return student_id

    def load_students(self):
        students = []
        if not os.path.exists(self.xml_path):
            return students
        dom = minidom.parse(self.xml_path)
        student_nodes = dom.getElementsByTagName('student')
        for node in student_nodes:
            student_id = node.getAttribute('id')
            nom = node.getElementsByTagName('nom')[0].firstChild.nodeValue
            prenom = node.getElementsByTagName('prenom')[0].firstChild.nodeValue
            niveau = node.getElementsByTagName('niveau')[0].firstChild.nodeValue
            classe = node.getElementsByTagName('classe')[0].firstChild.nodeValue
            suras_node = node.getElementsByTagName('suras')
            suras = int(suras_node[0].firstChild.nodeValue) if suras_node else 0
            student = StudentFactory.create_student(student_id, nom, prenom, niveau, classe, suras)
            students.append(student)
        return students

    def save_students(self):
        impl = minidom.getDOMImplementation()
        doc = impl.createDocument(None, "students", None)
        root = doc.documentElement
        for s in self.students:
            student_elem = doc.createElement("student")
            student_elem.setAttribute("id", s.student_id)
            for tag, value in [("nom", s.nom), ("prenom", s.prenom), ("niveau", s.niveau),
                               ("classe", s.classe), ("suras", str(s.suras))]:
                elem = doc.createElement(tag)
                elem.appendChild(doc.createTextNode(value))
                student_elem.appendChild(elem)
            root.appendChild(student_elem)
        os.makedirs(os.path.dirname(self.xml_path), exist_ok=True)
        with open(self.xml_path, "w", encoding="utf-8") as f:
            doc.writexml(f, addindent="  ", newl="\n", encoding="utf-8")

    def add_student(self, nom, prenom, niveau, classe, suras=0):
        student_id = self.generate_id()
        student = StudentFactory.create_student(student_id, nom, prenom, niveau, classe, suras)
        self.students.append(student)
        self.save_students()
        return student_id

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        self.save_students()

    def get_all_students(self):
        return self.students

    def find_student_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def filter_by_niveau(self, niveau):
        return [s for s in self.students if s.niveau.lower() == niveau.lower()]
