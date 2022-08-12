from inventory_report.inventory.product import Product
# from tests.factories.product_factory import ProductFactory


def test_cria_produto():
    # Seu teste deve ser escrito aqui
    product = Product(
        1,
        "prod",
        "empr",
        '10/08/2022',
        '15/8/2022',
        123,
        "guardar na geladeira"
    )

    assert product.id == 1
    assert product.nome_do_produto == "prod"
    assert product.nome_da_empresa == "empr"
    assert product.data_de_fabricacao == '10/08/2022'
    assert product.data_de_validade == '15/8/2022'
    assert product.numero_de_serie == 123
    assert product.instrucoes_de_armazenamento == "guardar na geladeira"
