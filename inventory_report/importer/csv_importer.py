from inventory_report.importer.importer import Importer
from pathlib import Path
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        file_extension = Path(path).suffix
        if file_extension != ".csv":
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf8") as file:
            path_reader = csv.DictReader(file, delimiter=",")
            return list(path_reader)
