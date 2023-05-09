import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from pathlib import Path


def main():
    if (len(sys.argv) != 3):
        sys.stderr.write("Verifique os argumentos\n")
        return

    file_extension_map = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }
    path = sys.argv[1]
    report_type = sys.argv[2]

    file_extension = Path(path).suffix
    read_class = file_extension_map.get(file_extension)
    reporter = InventoryRefactor(read_class)
    final_report = reporter.import_data(path, report_type)

    sys.stdout.write(final_report)
