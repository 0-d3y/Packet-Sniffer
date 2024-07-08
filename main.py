# Telegram:  @i_0d3y
# Instagram : cyber_77k



from scapy.all import sniff
import pyfiglet
from termcolor import colored

def display_logo():
    logo_text = pyfiglet.figlet_format("Packet Sniffer", font="slant")
    colored_logo = colored(logo_text, color="green")
    print(colored_logo + "\n                        insta: cyber_77k")

def print_packet(packet):
    print(f"\n======== Packet ========")
    print(colored(packet.summary(), "cyan"))

def sniff_packets():
    print(colored("\nSniffing packets... Press Ctrl+C to stop.\n", "yellow"))
    try:
        sniff(prn=print_packet)  
    except KeyboardInterrupt:
        print(colored("\nStopped sniffing.", "red"))

if __name__ == "__main__":
    display_logo()
    sniff_packets()
