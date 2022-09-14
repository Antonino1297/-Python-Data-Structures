fname = input("Enter file name: ")
fh = open(fname)
count = 0
y = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    l = line.find("0")
    x = float(line[1:])
    y = y + x
    avg = y / count

print("Average spam confidence:", avg)