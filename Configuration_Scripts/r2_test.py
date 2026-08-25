from netmiko import ConnectHandler


R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5002,
}


tests = {
    "R2 to R1 routed link": "ping 10.8.8.1",
    "R2 to Site A Students gateway": "ping 10.70.1.1",
    "R2 to Site A Teachers gateway": "ping 10.80.1.1",
}


try:
    connection = ConnectHandler(**R2)

    print("========== R2 NETWORK TESTS ==========")

    for purpose, command in tests.items():
        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except Exception as error:
    print(f"R2 testing failed: {error}")