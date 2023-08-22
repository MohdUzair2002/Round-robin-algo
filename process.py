import random
import string
import queue

class Process:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.tasks_queue = queue.Queue()
        self.execution_time = random.randint(1, 10)
        for _ in range(self.execution_time):
            random_uppercase = random.choice(string.ascii_uppercase)
            self.tasks_queue.put(random_uppercase)
