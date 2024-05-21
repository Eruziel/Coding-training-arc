from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        try:
            removed = next(filter(lambda p: p.name == product_name, self.products))
            self.products.remove(removed)
        except StopIteration:
            return

    def __repr__(self):
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)





