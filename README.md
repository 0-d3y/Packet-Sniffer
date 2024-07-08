# Packet Sniffer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)
[![GitHub issues](https://img.shields.io/github/issues/0-d3y/Packet-Sniffer)](https://github.com/0-d3y/Packet-Sniffer/issues)
[![GitHub stars](https://img.shields.io/github/stars/0-d3y/Packet-Sniffer)](https://github.com/0-d3y/Packet-Sniffer/stargazers)


## Dev: @i_0d3y

Packet Sniffer is a simple and open-source tool for sniffing network packets and displaying their details in a well-formatted and colored manner. The tool is developed using the `Scapy` library for packet sniffing and `pyfiglet` and `termcolor` libraries for enhancing the user interface with a logo display and text coloring.

## Requirements

Before you can use this tool, you need to install the following dependencies:

1. Python 3
2. The following Python libraries:
    - scapy
    - pyfiglet
    - termcolor

You can install the dependencies using pip:

```bash
pip install scapy pyfiglet termcolor
```
### Usage
To use the Packet Sniffer tool, follow these steps:

Ensure you have installed the above requirements.

```bash
git clone https://github.com/0-d3y/Packet-Sniffer.git
cd Packet-Sniffer
python main.py
```

You will see the Packet Sniffer logo displayed in a beautiful, colored format, and the tool will start sniffing packets and displaying their details. To stop sniffing packets, press Ctrl+C.

### Notes
You may need to run the tool with administrator privileges on some systems to ensure the ability to sniff packets.
The tool is designed for educational and experimental purposes. It is advised not to use it on unauthorized networks.
Contribution
Contributions to improve the tool are welcome. You can submit pull requests or open issues on the project's GitHub repository.
