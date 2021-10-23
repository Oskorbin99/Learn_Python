def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена'], "У вас скидка больше цены товара!"
    return price


if __name__ == '__main__':
    shoes = {'имя': 'Модные туфли', 'цена': 14900}
    print(apply_discount(shoes, 1.25))
