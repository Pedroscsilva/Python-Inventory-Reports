from inventory_report.inventory.product import Product


def test_relatorio_produto():
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
    expected_string = "O produto Mesa fabricado em 02/05/2023 por MesaCorp " \
                      "com validade até 02/05/2023 precisa ser armazenado " \
                      "em um local seco."
    assert str(test_product.__repr__()) == expected_string
