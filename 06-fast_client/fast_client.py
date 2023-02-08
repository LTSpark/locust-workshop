from faker import Faker
from locust import FastHttpUser, task, between

class DemoUser(FastHttpUser):

    faker = Faker()
    wait_time = between(2, 5)

    @task(2)
    def post_test(self):
        request = dict()

        request['name'] = self.faker.company()
        request['slogan'] = self.faker.catch_phrase()
        request['suffix'] = self.faker.company_suffix()
        request['phone_number'] = self.faker.phone_number()

        self.client.post("api/v1/company", json=request, name='Post Company')

    @task(5)
    def get_test(self):
        self.client.get("api/v1/company", name='Get Company')

    @task(3)
    def get_array_test(self):
        self.client.get(f"api/v1/company/{self.faker.random_int(10, 100)}", name='Get Companies')
