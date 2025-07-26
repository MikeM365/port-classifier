# Port Classifier

A simple command-line Python utility to classify a port number as "secure" or "not secure" based on standard networking conventions.

## How It Works

This tool operates on a simple and widely recognized principle in networking:

-   **Ports 0-1023** are known as "Well-Known Ports" or "Privileged Ports." They are reserved for standard services (like HTTP on port 80, or SSH on port 22) and typically require special administrative permissions to be used by an application.
-   **Ports 1024 and above** are "Registered" or "Dynamic" ports, which are generally available for any application to use.

This script classifies any port greater than 1024 as "secure" (i.e., not a privileged port) and any port 1024 or below as "not secure." **All analysis is done locally; no network connection is made.**

## Features

-   **100% Offline:** Classifies port numbers using a logical rule, without any network traffic.
-   **Educational:** A great tool for understanding the concept of privileged vs. unprivileged network ports.
-   **Zero Dependencies:** Runs using only standard Python, requiring no extra installation.
-   **Clear Output:** Provides simple, easy-to-understand feedback for a list of predefined ports.

## Usage

The script is pre-configured to check a list of common ports. To run it:

1.  Clone or download the repository.
2.  Navigate to the `port-classifier` directory.
3.  Run the script from your terminal:
    ```bash
    python port_checker.py
    ```

**Sample Output:**
--- Running Port Security Classification ---
Port 1025 is secure
Port 80 is not secure
Port 443 is not secure
Port 22 is not secure
...
