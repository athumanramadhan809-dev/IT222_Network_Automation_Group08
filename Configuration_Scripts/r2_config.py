from netmiko import ConnectHandler


# ============================================
# R2 CONNECTION DETAILS
# ============================================

R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5002,
}


# ============================================
# R2 CONFIGURATION
# Secondary School - Site B
# ============================================

configuration = [
    #Hostname
    "hostname R2",
    # Physical interface to SW2
    "interface GigabitEthernet0/0",
    "description TRUNK_TO_SW2",
    "no ip address",
    "no shutdown",

    # Students VLAN 70
    "interface GigabitEthernet0/0.70",
    "description STUDENTS_SITE_B",
    "encapsulation dot1Q 70",
    "ip address 10.70.2.1 255.255.255.0",

    # Teachers VLAN 80
    "interface GigabitEthernet0/0.80",
    "description TEACHERS_SITE_B",
    "encapsulation dot1Q 80",
    "ip address 10.80.2.1 255.255.255.0",

    # R2-R1 routed link
    "interface GigabitEthernet0/1",
    "description R2_TO_R1_OSPF_LINK",
    "ip address 10.8.8.2 255.255.255.252",
    "no shutdown",

    # OSPF
    "router ospf 1",
    "router-id 2.2.2.2",
    "network 10.70.2.0 0.0.0.255 area 0",
    "network 10.80.2.0 0.0.0.255 area 0",
    "network 10.8.8.0 0.0.0.3 area 0",
    #save
    "do wr",
]


# ============================================
# CONNECT AND CONFIGURE
# ============================================

try:
    connection = ConnectHandler(**R2)

    print("Connected to R2")

    if R2["secret"]:
        connection.enable()

    output = connection.send_config_set(configuration)

    print("\n===== R2 CONFIGURATION OUTPUT =====")
    print(output)

    verification = connection.send_command(
        "show ip interface brief"
    )

    print("\n--- Verification ---")
    print(verification)

    connection.save_config()

    print("\nR2 configuration saved successfully.")

    connection.disconnect()

except Exception as error:
    print(f"R2 configuration failed: {error}")