from inventory_report.inventory.product import Product


def test_cria_produto():
    product_id = 1
    product_name = "Mesa"
    company_name = "MesaCorp"
    fabrication_date = "02/05/2023"
    expiry_date = "02/05/2023"
    serial_no = "KZ97"
    conservation_method = "em um local seco"
    test_product = Product(product_id, product_name, company_name,
                           fabrication_date, expiry_date, serial_no,
                           conservation_method)

    assert test_product.id == product_id
    assert test_product.nome_do_produto == product_name
    assert test_product.nome_da_empresa == company_name
    assert test_product.data_de_fabricacao == fabrication_date
    assert test_product.data_de_validade == expiry_date
    assert test_product.numero_de_serie == serial_no
    assert test_product.instrucoes_de_armazenamento == conservation_method
