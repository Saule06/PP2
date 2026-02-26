import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 78)
print(f"{'DN':45} {'Description':15} {'Speed':8} {'MTU'}")
print("-" * 78)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs.get("dn", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

   
    print(f"{dn:45} {'':15} {speed:8} {mtu}")