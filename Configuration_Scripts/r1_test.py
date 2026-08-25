from netmiko import ConnectHandler


R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5000,
}


tests = {
    "R1 to R2 routed link": "ping 10.8.8.2",
    "R1 to Site B Students gateway": "ping 10.70.2.1",
    "R1 to Site B Teachers gateway": "ping 10.80.2.1",
}


try:
    connection = ConnectHandler(**R1)

    print("========== R1 NETWORK TESTS ==========")

    for purpose, command in tests.items():
        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"R1 testing failed: {error}")