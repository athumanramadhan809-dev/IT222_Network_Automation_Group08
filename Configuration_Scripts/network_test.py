from netmiko import ConnectHandler


# =========================================================
# ROUTER CONNECTIONS
# =========================================================

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5000,
}

R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5002,
}


# =========================================================
# NETWORK TESTS
# =========================================================

r1_tests = {

    "R1 to R2": "ping 10.8.8.2",

    "Site A Students gateway to Site B Students gateway":
        "ping 10.70.2.1",

    "Site A Teachers gateway to Site B Teachers gateway":
        "ping 10.80.2.1",

}


r2_tests = {

    "R2 to R1": "ping 10.8.8.1",

    "Site B Students gateway to Site A Students gateway":
        "ping 10.70.1.1",

    "Site B Teachers gateway to Site A Teachers gateway":
        "ping 10.80.1.1",

}


# =========================================================
# TEST R1
# =========================================================

print("\n" + "=" * 60)
print("SITE A / R1 TESTING")
print("=" * 60)

try:

    connection = ConnectHandler(**R1)

    for purpose, command in r1_tests.items():

        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)

        print(output)

    connection.disconnect()

except Exception as error:

    print(f"R1 testing failed: {error}")


# =========================================================
# TEST R2
# =========================================================

print("\n" + "=" * 60)
print("SITE B / R2 TESTING")
print("=" * 60)

try:

    connection = ConnectHandler(**R2)

    for purpose, command in r2_tests.items():

        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)

        print(output)

    connection.disconnect()

except Exception as error:

    print(f"R2 testing failed: {error}")