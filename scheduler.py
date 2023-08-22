import queue
from process import Process

class RoundRobinScheduler:
    def __init__(self, quantum_no, no_of_processes,arrival_times):
        self.quantum_no = quantum_no
        self.no_of_processes = no_of_processes
        self.all_processes = []
        self.ready_queue = queue.Queue()
        self.running_queue = queue.Queue()
        self.flag = [0] * no_of_processes
        self.least_arrival_time = min(arrival_times)
        self.arrival_times = arrival_times  

    def initialize_processes(self):
     for arrival_time in self.arrival_times:
        self.all_processes.append(Process(arrival_time))
        if arrival_time < self.least_arrival_time:
            self.least_arrival_time = arrival_time
        
    def print_process_summary(self):
        for i, process in enumerate(self.all_processes):
            print(f"Process {i+1} :-")
            print(f"Execution time for process {i+1} = {process.execution_time} Quantum no.")
            print(f"Arrival time = {process.arrival_time}")
            task = list(process.tasks_queue.queue)
            print(f"Tasks Elements for operation {i+1} = {task}\n")
    
    def run_scheduler(self):
        counter = 0
        latest_task_que = self.least_arrival_time

        while sum(self.flag) != self.no_of_processes:
            for j in range(self.no_of_processes):
                k = 0
                if j == 0:
                    self.least_arrival_time = self.least_arrival_time + k + j
                else:
                    self.least_arrival_time += 1
                print(f"Time :- {self.least_arrival_time}")
                print("---------------------------")

                if counter == 0:
                    Process_to_be_executed = [index for index, arrival in enumerate(self.arrival_times) if arrival <= self.least_arrival_time]
                    if Process_to_be_executed:
                        for d in Process_to_be_executed:
                            print(f"Process ID: {d + 1}")
                            print("State: Enqueuing in Ready Queue")
                            self.ready_queue.put(d)
                            self.arrival_times[d] = 1000

                if counter == 0 and j == 0:
                    pass
                else:
                    temp = self.running_queue.get()
                    if not self.all_processes[temp].tasks_queue.empty():
                        self.ready_queue.put(temp)
                    else:
                        self.flag[temp] = 1
                if sum(self.flag) == self.no_of_processes:
                    print("All processes are processed")
                    break
                latest_task_que = self.ready_queue.get()

                for k in range(self.quantum_no):
                    if counter == 0 and j == 0:
                        if self.all_processes[j].tasks_queue.empty():
                            break
                        else:
                            if k != 0:
                                self.least_arrival_time = self.least_arrival_time + k
                                print(f"Time :- {self.least_arrival_time}")
                                print("---------------------------")
                            if k == 0:
                                self.running_queue.put(latest_task_que)
                            print(f"State:- Process {latest_task_que + 1} in Running Que  \n")
                            if not self.all_processes[latest_task_que].tasks_queue.empty():
                                if k == 0:
                                    print(f"PC :- {self.all_processes[latest_task_que].tasks_queue.queue[k + 1]} ")
                                else:
                                    print(f"PC :- {self.all_processes[latest_task_que].tasks_queue.queue[0]} ")
                                print(f"Instruction Register :-Task {self.all_processes[latest_task_que].tasks_queue.get()} is executing \n")
                    else:
                        if self.all_processes[latest_task_que].tasks_queue.empty():
                            break
                        else:
                            if k != 0:
                                self.least_arrival_time = self.least_arrival_time + k
                                print(f"Time :- {self.least_arrival_time}")
                                print("---------------------------")
                            if k == 0:
                                self.running_queue.put(latest_task_que)
                            print(f"State:- Process {latest_task_que + 1} in Running Que  ")
                            print(f"Instruction Register :-Task {self.all_processes[latest_task_que].tasks_queue.get()} is executing \n")
                            if not self.ready_queue.empty():
                                if self.all_processes[self.ready_queue.queue[0]].tasks_queue.empty():
                                    pc = self.all_processes[latest_task_que].tasks_queue.queue[0]
                                    print(f"PC :- {pc} \n")
                                else:
                                    print(f"PC :- {self.all_processes[self.ready_queue.queue[0]].tasks_queue.queue[0]} \n")
                            else:
                                if not (self.all_processes[latest_task_que].tasks_queue.empty()):
                                 print(f"PC :- {self.all_processes[latest_task_que].tasks_queue.queue[0]} \n")

            counter += 1
