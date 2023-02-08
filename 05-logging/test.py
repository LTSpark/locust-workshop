from faker import Faker
from locust import HttpUser, between, task, events

from logger import Logger


class LoggerTest(HttpUser):

    faker = Faker()
    wait_time = between(1, 5)

    test_logger = Logger("Logging Stress Testing", "test_log")

    @events.init.add_listener
    def init_test(environment, **kwargs):
        Logger.create_log_file("test_log")

    @task(3)
    def get_test(self):
        response = self.client.get("api/v1/company", name="Get Company")
        self.test_logger.info({'response': response.text, 'status_code': response.status_code})

    @task(5)
    def get_array_test(self):
        response = self.client.get(f"api/v1/company/{self.faker.random_int(10, 100)}", name="Get Companies")
        self.test_logger.info({'response': response.text, 'status_code': response.status_code})
    