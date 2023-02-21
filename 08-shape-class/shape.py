from locust import LoadTestShape

class CustomShapeClass(LoadTestShape):
    time_limit = 600
    spawn_rate = 20

    def tick(self):
        run_time = self.get_run_time()

        if run_time < self.time_limit:
            # User count rounded to nearest hundred.
            user_count = round(run_time, -2)
            return (user_count, self.spawn_rate)

        return None
        