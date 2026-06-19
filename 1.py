class Product:
    total_products_count = 0

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        Product.total_products_count += 1

    def display_info(self):
        """Виводить базову інформацію про продукт та загальну кількість."""
        print(f"Назва: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Загалом створено продуктів у системі: {Product.total_products_count}")


class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, warranty_period: int):
        super().__init__(name, price)
        self.warranty_period = warranty_period 

    def display_info(self):
        """Перевизначений метод для виведення інформації про електроніку."""
        print("--- Електроніка ---")
        super().display_info()
        print(f"Гарантійний термін: {self.warranty_period} міс.")
        print("-" * 20)


class ClothingProduct(Product):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size  

    def display_info(self):
        """Перевизначений метод для виведення інформації про одяг."""
        print("--- Одяг ---")
        super().display_info()
        print(f"Розмір: {self.size}")
        print("-" * 20)

if __name__ == "__main__":
    phone = ElectronicProduct("Смартфон", 25000, 24)
    tshirt = ClothingProduct("Футболка", 800, "L")
    laptop = ElectronicProduct("Ноутбук", 42000, 12)

    phone.display_info()
    tshirt.display_info()
    laptop.display_info()
