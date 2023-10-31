f = open("testar.txt")
fd = f.readlines()
d = 1
ptp = 0
print(d)
if fd[0].find('00:00:00') == 0:
    d = 0
for i in fd:
    i = i.replace("\n", "")
    i = i.replace("\r", "")
    print(i)
    t = i.split(':')
    #print(t[0])
    #print(t[1])
    #print(t[2])
    ptc = int(t[0])*3600+int(t[1])*60+int(t[2])
    if ptc<=ptp:
        d = d+1
        ptp = ptc
        #print(d)

print(d)


