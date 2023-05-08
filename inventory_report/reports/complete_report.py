from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)

        counts = Counter(p["nome_da_empresa"] for p in list)
        most_common_companies = counts.most_common()

        company_products = "\nProdutos estocados por empresa:\n"
        for company, qty in most_common_companies:
            company_products += f"- {company}: {qty}\n"

        return (
            f"{simple_report}{company_products}"
        )
