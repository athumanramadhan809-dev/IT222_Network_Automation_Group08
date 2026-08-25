from netmiko import ConnectHandler


SW1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group08",
    "port": 5004,
    "timeout" : 500,
}


commands = [
    "show vlan brief",
    "show interfaces trunk",
    "show interfaces status",
    "show mac address-table",
]


try:
    connection = ConnectHandler(**SW1)

    print("Connected to SW1")
    print("\n========== SW1 VERIFICATION ==========\n")

    for command in commands:
        print(f"\n----- {command} -----")
        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"SW1 verification failed: {error}")