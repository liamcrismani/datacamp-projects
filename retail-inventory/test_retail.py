# Create products
p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")

# Update products
update_p1 = Product.update_product(1, quantity=45, price=950)

# Delete products
delete_p1 = Product.delete_product(1)

# Create orders
order = Order(order_id=1, products=[])

# Place orders
order_placement = order.place_order(1, 2, customer_info="John Doe")
