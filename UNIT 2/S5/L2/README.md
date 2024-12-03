
# Report Scansioni Nmap

Questo documento fornisce i risultati dettagliati delle scansioni effettuate sul target **Metasploitable** (IP: 192.168.60.2). Sono state eseguite le seguenti tipologie di scansioni:

1. **Fingerprinting del Sistema Operativo**
2. **Scansione SYN**
3. **Scansione TCP Connect**
4. **Rilevamento delle Versioni dei Servizi**

## Target: Metasploitable

### Informazioni Generali:
- **Indirizzo IP**: 192.168.60.2

![Alt_text](./OS fingerprinting.png "OS fingerprint")

### Risultati delle Scansioni:

#### 1. Fingerprinting del Sistema Operativo
- **Sistema Operativo**: Linux 2.6.X

#### 2. Scansione SYN
- **Porte Aperte**: 21, 22, 23, 25, 53, 80, 111, 139, 445, 512, 513, 514, 1099, 1524, 2049, 2121, 3306, 5432, 5900, 6000, 6667, 8009, 8180

#### 3. Scansione TCP Connect
- **Porte Aperte**: 21, 22, 23, 25, 53, 80, 111, 139, 445, 512, 513, 514, 1099, 1524, 2049, 2121, 3306, 5432, 5900, 6000, 6667, 8009, 8180

#### 4. Rilevamento delle Versioni dei Servizi
- **Servizi e Versioni**:
  - Porta 21: vsftpd 2.3.4
  - Porta 22: OpenSSH 4.7p1 (Debian 8ubuntu1)
  - Porta 23: Linux Telnet
  - Porta 25: Postfix smtpd
  - Porta 53: ISC BIND 9.4.2
  - Porta 80: Apache httpd 2.2.8 ((Ubuntu) DAV/2)
  - Porta 111: rpcbind 2 (RPC #100000)
  - Porte 139/445: Samba 3.X - 4.X (Workgroup: WORKGROUP)
  - Porta 3306: MySQL 5.0.51a
  - Porta 5432: PostgreSQL 8.3
  - Porta 5900: VNC Protocol 3.3
  - Porta 6667: UnrealIRCd
  - Porta 8009: Apache JServ (Protocollo v1.3)
  - Porta 8180: Tomcat/Coyote JSP Engine 1.1

---
