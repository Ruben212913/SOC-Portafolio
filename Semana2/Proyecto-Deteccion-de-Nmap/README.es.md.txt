Project Documentation: Capturing Unencrypted HTTP Traffic with Wireshark

1. Executive Summary
This document details the procedure for setting up a virtual network environment, establishing a local web server, and capturing and analyzing unencrypted HTTP traffic. The main objective was to demonstrate the vulnerability of information transmitted over an unencrypted protocol, such as HTTP, using the Wireshark protocol analyzer.

2. Project Objectives
Configure an isolated network: Establish a network connection between two virtual machines (Ubuntu and Kali Linux) using a VirtualBox Internal Network.

Create an insecure web server: Launch a local HTTP server to serve content in plain text.

Capture network traffic: Use Wireshark to intercept all data packets circulating between the server and the client.

Analyze plain text information: Demonstrate that the data from an HTTP request and response are visible and readable to anyone capturing the traffic.

3. Tools and Environment
Virtualization Software: VirtualBox

Virtual Machine 1 (Server): Ubuntu

Virtual Machine 2 (Client / Analyzer): Kali Linux

Web Server: Python 3 (http.server)

Protocol Analyzer: Wireshark

4. Detailed Procedure
Step 1: Virtual Environment Configuration
Both virtual machines were configured in VirtualBox with the network adapter in "Internal Network" mode. This ensured they could communicate with each other on an isolated network, without external access.

Step 2: Launching the Unencrypted HTTP Server (on Ubuntu)
A test HTML file (test.html) was created in the main Ubuntu folder.

Bash

echo "<h1>The test server works!</h1>" > test.html
A web server was launched on port 8000 using the Python module.

Bash

python3 -m http.server 8000
The machine's IP address for the internal network was verified with the ifconfig command, identifying it as 10.0.3.5 on the enp0s8 interface.

Step 3: Packet Capture (on Kali Linux)
The Kali machine's internal network interface was identified as eth1, with the IP address 10.0.3.4.

Wireshark was started with superuser permissions to ensure it could capture all packets.

Bash

sudo wireshark
Inside Wireshark, the eth1 interface was selected to begin the capture.

Step 4: Generating and Analyzing Traffic
In the Kali browser (Firefox), the page served by Ubuntu was accessed.

http://10.0.3.5:8000/test.html
After the page loaded, the capture in Wireshark was stopped.

A filter was applied to isolate the relevant traffic.

tcp.port == 8000 and http
The GET /test.html packet was selected, and the Follow > HTTP Stream function was used.

5. Conclusions and Vulnerability Demonstration
The exercise clearly demonstrated the unencrypted nature of the HTTP protocol. In the Wireshark "HTTP Stream" window, the content of the request and response, including the message <h1>The test server works!</h1>, was observed exposed in plain text.

This proves that any sensitive information (such as usernames, passwords, or personal data) sent through an HTTP website would be completely visible to an attacker capturing traffic on the same network. The only way to protect this information is by migrating to secure communication protocols like HTTPS, which encrypt traffic end-to-end.