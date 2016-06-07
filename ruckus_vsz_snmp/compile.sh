#!/bin/sh

set -e

rm -f RUCKUS*.py

smidump -f python -k RFC1155-SMI.txt | libsmi2pysnmp > RFC1155-SMI.py

smidump -f python -k UCD-SNMP-MIB.txt | libsmi2pysnmp > UCD-SNMP-MIB.py

smidump -f python -k RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-ROOT-MIB.py
smidump -f python -k RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-TC-MIB.py
smidump -f python -k RUCKUS-PRODUCTS-MIB.txt -p RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-PRODUCTS-MIB.py

smidump -f python -k RUCKUS-SCG-EVENT-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-SCG-EVENT-MIB.py
smidump -f python -k RUCKUS-SCG-SYSTEM-MIB.txt -p RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-SCG-SYSTEM-MIB.py

smidump -f python -k RUCKUS-SCG-CONFIG-WLAN-MIB.txt -p RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-SCG-CONFIG-WLAN-MIB.py
smidump -f python -k RUCKUS-SCG-WLAN-MIB.txt -p RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-SCG-WLAN-MIB.py
smidump -f python -k RUCKUS-SCG-TTG-MIB.txt -p RUCKUS-TC-MIB.txt -p RUCKUS-ROOT-MIB.txt | libsmi2pysnmp > RUCKUS-SCG-TTG-MIB.py

echo "All done!"

