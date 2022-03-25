from locust import HttpUser, task, SequentialTaskSet, between

class RootTask(SequentialTaskSet):
    @task
    def get_root(self):
        self.client.get("/")

class UsersTask(SequentialTaskSet):
    @task
    def get_users(self):
        self.client.get("/users")

class ScoreboardTask(SequentialTaskSet):
    @task
    def get_scoreboard(self):
        self.client.get("/scoreboard")
        self.client.get("https://securi.day/api/v1/scoreboard/top/10")

class ChallengesTask(SequentialTaskSet):
    @task
    def get_challenges(self):
        self.client.get("/challenges")
        self.client.get("/https://securi.day/api/v1/challenges")

class LoginTask(SequentialTaskSet):
    @task
    def login(self):
        self.client.get("/login")
        self.client.post(url = 'https://fierce-garden-25525.herokuapp.com/login?next=/challenges?',
                    json = {"name" : "test", "password": "test", "_submit": "Submit", "nonce": "9272af98535de548a708f87730ec95519fa4bf5152ef5334b770f5cbdcb7437c"}    )

class CTFdUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [RootTask, UsersTask, ScoreboardTask, ChallengesTask, LoginTask]
    