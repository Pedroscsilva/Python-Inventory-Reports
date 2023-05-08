from inventory_report.importer.importer import Importer
from pathlib import Path
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        file_extension = Path(path).suffix
        if file_extension != ".xml":
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()
        data = []
        for record in root.findall("record"):
            record_dict = {}
            for child in record:
                record_dict[child.tag] = child.text
            data.append(record_dict)
        return data
