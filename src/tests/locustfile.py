import os
from dotenv import load_dotenv


from locust import HttpUser,SequentialTaskSet,task,between


load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT")

class UseBehaviour(SequentialTaskSet):
    @task
    def simple_test(self):
            self.client.post('https://api.telegram.org/bot{token}/sendMessage'.format(token=TOKEN) ,data={'chat_id': CHAT_ID, 'text': 'test'},verify=False)

class WebsiteUser(HttpUser):
    tasks = [UseBehaviour]
    wait_time = between(1,2)
    host = 'https://locust.io'