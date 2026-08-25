from netmiko import ConnectHandler


R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5000,
}


commands = [
    "show ip interface brief",
    "show interfaces GigabitEthernet0/0.70",
    "show interfaces GigabitEthernet0/0.80",
    "show ip ospf neighbor",
    "show ip route",
    "show ip route ospf",
]


try:
    connection = ConnectHandler(**R1)

    print("Connected to R1")
    print("\n========== R1 VERIFICATION ==========\n")

    for command in commands:
        print(f"\n----- {command} -----")
        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"R1 verification failed: {error}")