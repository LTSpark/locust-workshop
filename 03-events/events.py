import json

from faker import Faker
from locust import HttpUser, task, between, events


class RequestUser(HttpUser):

    faker = Faker()
    wait_time = between(2, 5)

    @events.init.add_listener
    def on_init(environment, **kwargs):
        print("Initialazing Locust!!!")

    @events.quit.add_listener
    def on_exit(exit_code, **kwargs):
        print("Stopping Locust process with exit code " + str(exit_code))

    @events.request.add_listener
    def on_request(request_type, name, response_time, response_length, response, context, exception, **kwargs):
        print(f"{request_type} request made to endpoint {name}...")
        print(f"Response Time: {response_time} ms - Response Length: {response_length}")

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("Starting tests...")

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print("Finalized tests...")

    @task
    def post_test(self):
        request = dict()

        request['name'] = self.faker.company()
        request['slogan'] = self.faker.catch_phrase()
        request['suffix'] = self.faker.company_suffix()
        request['phone_number'] = self.faker.phone_number()

        self.client.post("api/v1/company", data=json.dumps(request))

    @task
    def get_test(self):
        self.client.get("api/v1/company")
