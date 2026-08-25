from netmiko import ConnectHandler


# ============================================
# R1 CONNECTION DETAILS
# ============================================

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5000,
}


# ============================================
# R1 CONFIGURATION
# Secondary School - Site A
# ============================================

configuration = [
    #Hostname
    "hostname R1",
    
    # Physical interface to SW1
    "interface GigabitEthernet0/0",
    "description TRUNK_TO_SW1",
    "no ip address",
    "no shutdown",

    # Students VLAN 70
    "interface GigabitEthernet0/0.70",
    "description STUDENTS_SITE_A",
    "encapsulation dot1Q 70",
    "ip address 10.70.1.1 255.255.255.0",

    # Teachers VLAN 80
    "interface GigabitEthernet0/0.80",
    "description TEACHERS_SITE_A",
    "encapsulation dot1Q 80",
    "ip address 10.80.1.1 255.255.255.0",

    # R1-R2 routed link
    "interface GigabitEthernet0/1",
    "description R1_TO_R2_OSPF_LINK",
    "ip address 10.8.8.1 255.255.255.252",
    "no shutdown",

    # OSPF
    "router ospf 1",
    "router-id 1.1.1.1",
    "network 10.70.1.0 0.0.0.255 area 0",
    "network 10.80.1.0 0.0.0.255 area 0",
    "network 10.8.8.0 0.0.0.3 area 0",
    #save
    "do wr",
]


# ============================================
# CONNECT AND CONFIGURE
# ============================================

try:
    connection = ConnectHandler(**R1)

    print("Connected to R1")

    if R1["secret"]:
        connection.enable()

    output = connection.send_config_set(configuration)

    print("\n===== R1 CONFIGURATION OUTPUT =====")
    print(output)

    verification = connection.send_command(
        "show ip interface brief"
    )

    print("\n--- Verification ---")
    print(verification)

    connection.save_config()

    print("\nR1 configuration saved successfully.")

    connection.disconnect()

except Exception as error:
    print(f"R1 configuration failed: {error}")