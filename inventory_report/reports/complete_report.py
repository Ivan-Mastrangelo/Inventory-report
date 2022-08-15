from inventory_report.reports.simple_report import SimpleReport
from collections import Counter
from collections import OrderedDict


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        relatorio_simplificado = SimpleReport.generate(products)

        nomes_empresas = list()

        for product in products:
            if product["nome_da_empresa"] != "":
                nomes_empresas.append(product["nome_da_empresa"])

        dict_empresas = OrderedDict.fromkeys(nomes_empresas)

        lista_empresas = Counter(nomes_empresas).most_common()

        for a in lista_empresas:
            dict_empresas[a[0]] = a[1]
        print(dict_empresas.items())

        relatorio_complementar = ""

        for a in dict_empresas.items():
            relatorio_complementar += f"- {a[0]}: {a[1]}\n"

        return (
            relatorio_simplificado + "\n"
            + "Produtos estocados por empresa:\n"
            + relatorio_complementar
        )
