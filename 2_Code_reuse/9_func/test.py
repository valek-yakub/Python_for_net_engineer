from collections import defaultdict
from pprint import pprint


access =  defaultdict(str)
trunk = defaultdict(list)
all_interfaces = defaultdict(list)

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "duplex auto"
]

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk encapsulation dot1q",
    "switchport trunk allowed vlan ", "duplex auto"
]

mode = {
    "switchport mode access": access_mode_template,
    "switchport mode trunk": trunk_mode_template
}





for intf, commands in all_interfaces.items():
    if





