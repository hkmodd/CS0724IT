 /\* stylesheet print \*/ @media print { #menu { display:none; } body { font-family: Verdana, Helvetica, sans-serif; } h1 { font-size: 13pt; font-weight:bold; margin:4pt 0pt 0pt 0pt; padding:0; } h2 { font-size: 12pt; font-weight:bold; margin:3pt 0pt 0pt 0pt; padding:0; } h3, a:link, a:visited { font-size: 9pt; font-weight:bold; margin:1pt 0pt 0pt 20pt; padding:0; text-decoration: none; color: #000000; } p,ul { font-size: 9pt; margin:1pt 0pt 8pt 40pt; padding:0; text-align:left; } li { font-size: 9pt; margin:0; padding:0; text-align:left; } table { margin:1pt 0pt 8pt 40pt; border:0px; width:90% } td { border:0px; border-top:1px solid black; font-size: 9pt; } .head td { border:0px; font-weight:bold; font-size: 9pt; } .noprint { display: none; } } /\* stylesheet screen \*/ @media screen { body { font-family: Verdana, Helvetica, sans-serif; margin: 0px; background-color: #FFFFFF; color: #000000; text-align: center; } #container { text-align:left; margin: 10px auto; width: 90%; } h1 { font-family: Verdana, Helvetica, sans-serif; font-weight:bold; font-size: 14pt; color: #FFFFFF; background-color:#2A0D45; margin:10px 0px 0px 0px; padding:5px 4px 5px 4px; width: 100%; border:1px solid black; text-align: left; } h2 { font-family: Verdana, Helvetica, sans-serif; font-weight:bold; font-size: 11pt; color: #000000; margin:30px 0px 0px 0px; padding:4px; width: 100%; background-color:#F0F8FF; text-align: left; } h2.green { color: #000000; background-color:#CCFFCC; border-color:#006400; } h2.red { color: #000000; background-color:#FFCCCC; border-color:#8B0000; } h3 { font-family: Verdana, Helvetica, sans-serif; font-weight:bold; font-size: 10pt; color:#000000; background-color: #FFFFFF; width: 75%; text-align: left; } p { font-family: Verdana, Helvetica, sans-serif; font-size: 8pt; color:#000000; background-color: #FFFFFF; width: 75%; text-align: left; } p i { font-family: Verdana, Helvetica, sans-serif; font-size: 8pt; color:#000000; background-color: #CCCCCC; } ul { font-family: Verdana, Helvetica, sans-serif; font-size: 8pt; color:#000000; background-color: #FFFFFF; width: 75%; text-align: left; } a { font-family: Verdana, Helvetica, sans-serif; text-decoration: none; font-size: 8pt; color:#000000; font-weight:bold; background-color: #FFFFFF; color: #000000; } li a { font-family: Verdana, Helvetica, sans-serif; text-decoration: none; font-size: 10pt; color:#000000; font-weight:bold; background-color: #FFFFFF; color: #000000; } a:hover { text-decoration: underline; } a.up { color:#006400; } table { width: 80%; border:0px; color: #000000; background-color: #000000; margin:10px; } tr { vertical-align:top; font-family: Verdana, Helvetica, sans-serif; font-size: 8pt; color:#000000; background-color: #FFFFFF; } tr.head { background-color: #E1E1E1; color: #000000; font-weight:bold; } tr.open { background-color: #CCFFCC; color: #000000; } tr.script { background-color: #EFFFF7; color: #000000; } tr.filtered { background-color: #F2F2F2; color: #000000; } tr.closed { background-color: #F2F2F2; color: #000000; } td { padding:2px; } #menu li { display : inline; margin : 0; /\*margin-right : 10px;\*/ padding : 0; list-style-type : none; } #menubox { position: fixed; bottom: 0px; right: 0px; width: 120px; } /\* This section handle's IE's refusal to honor the fixed CSS attribute \*/ \* html div#menubox { position: absolute; top:expression(eval( document.compatMode && document.compatMode=='CSS1Compat') ? documentElement.scrollTop+(documentElement.clientHeight-this.clientHeight) : document.body.scrollTop +(document.body.clientHeight-this.clientHeight)); } /\* This fixes the jerky effect when scrolling in IE\*/ \* html,\* html body { background: #fff url(nosuchfile) fixed; } .up { color: #000000; background-color:#CCFFCC; } .down { color:#626262; background-color: #F2F2F2; } .print\_only { display: none; } .hidden { display: none; } .unhidden { display: block; } } Nmap Scan Report - Scanned at Tue Dec 3 16:53:33 2024 function toggle(divID) { var item = document.getElementById(divID); if (item) { item.className=(item.className=='hidden')?'unhidden':'hidden'; } } function togglePorts(tableID,portState) { var table = document.getElementById(tableID); var tbody = table.getElementsByTagName("tbody")\[0\]; var rows = tbody.getElementsByTagName("tr"); for (var i=0; i < rows.length; i++) { var value = rows\[i\].getElementsByTagName("td")\[2\].firstChild.nodeValue; if (value == portState) { rows\[i\].style.display = (rows\[i\].style.display == 'none')?'':'none'; } } } function toggleAll(portState) { var allTables = document.getElementsByTagName("table"); for (var c=0; c < allTables.length; c++) { if (allTables\[c\].id != "") { togglePorts(allTables\[c\].id, portState) } } } function init (){ toggleAll('closed'); toggleAll('filtered'); } window.onload = init;

Nmap Scan Report - Scanned at Tue Dec 3 16:53:33 2024
=====================================================

*   [Scan Summary](#scansummary)
*   | [192.168.50.3](#host_192_168_50_3)

* * *

Scan Summary
------------

Nmap 7.94SVN was initiated at Tue Dec 3 16:53:33 2024 with these arguments:  
_/usr/lib/nmap/nmap --privileged -A --script=default,vuln,smb-enum-shares,http-enum --script-timeout 30s --max-retries 3 -oA report 192.168.50.3_  

Verbosity: 0; Debug level 0

Nmap done at Tue Dec 3 16:54:07 2024; 1 IP address (1 host up) scanned in 34.53 seconds

* * *

192.168.50.3(online)
--------------------

### Address

*   192.168.50.3 (ipv4)
*   00:0C:29:DD:2F:3F - VMware (mac)

### Ports

The 997 ports scanned but not shown below are in state: **closed**

*   997 ports replied with: **reset**
    

Port

State [(toggle closed \[0\]](javascript:togglePorts('porttable_192.168.50.3','closed');) [| filtered \[0\])](javascript:togglePorts('porttable_192.168.50.3','filtered');)

Service

Reason

Product

Version

Extra info

135

tcp

open

msrpc 

syn-ack

Microsoft Windows RPC 

 

 

139

tcp

open

netbios-ssn 

syn-ack

Microsoft Windows netbios-ssn 

 

 

445

tcp

open

microsoft-ds 

syn-ack

Windows XP microsoft-ds 

 

 

### Remote Operating System Detection

*   Used port: **135/tcp** (**open**)
*   Used port: **1/tcp** (**closed**)
*   Used port: **44504/udp** (**closed**)
*   OS match: **Microsoft Windows XP SP2 or SP3** (**100%**)

### Host Script Output

Script Name

Output

smb-enum-shares 

  note: ERROR: Enumerating shares failed, guessing at common ones (NT\_STATUS\_ACCESS\_DENIED)
  account\_used: <blank>
  \\\\192.168.50.3\\ADMIN$: 
    warning: Couldn't get details for share: NT\_STATUS\_ACCESS\_DENIED
    Anonymous access: <none>
  \\\\192.168.50.3\\C$: 
    warning: Couldn't get details for share: NT\_STATUS\_ACCESS\_DENIED
    Anonymous access: <none>
  \\\\192.168.50.3\\IPC$: 
    warning: Couldn't get details for share: NT\_STATUS\_ACCESS\_DENIED
    Anonymous access: READ 

nbstat 

NetBIOS name: WINXP-VM, NetBIOS user: <unknown>, NetBIOS MAC: 00:0c:29:dd:2f:3f (VMware) 

smb-vuln-ms08-067 

  VULNERABLE:
  Microsoft Windows system vulnerable to remote code execution (MS08-067)
    State: VULNERABLE
    IDs:  CVE:CVE-2008-4250
          The Server service in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2,
          Vista Gold and SP1, Server 2008, and 7 Pre-Beta allows remote attackers to execute arbitrary
          code via a crafted RPC request that triggers the overflow during path canonicalization.
          
    Disclosure date: 2008-10-23
    References:
      https://technet.microsoft.com/en-us/library/security/ms08-067.aspx
      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
 

smb-security-mode 

  account\_used: <blank>
  authentication\_level: user
  challenge\_response: supported
  message\_signing: disabled (dangerous, but default) 

smb-vuln-ms10-054 

false 

samba-vuln-cve-2012-1182 

NT\_STATUS\_ACCESS\_DENIED 

clock-skew 

mean: -30m00s, deviation: 42m25s, median: -1h00m00s 

smb2-time 

Protocol negotiation failed (SMB2) 

smb-vuln-ms10-061 

ERROR: Script execution failed (use -d to debug) 

smb-os-discovery 

  OS: Windows XP (Windows 2000 LAN Manager)
  OS CPE: cpe:/o:microsoft:windows\_xp::-
  Computer name: winxp-vm
  NetBIOS computer name: WINXP-VM\\x00
  Workgroup: DIALOCAN\\x00
  System time: 2024-12-03T16:53:51+01:00
 

  
[Misc Metrics (click to expand)](javascript:toggle('metrics_192.168.50.3');)

Metric

Value

Ping Results

arp-response

Network Distance

1 hops

TCP Sequence Prediction

Difficulty=265 (Good luck!)

IP ID Sequence Generation

Incremental

[Go to top](#top)  
[Toggle Closed Ports](javascript:toggleAll('closed');)  
[Toggle Filtered Ports](javascript:toggleAll('filtered');)