name = input("Enter file:")
hours = list()
full = dict()
count = 0
lll = list()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.split()
    if 'From' in line:
        time = line[5]
        time = time.split(':')
        hours.append(time[0])
for number in hours:
    full[number] = full.get(number, 0) + 1
for k, v in full.items():
    a = (k, v)
    lll.append(a)
c = sorted(lll)
for k, v in c:
    print(k, v)