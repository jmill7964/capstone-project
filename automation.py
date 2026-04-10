from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "DEVICE_IP",
    "username": "cisco",
    "password": "cisco123!"
}

connection = ConnectHandler(**device)
print("Connected successfully")

output = connection.send_command("show running-config")

with open("backup_config.txt", "w") as f:
    f.write(output)

print("Backup completed")

checkpoint = connection.send_command_timing(
    "copy running-config flash:backup_config.cfg"
)

if "Destination filename" in checkpoint:
    checkpoint += connection.send_command_timing("\n")

print("Checkpoint created")

connection.send_config_set(["hostname NETLAB-R1"])
print("Configuration change applied")

verify = connection.send_command("show running-config | include hostname")
print(verify)

if "hostname NETLAB-R1" in verify:
    print("Verification successful")
else:
    print("Verification failed")
    print("Starting rollback...")

    rollback = connection.send_command_timing(
        "configure replace flash:backup_config.cfg force"
    )

    if "confirm" in rollback.lower():
        rollback += connection.send_command_timing("\n")

    print("Rollback completed")

