class Product:

    inventory: list[object] = []

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id: int = product_id
        self.name: str = name
        self.category:str = category
        self.quantity:int = quantity
        self.price: float = price
        self.supplier:str = supplier

    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_id = len(inventory) + 1
        new_product = Product(cls.product_id, name, category, quantity, price, supplier)
        inventory.append(cls.new_product)
        print("Product added successfully")

    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        global inventory
        for product in inventory:
            if product.product_id == product_id:
                if quantity:
                    product.quantity = quantity
                elif price:
                    product.price = price
                elif supplier:
                    product.supplier = supplier
                print("Product information update successfully.")
            else:
                print("Product not found.")


    def delete_product(cls, product_id):
        for product in inventory:
            if product.product_id == product_id:
                inventory.del()


class Order:

    def __init__(self, order_id, products, customer_info):
        self.order_id = order_id
        self.products = products
        self.customer_info = None

    def place_order():
