from locust import HttpUser, task


class HomePageUser(HttpUser):
    @task
    def home(self):
        self.client.get("/")
