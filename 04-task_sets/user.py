from locust import HttpUser, constant

from tasks import SequentialOperationTasks, RetrieveTasks

# User --class-picker to select User class on Web UI
class TotalDemoUser(HttpUser):

    wait_time = constant(1)
    tasks = { SequentialOperationTasks: 2, RetrieveTasks: 5 }


class SequentialDemoUser(HttpUser):

    wait_time = constant(1)
    tasks = { SequentialOperationTasks: 2 }


class DemoUser(HttpUser):

    wait_time = constant(1)
    tasks = { RetrieveTasks: 2 }
