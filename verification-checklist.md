# Verification and Validation

## Purpose
This document explains how the automation workflow is validated before, during, and after the configuration change.

## Pre-Change State
Before applying any changes, the following state is captured:

- SSH connectivity to the Cisco IOS XE device is confirmed
- The current hostname is identified
- The current running configuration is backed up to `backup_config.txt`
- A device checkpoint is created as `flash:backup_config.cfg`

## Verification Method
The automation script verifies the applied change by checking the device hostname after configuration is sent.

Verification command used in the script:

```python
verify = connection.send_command("show running-config | include ^hostname")
