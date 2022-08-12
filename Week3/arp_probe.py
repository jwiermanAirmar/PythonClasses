# -*- coding: utf-8 -*-
"""
winnetpy is a collection of functions used for networking diagnostics on Windows-based systems.
"""

import subprocess


def arp_probe(verbose=False) -> list[dict[str:str]]:
    """Gets current ARP entries by interrogating the current protocol data for this machine. If more than one network interface uses ARP, entries for each ARP table are retrieved.
    
    verbose: Displays current ARP entries in verbose mode.  All invalid entries and entries on the loop-back interface will be shown."""
    # Base command to send
    cmd = "arp -a"
    # If verpose, append a space and our verbose flag of -v
    if verbose:
        cmd += " -v"
    # Run command and decode results to UTF8.
    response = subprocess.check_output(
        cmd, shell=True, stderr=subprocess.STDOUT
    ).decode()
    # Split our output string into each line by splitting on CR/LF (\r\n).
    lines = response.split("\r\n")
    # Variable to keep track of when our connection interface changes.
    current_interface = ""
    # Initialize a list of our arp probe results.
    arp_results = []
    # For every line in our list of lines:
    for line in lines:
        # If we find the exact word "Interface" in our line, the interface changed.
        if "Interface" in line:
            # Strip leading and trailing whitespace, split into list on whitespace.
            line_chunks = line.strip().split()
            # Index 1 of our new list is going to be the interface.
            current_interface = line_chunks[1]
        # If our line contains "dynamic", "static", or "invalid, it's a valid arp entry.
        if "dynamic" in line or "static" in line or "invalid" in line:
            # Strip leading and trailing whitespace, split on whitespace
            line_chunks = line.strip().split()
            # If the length of line_chunks is 2, the mac address is blank.
            if len(line_chunks) == 2:
                # Build a line entry dict, set mac to be null.
                line_entry = {
                    "interface": current_interface,
                    "mac": "",
                    "ipv4": line_chunks[0],
                    "type": line_chunks[1],
                }
            # Mac address exists! Build a line entry dict of respective chunks.
            else:
                line_entry = {
                    "interface": current_interface,
                    "mac": line_chunks[1],
                    "ipv4": line_chunks[0],
                    "type": line_chunks[2],
                }
            # Append our line_entry dict into our arp_results list.
            arp_results.append(line_entry)
    # After results parsing is done, return list of arp_results.
    return arp_results


print(arp_probe(verbose=True))
