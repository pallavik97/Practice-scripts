import platform
import psutil  # Install with: pip install psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

def check_disk_usage():
    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Disk Usage ({partition.device}): {usage.percent}%")

def check_processes():
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    for process in processes:
        print(f"Process: {process.info}")

def main():
    try:
        print("Checking System Metrics:")
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_processes()

    except Exception as e:
        print(f"Error: {e}")
        # You can raise an exception or log the error, depending on your needs.

if __name__ == "__main__":
    main()
