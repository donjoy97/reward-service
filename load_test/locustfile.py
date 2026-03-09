from locust import HttpUser,task

class RewardUser(HttpUser):

    @task
    def reward(self):

        self.client.post("/reward/decide",json={
        "txn_id":"txn123",
        "user_id":"user1",
        "merchant_id":"m1",
        "amount":100,
        "txn_type":"PAYMENT",
        "ts":123456
        })