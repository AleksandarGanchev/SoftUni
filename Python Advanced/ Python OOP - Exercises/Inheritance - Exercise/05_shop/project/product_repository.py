from project import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        # print(f"{x.name}: {x.quantity}" for x in self.products)
        return "\n".join(f"{x.name}: {x.quantity}" for x in self.products)
