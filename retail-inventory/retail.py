class Product:
    
    inventory = []

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = len(cls.inventory) + 1
        new_product = cls(product_id, name, category, quantity, price, supplier)
        return "Product added successfully."

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully."
        return "Product not found."

    @classmethod
    def delete_product(cls, product_id):
        for i, product in enumerate(cls.inventory):
            if product.product_id == product_id:
                del cls.inventory[i]
                return "Product deleted successfully."    
        return "Product not found."
            

class Order:

    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        for product in Product.inventory:
            if product.product_id == product_id and product.quantity >= quantity:
                product.quantity -= quantity
                self.products.append((product_id, quantity))
                if customer_info:
                    self.customer_info = customer_info
                return f"Order placed successfully. Order ID: {self.order_id}"
        return "Order could not be placed. Product not found or insufficient quantity."


# As an example, your code must be able to create products like this:

p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")

# Update them like this:

update_p1 = Product.update_product(1, quantity=45, price=950)

# Delete them like this:

delete_p1 = Product.delete_product(1)

# And, create and place orders like this:

order = Order(order_id=1, products=[])

order_placement = order.place_order(1, 2, customer_info="John Doe")
