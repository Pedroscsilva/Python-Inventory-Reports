from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        all_fab_dates = [p["data_de_fabricacao"] for p in list]
        old_date = min(all_fab_dates)

        all_val_dates = [datetime.strptime(p["data_de_validade"], "%Y-%m-%d")
                         for p in list]
        now = datetime.now()
        future_date = min(dt for dt in all_val_dates if dt > now).date()
        counts = Counter(p["nome_da_empresa"] for p in list)
        most_common = counts.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {future_date}\n"
            f"Empresa com mais produtos: {most_common}"
        )
