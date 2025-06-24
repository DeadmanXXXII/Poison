# Poison-
This repo will consist of poisoned PDF, images, documents and pictures like those used by the North Korean APT's

## New additions due to new findings:

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


### File: create_zip_bomb.py

Description: This Python script is a utility designed to generate a "zip bomb" file. A zip bomb (also known as a "decompression bomb") is a malicious archive that is very small in compressed size but expands to an extremely large uncompressed size when extracted. This property makes them dangerous for causing Denial of Service (DoS) attacks by exhausting a target system's disk space, memory, or CPU resources during decompression.

Functionality:
The script works by leveraging recursive compression:

Initial Dummy File: It first creates a highly compressible dummy file (e.g., filled with null bytes) of a specified size.
Layered Compression: It then iteratively compresses the previously created zip file into a new zip file for a specified number of "layers." This process, though simple, leads to an exponential increase in the theoretical uncompressed size with each added layer. The zipfile.ZIP_STORED method is used in the recursive steps to ensure the internal zip files are stored without re-compression, making the expansion effect dramatic.
Output: The final result is a small .zip file (e.g., dangerous_bomb.zip) that, when extracted by a target system, can expand to gigabytes or even terabytes, depending on the configured initial file size and number of layers.
Usage/Parameters:
The script's main function create_zip_bomb takes three key arguments:

initial_file_size_mb: The size (in megabytes) of the initial highly compressible dummy file.
num_layers: The number of times the recursive zipping process is performed. Each layer effectively multiplies the potential uncompressed size.
output_filename: The desired name for the generated zip bomb file (defaults to dangerous_bomb.zip).
Security Context & Purpose (PoC):
This script is intended as a Proof of Concept (PoC) tool for cybersecurity professionals to demonstrate the severe impact of file upload vulnerabilities, specifically Denial of Service through resource exhaustion. By generating a zip bomb, researchers can test a target application's resilience against such attacks, identifying weaknesses in:

File size limits (both compressed and uncompressed).
Decompression safeguards (e.g., sandboxing, memory/CPU limits for file processing).
Error handling and logging during unexpected resource consumption.
Example Configuration (as per the script):
The if __name__ == "__main__": block provides commented-out examples to generate zip bombs of varying uncompressed sizes. For instance, initial_mb = 100 and layers = 100 can create a zip bomb estimated to expand to approximately 100 GB.

Caution: This tool generates files that can cause significant disruption. It should only be used in controlled environments, with explicit authorization, and strictly within the scope of responsible disclosure or bug bounty programs.

### dangerous_bomb.zip

This is an output of the above script with parameters 2GBs and 20 Layers.

![Usage](https://raw.githubusercontent.com/DeadmanXXXII/Poison/main/Screenshot_20250624-223040.png)



### malicious.mp4

This is a special crafted mp4 with an ffyp atom bomb. Its initial state of size is 74kb a small file with 128 mb dump. This can be increased quite drastically.


### test.sql


This is an osquery rule to check for RCE.
-- Description: This Osquery rule is a Proof of Concept (PoC) for Remote Code Execution.
-- It attempts to use the 'system()' table to execute an external command.
-- Successful execution will result in an HTTP callback to the specified Request Catcher URL,
-- proving the 'system' table is enabled and exploitable.

-- This rule is designed to run once and report its findings.

