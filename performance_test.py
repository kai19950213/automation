from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3) # 模擬使用者間的等待時間，單位為秒

    @task
    def my_task(self):
        self.client.get("https://wwSgoogle.com/") ## 傳送HTTP請求