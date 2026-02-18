requests = []

n = int(input("Enter number of requests: "))
i = 0
while i < n:
    value = int(input("Enter request value: "))
    requests = requests + [value]
    i = i + 1

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

valid = 0
removed = 0

for req in requests:
    if req < 0:
        invalid_requests = invalid_requests + [req]
    elif req == 0:
        pass
    elif req >= 1 and req <= 20:
        low_demand = low_demand + [req]
        valid = valid + 1
    elif req >= 21 and req <= 50:
        moderate_demand = moderate_demand + [req]
        valid = valid + 1
    else:
        high_demand = high_demand + [req]
        valid = valid + 1

fullname = "Srinivasa Rao Neelamraju"

name = ""
for ch in fullname:
    if ch != " ":
        name = name + ch

L = 0
for ch in name:
    L = L + 1

PLI = L % 3

if PLI == 0:
    removed = len(low_demand)
    low_demand = []
elif PLI == 1:
    removed = len(high_demand)
    high_demand = []
else:
    removed = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []

print("Length of Name :", L)
print("PLI Value:", PLI)

if PLI == 0:
    print("Applied Rule: Rule A")
elif PLI == 1:
    print("Applied Rule: Rule B")
else:
    print("Applied Rule: Rule C")

print("Total Valid Requests:", valid)
print("Requests Removed Due to PLI:", removed)

print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
