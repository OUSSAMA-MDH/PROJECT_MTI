from xml.dom import minidom
import os

def load_xml(path):
    if not os.path.exists(path):
        return None
    return minidom.parse(path)

def save_xml(dom, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        dom.writexml(f, addindent="  ", newl="\n", encoding="utf-8")
