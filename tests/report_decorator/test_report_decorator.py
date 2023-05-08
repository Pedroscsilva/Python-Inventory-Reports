from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


def test_decorar_relatorio():
    colored_report_class = ColoredReport(SimpleReport)
    p_list = CsvImporter.import_data("inventory_report/data/inventory.csv")
    colored_report = colored_report_class.generate(p_list)
    expect = ("\033[32mData de fabricação mais antiga:\033[0m "
              "\033[36m2020-09-06\033[0m\n"
              "\033[32mData de validade mais próxima:\033[0m "
              "\033[36m2023-09-17\033[0m\n"
              "\033[32mEmpresa com mais produtos:\033[0m "
              "\033[31mTarget Corporation\033[0m")
    assert expect == colored_report
