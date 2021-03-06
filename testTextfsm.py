import textfsm
template = "templates/juniper_junos_show_lldp_neighbors_interface.textfsm"
raw_text_data = "tests/alcatel_sros/show_lldp_neighbor-match/alcatel_sros_show_lldp_neighbor-match.raw"
re_table = textfsm.TextFSM(open(template))
data = re_table.ParseText("""LLDP Neighbor Information:
Local Information:
Index: 1 Time to live: 120 Time mark: Thu Nov 26 06:41:24 2015 Age: 1 secs
Local Interface    : ge-0/0/8
Parent Interface   : -
Local Port ID      : 518
Ageout Count       : 0

Neighbour Information:
Chassis type       : Mac address
Chassis ID         : 88:e0:f3:1f:14:e0
Port type          : Locally assigned
Port ID            : 880
Port description   : ge-0/0/8
System name        : bng-nw6moj.juniper.net

System Description : Juniper Networks, Inc. ex4300-24p Ethernet Switch, kernel JUNOS 14.1I20151125_0548_rajjs, Build date: 2015-11-25 06:06:58 UTC Copyright (c) 1996-2015 Juniper Networks, Inc.

System capabilities
        Supported: Bridge Router
        Enabled  : Bridge Router

Management address
        Address Type      : IPv4(1)
        Address           : 10.204.39.232
        Interface Number  : 33
        Interface Subtype : ifIndex(2)
        OID               : 1.3.6.1.2.1.31.1.1.1.1.33.
Media endpoint class: Network Connectivity""")

# Display result as CSV
# First the column headers
print( ', '.join(re_table.header) )
# Each row of the table.
for row in data:
  print( ', '.join(row) )
print(data)