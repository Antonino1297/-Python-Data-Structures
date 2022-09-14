fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    for value in line.split():
        if value not in lst:
            lst.append(value)

lst.sort()
print(lst)