from scheduler import RoundRobinScheduler
from utilities import print_colored_header

if __name__ == "__main__":
    quantum_no = int(input("Enter the quantum no = "))
    no_of_processes = int(input("Enter the no of processes = "))
    
    arrival_times = []
    for i in range(no_of_processes):
        arrival_time = int(input(f"Enter the arrival time for process {i+1} = "))
        arrival_times.append(arrival_time)
    
    scheduler = RoundRobinScheduler(quantum_no, no_of_processes, arrival_times)
    scheduler.initialize_processes()
    
    print_colored_header("Round Robin Scheduler", "green")
    scheduler.print_process_summary()
    scheduler.run_scheduler()
