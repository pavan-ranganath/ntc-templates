import textfsm
template = "templates/alcatel_sros_show_lldp_neighbor-match.textfsm"
raw_text_data = "tests/alcatel_sros/show_lldp_neighbor-match/alcatel_sros_show_lldp_neighbor-match.raw"
re_table = textfsm.TextFSM(open(template))
data = re_table.ParseText("""1/1/c4/1      NB    D4:04:FF:68:35:60  13     et-8/1/1        dltyo5-bbisp-gw1
1/1/c4/1      NB    D4:04:FF:68:35:60  13     et-8/1/1        dltyo5-bbisp-gw1""")

# Display result as CSV
# First the column headers
print( ', '.join(re_table.header) )
# Each row of the table.
for row in data:
  print( ', '.join(row) )