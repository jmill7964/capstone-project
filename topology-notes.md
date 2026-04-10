# Topology Notes

## Topology Description
This lab uses a simple two-node topology:

- Linux Host
  - Runs Python automation script
  - Uses Netmiko for SSH-based automation

- Cisco IOS XE Device (CSR1000v)
  - Receives configuration commands
  - Stores checkpoint file for rollback

## Connection
- The Linux host connects to the CSR1000v over SSH

## Lab Alignment
This topology matches the lab environment used in NDG Netlab DevNet and reflects the instructional workflow described in the student lab.

## Label Requirements
The topology diagram should clearly label:
- Linux Host
- SSH
- Cisco IOS XE / CSR1000v
