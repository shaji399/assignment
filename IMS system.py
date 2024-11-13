class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        """Adjusts stock quantity. Pass a positive number to increase, negative to decrease."""
        self.stock_quantity += quantity
        if self.stock_quantity < 0:
            self.stock_quantity = 0  # Prevent negative stock.

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Stock: {self.stock_quantity}"
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """Adds a product to the inventory."""
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """Removes a product from the inventory."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        """Updates a product's details."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        product = self.products[product_id]
        if name: product.name = name
        if category: product.category = category
        if price: product.price = price
        if stock_quantity is not None: product.update_stock(stock_quantity)

    def get_product(self, product_id):
        """Gets a product by ID."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        return self.products[product_id]

    def list_products(self):
        """Lists all products in the inventory."""
        return [str(product) for product in self.products.values()]

    def search_by_name(self, name):
        """Searches products by name."""
        return [str(product) for product in self.products.values() if name.lower() in product.name.lower()]

    def search_by_category(self, category):
        """Searches products by category."""
        return [str(product) for product in self.products.values() if category.lower() in product.category.lower()]

    def filter_by_stock(self, threshold):
        """Filters products that have stock less than the threshold."""
        return [str(product) for product in self.products.values() if product.stock_quantity < threshold]

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Authentication:
    def __init__(self):
        self.users = {
            'admin': User('admin', 'admin123', 'admin'),
            'user1': User('user1', 'user123', 'user')
        }

    def authenticate(self, username, password):
        """Authenticates a user based on username and password."""
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

