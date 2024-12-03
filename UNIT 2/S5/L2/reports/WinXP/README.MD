# Nmap Scan Report

## Scan Details
- **Scan Date**: Tue Dec 3 16:53:33 2024
- **Nmap Version**: 7.94SVN
- **Arguments Used**:  
  `/usr/lib/nmap/nmap --privileged -A --script=default,vuln,smb-enum-shares,http-enum --script-timeout 30s --max-retries 3 -oA report 192.168.50.3`
- **Scan Duration**: 34.53 seconds
- **Hosts Scanned**: 1 IP address (1 host up)

---

## Host: 192.168.50.3
- **MAC Address**: 00:0C:29:DD:2F:3F (VMware)

### Ports Summary
- **997 Ports**: Closed (replied with `reset`)
- **Open Ports**:
  | Port | Protocol | State | Service           | Reason    | Product                        | Version | Extra Info |
  |------|----------|-------|-------------------|-----------|--------------------------------|---------|------------|
  | 135  | tcp      | open  | msrpc             | syn-ack   | Microsoft Windows RPC          |         |            |
  | 139  | tcp      | open  | netbios-ssn       | syn-ack   | Microsoft Windows netbios-ssn  |         |            |
  | 445  | tcp      | open  | microsoft-ds      | syn-ack   | Windows XP microsoft-ds        |         |            |

---

### Remote Operating System Detection
- **Ports Used**:  
  - `135/tcp` (open)  
  - `1/tcp` (closed)  
  - `44504/udp` (closed)
- **OS Match**: Microsoft Windows XP SP2 or SP3 (100%)

---

### Host Script Output
| Script Name           | Output                                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **smb-enum-shares**   | ERROR: Enumerating shares failed (NT_STATUS_ACCESS_DENIED). Anonymous access for `ADMIN$`, `C$`, and `IPC$` shares: Denied except for `IPC$` (Read Access).       |
| **nbstat**            | NetBIOS name: WINXP-VM, NetBIOS user: `<unknown>`, NetBIOS MAC: 00:0C:29:DD:2F:3F (VMware).                                                                      |
| **smb-vuln-ms08-067** | VULNERABLE: Microsoft Windows system vulnerable to remote code execution (MS08-067). Disclosure date: 2008-10-23.                                               |
| **smb-security-mode** | Authentication level: user, Challenge-response: supported, Message signing: disabled (dangerous, but default).                                                  |
| **smb-vuln-ms10-054** | false                                                                                                                                                          |
| **samba-vuln-cve-2012-1182** | NT_STATUS_ACCESS_DENIED                                                                                                                                |
| **clock-skew**        | Mean: -30m00s, Deviation: 42m25s, Median: -1h00m00s                                                                                                             |
| **smb2-time**         | Protocol negotiation failed (SMB2).                                                                                                                             |
| **smb-vuln-ms10-061** | ERROR: Script execution failed.                                                                                                                                 |
| **smb-os-discovery**  | OS: Windows XP (Windows 2000 LAN Manager), Workgroup: DIALOCAN, System time: 2024-12-03T16:53:51+01:00.                                                         |

---

### Miscellaneous Metrics
- **Ping Results**: arp-response
- **Network Distance**: 1 hop
- **TCP Sequence Prediction**: Difficulty=265 (Good luck!)
- **IP ID Sequence Generation**: Incremental

---

**Note**: This report is generated from an Nmap scan output formatted using custom XSL stylesheets.
