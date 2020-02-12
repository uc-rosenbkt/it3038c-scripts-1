import os

filename = "/var/log/secure"

with open(filename) as filename:
    lines = set(f.read().splitlines())
    for line in lines:
        if "sayersmx" in line:
            print(line)