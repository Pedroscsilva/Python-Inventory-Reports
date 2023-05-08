import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from pathlib import Path


class Inventory:
    @staticmethod
    def read_csv(path):
        with open(path, encoding="utf8") as file:
            path_reader = csv.DictReader(file, delimiter=",")
            return list(path_reader)

    @staticmethod
    def read_json(path):
        with open(path) as file:
            return json.load(file)

    @staticmethod
    def read_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        data = []
        for record in root.findall("record"):
            record_dict = {}
            for child in record:
                record_dict[child.tag] = child.text
            data.append(record_dict)
        return data

    @staticmethod
    def import_data(path, report_type):
        file_extension_map = {
            ".csv": Inventory.read_csv,
            ".json": Inventory.read_json,
            ".xml": Inventory.read_xml,
        }
        file_extension = Path(path).suffix
        read_fn = file_extension_map.get(file_extension)
        data = read_fn(path)

        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)
