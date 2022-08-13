from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):

        nome_da_empresa = list()

        for product in products:
            if product["nome_da_empresa"] != "":
                nome_da_empresa.append(product["nome_da_empresa"])

        empresa = Counter(nome_da_empresa).most_common()[0][0]

        data_fabricacao = cls.data_mais_antiga_de_fabricacao(products)
        data_de_validade_prox = cls.data_mais_próxima_de_validade(products)

        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade_prox}\n"
            f"Empresa com mais produtos: {empresa}"
        )

    @classmethod
    def data_mais_antiga_de_fabricacao(cls, products):
        data_de_fabricacao = set()

        for product in products:
            if product["data_de_fabricacao"] != "":
                data = product["data_de_fabricacao"].split("-")
                data_de_fabricacao.add(
                    date(int(data[0]), int(data[1]), int(data[2]))
                )
        data_fabricacao_mais_antiga = date.today()

        for data_mais_antiga in data_de_fabricacao:
            if data_mais_antiga < data_fabricacao_mais_antiga:
                data_fabricacao_mais_antiga = data_mais_antiga
        return data_fabricacao_mais_antiga

    @classmethod
    def data_mais_próxima_de_validade(cls, products):
        data_de_validade = set()

        for product in products:
            if product["data_de_validade"] != "":
                # data_de_validade.add(product["data_de_validade"])
                data = product["data_de_validade"].split("-")
                data_de_validade.add(
                    date(int(data[0]), int(data[1]), int(data[2]))
                )

        dias_validos = list()
        hoje = date.today()

        for data_validade_proxima in data_de_validade:
            if data_validade_proxima >= hoje:
                dias_validos.append(data_validade_proxima)
        dias_validos_ordenados = sorted(dias_validos)

        return dias_validos_ordenados[0]
