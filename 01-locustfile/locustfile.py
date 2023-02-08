import json

from faker import Faker
from locust import HttpUser, task, between

class DemoUser(HttpUser):

    faker = Faker()
    wait_time = between(2, 5)

    @task
    def post_test(self):
        request = dict()

        request['name'] = self.faker.company()
        request['slogan'] = self.faker.catch_phrase()
        request['suffix'] = self.faker.company_suffix()
        request['phone_number'] = self.faker.phone_number()

        self.client.post("api/v1/company", data=json.dumps(request))

    @task(3)
    def get_test(self):
        self.client.get("api/v1/company")

    @task(5)
    def get_array_test(self):
        self.client.get("api/v1/company/50")
