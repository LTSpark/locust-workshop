import json
import uuid

from faker import Faker
from locust import SequentialTaskSet, TaskSet, task


class SequentialOperationTasks(SequentialTaskSet):

    faker = Faker()

    @task
    def post_company(self):
        request = dict()

        request['name'] = self.faker.company()
        request['slogan'] = self.faker.catch_phrase()
        request['suffix'] = self.faker.company_suffix()
        request['phone_number'] = self.faker.phone_number()

        self.client.post("api/v1/company", data=json.dumps(request), name="Get Company")
    
    @task
    def put_company(self):
        self.client.put(f"api/v1/company/{str(uuid.uuid4())}", name="Update Company")
    
    @task
    def delete_company(self):
        self.client.delete(f"api/v1/company/{str(uuid.uuid4())}", name="Delete Company")


class RetrieveTasks(TaskSet):

    faker = Faker()

    @task(3)
    def get_test(self):
        self.client.get("api/v1/company", name="Get Company")

    @task(5)
    def get_array_test(self):
        self.client.get(f"api/v1/company/{self.faker.random_int(10, 100)}", name="Get Companies")
