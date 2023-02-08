from requests import JSONDecodeError

from faker import Faker
from locust import HttpUser, task


class ResponseTest(HttpUser):

    faker = Faker()

    @task
    def validate_response(self):

        request = dict()
        request['name'] = self.faker.company()
        request['slogan'] = self.faker.catch_phrase()
        request['suffix'] = self.faker.company_suffix()
        request['phone_number'] = self.faker.phone_number()

        with self.client.post(
            "api/v1/company?testing_failure=true", 
            json=request, 
            name="Testing API Response", 
            catch_response=True
        ) as response:
            try:
                if response.status_code != 201:
                    response.failure("Failed Operational Task... " + response.text)
                elif response.elapsed.total_seconds() > 0.01:
                    response.failure("Too slow service!!!")
                else:
                    response.success()
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")

