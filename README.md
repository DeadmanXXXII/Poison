# Poison-
This repo will consist of poisoned PDF, images, documents and pictures like those used by the North Korean APT's

### File: poison_image.svg
This is a basic example PoC of a svg image that forces a .txt download but is recognized by a server as a harmless blue blue square 🟦 like this one.
The .txt file in particular just states

```
You clicked my poison picture from while I was bug hunting.
This is harmless, it just forces this download of this.
Built by: DeadmanXXXII
```


The fact that you are able to read this means it worked and your server processes .svg as much as this format like .pdf is highly recognized for simplicity of business functions.
It's extremely dangerous.
.txt .png only in a secure environment 
.txt only in zero trust as you can re appendage later.

#### Why?

Simply because that could be disruption s+d.py in base64 and if you allow creation in your system as you haven't banned them and your cron policies are bad. You have about 3mins to check your last backup time and find that script, without responding to the request and packet floods thinking you are being Ddos'd when it activates before it erases upto 75% of all records on the device its managed to get hold of. By ten minutes if you haven't got a backup I hope your paper records are good.

This was a 🟦 and is now an actual picture to seem less conspicuous.


![Usage](https://raw.githubusercontent.com/DeadmanXXXII/Poison/main/Nethinter-use-evidence.png)


### File: mal.csv

Description: This file is a Proof-of-Concept for a CSV Injection (Formula Injection) vulnerability. It contains specially crafted spreadsheet formulas designed to demonstrate two potential attack vectors:

Data Exfiltration/External Interaction: The =HYPERLINK formula attempts to force an outbound HTTP/S request to a controlled external server (https://deadmanxxxii.requestcatcher.com/log). This proves that arbitrary external connections can be initiated from the victim's spreadsheet, allowing for potential data exfiltration or redirection to phishing sites.
Web Service Interaction: The =WEBSERVICE formula attempts to fetch data from an external URL, similarly confirming external connectivity and potential data leakage or interaction with attacker-controlled web services.

### File: malicious.csv

Description: This file is a Proof-of-Concept for a CSV Injection (Formula Injection) vulnerability, focusing on internal formula execution and client-side command execution. It contains two primary malicious formulas:

Basic Formula Execution: The =2+2 formula demonstrates that the spreadsheet program is indeed interpreting and executing injected formulas, serving as a foundational test.
Client-Side Command Execution (DDE): The =CMD|' /C calc'!A0 formula attempts to execute an operating system command (specifically, opening the calculator on a Windows machine) via Dynamic Data Exchange (DDE). While modern spreadsheet programs often display security warnings for DDE, its attempted execution proves the potential for arbitrary command execution on the client's system.
