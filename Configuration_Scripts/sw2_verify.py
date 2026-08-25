from netmiko import ConnectHandler


SW2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group08",
    "port": 5006,
    "timeout" : 500,
}


commands = [
    "show vlan brief",
    "show interfaces trunk",
    "show interfaces status",
    "show mac address-table",
]


try:
    connection = ConnectHandler(**SW2)

    print("Connected to SW2")
    print("\n========== SW2 VERIFICATION ==========\n")

    for command in commands:
        print(f"\n----- {command} -----")
        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"SW2 verification failed: {error}")