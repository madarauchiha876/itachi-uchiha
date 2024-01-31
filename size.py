import psutil

def get_disk_space():
    disk = psutil.disk_usage('/')
    total_space = disk.total
    used_space = disk.used
    free_space = disk.free

    print(f"Total Disk Space: {total_space / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {used_space / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {free_space / (1024 ** 3):.2f} GB")

def get_ram_details():
    ram = psutil.virtual_memory()
    total_ram = ram.total
    available_ram = ram.available
    used_ram = ram.used

    print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {available_ram / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    get_disk_space()
    print("\n--------------------------------\n")
    get_ram_details()
