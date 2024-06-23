class Product:

    inventory = []

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_id = len(inventory) + 1
        new_product = Product(cls.product_id, name, category, quantity, price, supplier)
        inventory.append(cls.new_product)
        print("Product added successfully")

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in inventory:
            if product.product_id == product_id:
                if quantity:
                    product.quantity = quantity
                elif price:
                    product.price = price
                elif supplier:
                    product.supplier = supplier
                    print("Product information updated successfully.")
            else:
                print("Product not found.")

    @classmethod
    def delete_product(cls, product_id):
        for product in inventory:
            if product.product_id == product_id:
                inventory.remove(product)
                print("Product deleted successfully.")
            else:
                print("Product not found.")


class Order:

    def __init__(self, order_id, products, customer_info):
        self.order_id = order_id
        self.products = products
        self.customer_info = None

    def place_order(self, product_id, quantity, customer_info=None):
	    products.append((product_id, quantity))
	    print(f"Order placed successfull. Order ID:{self.order_id}")
	