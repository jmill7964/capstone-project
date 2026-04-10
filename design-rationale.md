# Design Rationale: Automated Configuration Backup, Change, Verification, and Rollback

## Introduction
This project was designed as an instructional network automation lab for undergraduate networking students. The lab teaches students how to implement a safe automation workflow using Python and Cisco IOS XE in the NDG Netlab DevNet environment. Rather than focusing only on making a configuration change, the lab emphasizes the full operational lifecycle of change management, including backup, validation, and rollback.

The lab was intentionally scoped to fit within a 45–75 minute completion window while still exposing students to realistic automation concepts. The overall design reflects the idea that network automation must be technically correct, operationally safe, and instructionally clear.

## Tool and Approach Selection
Python was selected as the primary automation language because it is widely used in network automation and is accessible to undergraduate students. Its syntax is readable, and it supports a large ecosystem of libraries relevant to network programmability.

Netmiko was selected as the primary automation library because it provides a simple and reliable SSH interface for Cisco IOS XE devices. This allows students to automate tasks using the same command-line concepts they are already learning in traditional networking courses. Netmiko also reduces the complexity of connection handling, command execution, and configuration mode transitions.

The Cisco IOS XE CSR1000v platform was used because it aligns with the NDG Netlab DevNet environment required for the course. It also provides a realistic enterprise-style environment while remaining accessible in a virtual lab setting.

A CLI-based automation approach was chosen instead of NETCONF or RESTCONF because the goal of this lab is to provide a manageable entry point for undergraduate students. While model-driven interfaces are more structured and robust, they also introduce additional complexity in payload construction, schema understanding, and protocol handling. For this instructional context, CLI-based automation offers a more practical balance between realism and accessibility.

## Automation Workflow Design
The automation workflow follows a structured sequence:

1. Prompt the user for device IP address, username, and password  
2. Establish an SSH connection to the device  
3. Capture the running configuration and save it locally  
4. Create a device checkpoint in flash storage  
5. Apply a configuration change  
6. Verify the result of the change  
7. Trigger rollback if verification fails  
8. Disconnect from the device  

This workflow was chosen because it mirrors real-world change management practices. Production network changes should not be made without a backup, and they should not be considered complete until validation confirms that the intended state was achieved.

The selected configuration change was limited to the device hostname. This was an intentional instructional decision. A hostname change is easy to verify, introduces minimal operational risk, and provides a clear example of pre-change state, post-change state, and rollback behavior.

## Design Tradeoffs
One major tradeoff in this project was simplicity versus robustness. A more advanced implementation could use structured parsing tools such as pyATS/Genie or a model-driven interface such as NETCONF. However, these approaches would add technical depth at the cost of greater complexity for students.

By using Netmiko and CLI-based verification, the lab remains understandable and achievable within the required timeframe. The tradeoff is that CLI output is less structured than API-based responses, which can make parsing and validation less precise.

Another tradeoff was security versus instructional simplicity. To satisfy repository quality expectations, the final automation script prompts the user for credentials rather than hardcoding them. This improves security and aligns with best practices. At the same time, it slightly increases the number of prompts students must work through while testing the script.

A third tradeoff involved scope control. The lab could have been expanded to include interface configuration, VLAN creation, or policy changes. However, such changes increase the risk of disrupting connectivity and may complicate rollback behavior. Restricting the change to the hostname keeps the lab safe and focused while still demonstrating the essential concepts.

## Error Handling and Risk Mitigation
Error handling is a key part of the design. The script includes handling for authentication failure, connection timeout, and general unexpected exceptions. This helps students understand that automation workflows must anticipate failure conditions rather than assuming success.

Risk mitigation is built into the lab in several ways. First, a local backup is created before any change is made. Second, a device checkpoint is stored in flash so that rollback can be performed directly on the device. Third, the scope of change is limited to the hostname, which minimizes the chance of breaking management access or routing behavior. Finally, the lab requires students to intentionally trigger a verification failure so they can observe the rollback process in action.

This emphasis on rollback is one of the most important design features of the project. In operational environments, failed changes must be reversible. By making rollback a required part of the student demonstration, the lab reinforces the principle that safe automation is not just about speed—it is about control and recoverability.

## Verification Strategy
The verification method used in this lab is intentionally straightforward. After the configuration change is applied, the script runs:

```python
verify = connection.send_command("show running-config | include ^hostname")
