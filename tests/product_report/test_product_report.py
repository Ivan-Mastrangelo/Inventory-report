from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # Seu teste deve ser escrito aqui
    product = Product(
        1,
        "prod",
        "empr",
        "10/08/2022",
        "15/08/2022",
        123,
        "guardar na geladeira",
    )
    expected = (
        "O produto prod fabricado em 10/08/2022 "
        "por empr com validade até 15/08/2022 "
        "precisa ser armazenado guardar na geladeira.")

    assert product.__repr__() == expected
