import psutil
DRIVE_PATHS = ["C:\\", "D:\\", "F:\\", "G:\\"]
def collect() -> dict:
    end_dict = {}
    #General CPU parameters (Utilization etc.)
    cpu_usage = psutil.cpu_percent(interval = 1) #CPU utilization in Float
    end_dict.update({"cpu_usage": cpu_usage})
    try:
        cpu_frequency = psutil.cpu_freq() #Current, Min and Max frequencie of CPU
        end_dict.update({"cpu_frequency_current": cpu_frequency.current})
    except AttributeError:
        end_dict.update({"cpu_frequency_current": None})

    #General Memory related parameters 

    total_memory = psutil.virtual_memory() #Total, available and percent of memory in the system (RAM)
    end_dict.update({"memory_used_percent": total_memory.percent})

    #General drives related parameters
    for drive in DRIVE_PATHS:
        key = f"drive_{drive[0]}_usage_percent"
        try:
            end_dict.update({key: psutil.disk_usage(drive).percent})
        except OSError: #In case the drive with this mountin point is not accessible
            end_dict.update({key: None})
            print(f"Skipping {drive[0]}: not readable")



    
    return end_dict
if __name__ == "__main__":
    print(collect())