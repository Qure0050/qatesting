from locust import HttpUser, task, between

class SauceDemoLoadUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def load_inventory_page(self):
        self.client.get("/inventory.html", name="01_Load_Inventory")

    @task(1)
    def view_shopping_cart(self):
        self.client.get("/cart.html", name="02_View_Cart")