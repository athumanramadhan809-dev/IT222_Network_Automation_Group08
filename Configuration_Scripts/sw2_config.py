from netmiko import ConnectHandler


# ============================================
# SW2 CONNECTION DETAILS
# ============================================

SW2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group08",
    "port": 5006,
    "timeout" : 500,
}


# ============================================
# SW2 CONFIGURATION
# Academic Block B
# ============================================

configuration = [
    #Hostname
    "hostname SW1",

    # VLAN 70 - Students
    "vlan 70",
    "name STUDENTS",

    # VLAN 80 - Teachers
    "vlan 80",
    "name TEACHERS",

    # Gi0/1 - Trunk to R2
    "interface GigabitEthernet0/1",
    "description TRUNK_TO_R2",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan 70,80",
    "no shutdown",

    # Gi0/2 - Student PC
    "interface GigabitEthernet0/2",
    "description STUDENT_PC2",
    "switchport mode access",
    "switchport access vlan 70",
    "spanning-tree portfast",
    "no shutdown",

    # Gi0/3 - Teacher PC
    "interface GigabitEthernet0/3",
    "description TEACHER_PC2",
    "switchport mode access",
    "switchport access vlan 80",
    "spanning-tree portfast",
    "no shutdown",
]


# ============================================
# CONNECT AND CONFIGURE
# ============================================

try:
    connection = ConnectHandler(**SW2)

    print("Connected to SW2")

    if SW2["secret"]:
        connection.enable()

    output = connection.send_config_set(configuration)

    print("\n===== SW2 CONFIGURATION OUTPUT =====")
    print(output)

    verification = connection.send_command(
        "show ip interface brief"
    )

    print("\n--- Verification ---")
    print(verification)

    connection.save_config()

    print("\nSW2 configuration saved successfully.")

    connection.disconnect()

except Exception as error:
    print(f"SW2 configuration failed: {error}")