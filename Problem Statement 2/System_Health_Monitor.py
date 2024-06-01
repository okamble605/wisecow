import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')
CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 80 

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {disk_usage}% used')
    return disk_usage

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    return processes

def main():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    processes = check_running_processes()
    
    logging.info(f'CPU Usage: {cpu_usage}%')
    logging.info(f'Memory Usage: {memory_usage}%')
    logging.info(f'Disk Usage: {disk_usage}%')
    logging.info(f'Running Processes: {len(processes)}')
    
    print('System health check complete. Check system_health.log for details.')

if __name__ == "__main__":
    main()
