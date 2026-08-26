# IT 222 - Assignment 8

# Secondary School Campus Network Automation

---

## 1. Assignment Identification

| Item | Details |

| Assignment Number | 8 |
| Scenario | Secondary School Campus Network |
| Group Number | Group 08 |
| Routing Protocol | OSPF |
| Network Devices | R1, R2, SW1, SW2 |
| Automation Language | Python |
| Automation Library | Netmiko |
| Network Simulation Platform | GNS3 |

---

# 2. Group Members

|No.| Name | Registration Number |

| 1 | RAMADHAN ATHUMAN RAMADHAN | 2024/0873 |
| 2 | SADA HAMUDU SALIMU | 2024/1334 |
| 3 | MWAMARY SULEIMAN ISSA | 2024/0696 |
| 4 | SALOME ROBERT MALILO | 2024/1264 |

---

# 3. Scenario Description

The scenario represents a secondary school campus consisting of two
academic blocks.

The school network contains two main user functions:

- Students
- Teachers

Student computers and Teacher computers must be logically separated
using different VLANs. However, both academic blocks must remain
connected through the routed network.

The network consists of two routers (R1 and R2) and two switches
(SW1 and SW2). Each site contains Student and Teacher end devices.

The network uses VLAN segmentation, router-on-a-stick inter-VLAN
routing, an R1-to-R2 routed link, and OSPF for dynamic routing
between the two academic blocks.

---

# 4. Network Requirements

The network is designed to achieve the following requirements:

1. Separate Student computers from Teacher computers using VLANs.

2. Provide a dedicated Student VLAN.

3. Provide a dedicated Teacher VLAN.

4. Provide connectivity between the two academic blocks.

5. Allow Student networks to communicate between Site A and Site B.

6. Allow Teacher networks to communicate between Site A and Site B.

7. Provide inter-VLAN routing through the routers.

8. Configure trunk connectivity between each router and its
   corresponding switch.

9. Establish routed connectivity between R1 and R2.

10. Use OSPF to exchange routes between the two sites.

11. Automate device configuration using Python and Netmiko.

12. Provide verification scripts to confirm the correct operation
    of the configured devices.

13. Provide network-level testing scripts to demonstrate
    end-to-end connectivity.

---

# 5. Network Topology

The network contains the following main components:

