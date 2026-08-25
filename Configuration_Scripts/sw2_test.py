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


tests = {
    "Verify Students VLAN exists": "show vlan id 70",
    "Verify Teachers VLAN exists": "show vlan id 80",
    "Verify router trunk": "show interfaces GigabitEthernet0/1 switchport",
    "Verify trunk VLANs": "show interfaces trunk",
}


try:
    connection = ConnectHandler(**SW2)

    print("========== SW2 OPERATIONAL TESTS ==========")

    for purpose, command in tests.items():
        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"SW2 testing failed: {error}")