```text
                         SECONDARY SCHOOL CAMPUS NETWORK


             SITE A                                      SITE B

       Student-PC1                                  Student-PC2
       10.70.1.10                                   10.70.2.10
             |                                            |
             | Gi0/2                                      | Gi0/2
             |                                            |
           SW1                                          SW2
             |                                            |
             | Gi0/1                                     | Gi0/1
             |                                            |
             |                                            |
            R1 ========================================== R2
                 R1-R2 Routed Link: 10.8.8.0/30
                         OSPF Area 0
             |                                            |
             | Gi0/1                                      | Gi0/1
          Trunk Link                                   Trunk Link
             |                                            |
             |                                            |
           SW1                                          SW2
             |                                            |
          Gi0/3                                        Gi0/3
             |                                            |
       Teacher-PC1                                  Teacher-PC2
       10.80.1.10                                   10.80.2.10
Main Devices
R1 - Site A router
R2 - Site B router
SW1 - Site A access switch
SW2 - Site B access switch
Student-PC1 - Student endpoint at Site A
Teacher-PC1 - Teacher endpoint at Site A
Student-PC2 - Student endpoint at Site B
Teacher-PC2 - Teacher endpoint at Site B


# 6. VLAN Design

Two VLANs are used to separate Student and Teacher functions.

VLAN ID	VLAN Name	         Function
70	      Students	         Student computers
80	      Teachers	         Teacher computers

The Student and Teacher VLANs are maintained at both academic
blocks.

#  7. IP Addressing Plan

Site A
Function	VLAN	Network	      Gateway	     Host
Students	70	10.70.1.0/24	10.70.1.1	10.70.1.10
Teachers	80	10.80.1.0/24	10.80.1.1	10.80.1.10

Site B
Function	VLAN	Network	       Gateway	   Host
Students	70	10.70.2.0/24	10.70.2.1	10.70.2.10
Teachers	80	10.80.2.0/24	10.80.2.1	10.80.2.10


R1-R2 Routed Link
Link	Network
R1-R2	10.8.8.0/30

The /30 network provides the point-to-point routed connection between
R1 and R2.

# 8. Interface and Port Assignment

The assignment specifies the following interface roles:

Device	Interface	      Function
R1	      Gi0/1	            Trunk toward SW1
R2	      Gi0/1	            Trunk toward SW2
SW1	      Gi0/1       	Trunk toward R1
SW2	      Gi0/1	            Trunk toward R2
SW1	      Gi0/2	            Students VLAN 70
SW1	      Gi0/3	            Teachers VLAN 80
SW2	      Gi0/2	            Students VLAN 70
SW2	      Gi0/3	            Teachers VLAN 80

The Gi0/1 router-to-switch links carry the required VLAN traffic
between the switches and routers.



# 9. Routing Method
OSPF

The network uses Open Shortest Path First (OSPF) as the dynamic
routing protocol.

OSPF is used to exchange routes between R1 and R2 so that both
academic blocks can reach the required remote networks.

The OSPF configuration is designed to allow the routers to learn
the remote Student and Teacher networks dynamically.

The R1-R2 routed link is used as the OSPF adjacency path.




10. Router-on-a-Stick Design

Inter-VLAN routing is implemented using router subinterfaces.

The router-facing trunk interface carries traffic for:

VLAN 70 - Students
VLAN 80 - Teachers

Each VLAN is assigned a corresponding gateway on its local router.

Example logical design:

R1
 |
 +-- Gi0/1.70 ---- VLAN 70 Students
 |
 +-- Gi0/1.80 ---- VLAN 80 Teachers

and:

R2
 |
 +-- Gi0/1.70 ---- VLAN 70 Students
 |
 +-- Gi0/1.80 ---- VLAN 80 Teachers



# 11. Scenario Requirements Analysis
Requirement	Configuration Used	Verification	Operational Test
Separate Students and Teachers	VLAN 70 and VLAN 80	show vlan brief	Verify devices are assigned to correct VLANs
Connect Site A and Site B	R1-R2 routed link	show ip interface brief	Ping R1 to R2
Carry VLAN traffic between router and switch	Gi0/1 trunk	show interfaces trunk	Verify trunk status and VLANs
Provide Student gateway	Student router subinterface	show ip interface brief	Student PC → Student gateway
Provide Teacher gateway	Teacher router subinterface	show ip interface brief	Teacher PC → Teacher gateway
Exchange remote routes	OSPF	show ip ospf neighbor	Verify OSPF adjacency
Learn remote networks	OSPF	show ip route ospf	Verify remote VLAN routes
Student communication between sites	Routing + VLAN configuration	Routing table and ping	Student Site A → Student Site B
Teacher communication between sites	Routing + VLAN configuration	Routing table and ping	Teacher Site A → Teacher Site B




# 12. Python Automation

Python automation is used to configure, verify, and test the network
devices.

The project uses Netmiko to establish connections to the Cisco IOS
devices and execute the required configuration and verification
commands.

The automation is organized into three main functions:

Configuration
Verification
Testing

Each network device has scenario-specific scripts.


# 13. Configuration Scripts

The Configuration_Scripts/ directory contains the completed
scenario-specific Python scripts.

Expected structure:

Configuration_Scripts/
│
├── r1_config.py
├── r1_verify.py
├── r1_test.py
│
├── r2_config.py
├── r2_verify.py
├── r2_test.py
│
├── sw1_config.py
├── sw1_verify.py
├── sw1_test.py
│
├── sw2_config.py
├── sw2_verify.py
├── sw2_test.py
│
├── network_verify.py
└── network_test.py
Device Configuration Scripts
r1_config.py - Configures R1
r2_config.py - Configures R2
sw1_config.py - Configures SW1
sw2_config.py - Configures SW2
Device Verification Scripts
r1_verify.py
r2_verify.py
sw1_verify.py
sw2_verify.py

These scripts collect evidence showing that the required
configuration has been applied correctly.

Device Testing Scripts
r1_test.py
r2_test.py
sw1_test.py
sw2_test.py

These scripts perform device-level operational tests.

14. Network-Level Verification

The network_verify.py script is responsible for collecting
evidence from multiple devices to demonstrate that the integrated
network is operating correctly.

Important verification commands include:

show ip interface brief
show interfaces trunk
show vlan brief
show ip ospf neighbor
show ip route
show ip route ospf

The verification process should confirm:

Interfaces are operational.
VLANs exist.
Access ports are assigned correctly.
Trunk links are operational.
Router subinterfaces are operational.
R1 and R2 form an OSPF neighbor relationship.
Remote Student networks are learned.
Remote Teacher networks are learned.
15. Network-Level Testing

The network_test.py script performs scenario-based end-to-end
connectivity tests.

/*************Point to Remember****************************/

Inorder to confirm ping from student PCs and Teacher PCs to another end-devices you must first confirgure it. Since we are used Firefox docker as client devices, open it and open terminal inside Firefox docker and then enter the followings commands to provides ip address on a device manually.
   For Student-PC on site A
   *********************************
     sudo ip addr add 10.70.1.10/24 dev eth0
     sudo ip link set eth0 up
     sudo ip route add default via 10.70.1.1
  ***********************************
     For Teacher-PC on site A
   *********************************
     sudo ip addr add 10.80.1.10/24 dev eth0
     sudo ip link set eth0 up
     sudo ip route add default via 10.80.1.1
  ***********************************
     For Student-PC on site B
   *********************************
     sudo ip addr add 10.70.2.10/24 dev eth0
     sudo ip link set eth0 up
     sudo ip route add default via 10.70.2.1
  ***********************************
     For Student-PC on siteA
   *********************************
     sudo ip addr add 10.80.2.10/24 dev eth0
     sudo ip link set eth0 up
     sudo ip route add default via 10.80.2.1
  ***********************************
/***********This Above is important because end-host devices does not save ip address like routers and swtches, so before Ping Tests need to confirgure it first************************/




Test 1 - Student Site A to Student Site B
Source:
Student-PC1
10.70.1.10

Destination:
Student-PC2
10.70.2.10

Expected Result:
SUCCESS

Purpose:

To demonstrate that Student networks remain connected across the
two academic blocks.

Test 2 - Teacher Site A to Teacher Site B
Source:
Teacher-PC1
10.80.1.10

Destination:
Teacher-PC2
10.80.2.10

Expected Result:
SUCCESS

Purpose:

To demonstrate that Teacher networks remain connected across the
two academic blocks.

Test 3 - Student Site A Default Gateway
Source:
Student-PC1
10.70.1.10

Destination:
10.70.1.1

Expected Result:
SUCCESS

Purpose:

To verify Student VLAN gateway connectivity.

Test 4 - Teacher Site A Default Gateway
Source:
Teacher-PC1
10.80.1.10

Destination:
10.80.1.1

Expected Result:
SUCCESS

Purpose:

To verify Teacher VLAN gateway connectivity.

Test 5 - R1 to R2
Source:
R1

Destination:
R2

Network:
10.8.8.0/30

Expected Result:
SUCCESS

Purpose:

To verify the routed connection between the two academic blocks.

Test 6 - OSPF Neighbor Formation

Verification command:

show ip ospf neighbor

Expected Result:

R1 and R2 should establish an OSPF neighbor relationship.

Purpose:

To confirm that dynamic routing is operating between the two
routers.

Test 7 - OSPF Learned Routes

Verification command:

show ip route ospf

Expected Result:

Each router should learn the required remote networks through OSPF.

Purpose:

To confirm that the network can dynamically reach the remote
academic block.

16. Expected Network Behaviour

After successful configuration, the network should provide:

Student Site A
      |
      | VLAN 70
      |
     R1
      |
      | OSPF
      |
     R2
      |
      | VLAN 70
      |
Student Site B

and:

Teacher Site A
      |
      | VLAN 80
      |
     R1
      |
      | OSPF
      |
     R2
      |
      | VLAN 80
      |
Teacher Site B

Therefore:

Student Site A should reach Student Site B.
Teacher Site A should reach Teacher Site B.
R1 should reach R2.
OSPF neighbors should form.
OSPF routes should be learned.
Student and Teacher functions should remain logically separated
through VLANs.



17. How to Run the Project
Step 1 - Open GNS3

Open the GNS3 project located in:

GNS3_Project_File/
Step 2 - Start the Devices

Start:

R1
R2
SW1
SW2
Student-PC1
Teacher-PC1
Student-PC2
Teacher-PC2
Step 3 - Confirm Device Console Information

The Python scripts use the GNS3 console/TELNET connection information
for the Cisco IOS devices.

The connection information should include:

GNS3 VM/Server IP
TELNET console port
Device type

The TELNET port may change when the GNS3 project is modified.

Step 4 - Install Python Dependencies

Install Netmiko:

pip install netmiko

If a Python virtual environment is used:

python -m venv venv

Activate it before installing the required packages.

Step 5 - Configure the Devices

Run the configuration scripts in the following order:

1. r1_config.py
2. r2_config.py
3. sw1_config.py
4. sw2_config.py
Step 6 - Verify Individual Devices

Run:

1. r1_verify.py
2. r2_verify.py
3. sw1_verify.py
4. sw2_verify.py
Step 7 - Verify the Integrated Network

Run:

python network_verify.py
Step 8 - Run End-to-End Tests

Run:

python network_test.py

The test results should demonstrate the required Student and Teacher
communication between the two academic blocks and confirm OSPF
operation.



18. Repository Structure

The project follows the required GitHub repository structure:

IT222_Network_Automation_Group08/
│
├── Configuration_Scripts/
│   ├── r1_config.py
│   ├── r1_verify.py
│   ├── r1_test.py
│   ├── r2_config.py
│   ├── r2_verify.py
│   ├── r2_test.py
│   ├── sw1_config.py
│   ├── sw1_verify.py
│   ├── sw1_test.py
│   ├── sw2_config.py
│   ├── sw2_verify.py
│   ├── sw2_test.py
│   ├── network_verify.py
│   └── network_test.py
│
├── GNS3_Project_File/
│
├── Templates/
│
├── Usage_Examples/
│
└── README.md

The original supplied templates are retained in Templates/ for
reference.

The supplied example scripts are retained in Usage_Examples/ for
learning and reference.

The completed scenario-specific work is maintained in
Configuration_Scripts/.

19. Assumptions

The following assumptions apply to this implementation:

GNS3 is used as the network simulation environment.
Cisco IOS devices support the required VLAN, trunk, subinterface,
routing, and OSPF commands.
Python and Netmiko are available on the automation workstation.
The required Cisco IOS images are already available in the GNS3
environment.
The end devices are configured according to the addressing plan
documented in this README.
The R1-R2 routed link uses the assigned 10.8.8.0/30 network.
TELNET console information is obtained from the current GNS3
project before running the automation scripts.
22. Conclusion

This project implements an automated secondary school campus
network connecting two academic blocks.

VLAN 70 is used for Students and VLAN 80 is used for Teachers.
The two VLAN functions are logically separated while the two
academic blocks remain connected through R1 and R2.

OSPF provides dynamic route exchange between the routers, while
Python and Netmiko are used to automate configuration, verification,
and testing.

The completed project demonstrates:

VLAN segmentation
Access-port configuration
Trunk configuration
Router-on-a-stick
IP addressing
Inter-site routing
OSPF neighbor formation
OSPF route learning
End-to-end Student connectivity
End-to-end Teacher connectivity
Network verification
Automated network testing

A future security enhancement can introduce stateful access control
between Student and Teacher networks while preserving required
Student-to-Student and Teacher-to-Teacher communication.

23. Project Status
[✅] GNS3 topology completed
[✅] R1 configuration completed
[✅] R2 configuration completed
[✅] SW1 configuration completed
[✅] SW2 configuration completed
[✅] Student VLAN verified
[✅] Teacher VLAN verified
[✅] Trunk links verified
[✅] Router subinterfaces verified
[✅] R1-R2 connectivity verified
[✅] OSPF neighbor verified
[✅] OSPF routes verified
[✅] Student Site A → Student Site B tested
[✅] Teacher Site A → Teacher Site B tested
[✅] network_verify.py completed
[✅] network_test.py completed
[✅] README.md completed
[✅] GitHub repository organized
[✅] Final GitHub repository URL checked

# GitHub Repository

Repository: IT222_Network_Automation_Group08

GitHub URL: https://github.com/athumanramadhan809-dev/IT222_Network_Automation_Group08.git
```
