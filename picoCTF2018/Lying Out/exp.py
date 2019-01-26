from pwn import *

traffic=[
    10900,10800,10850,11000,10800,10750,10800,10850,
    10900,11000,10800,10800,11000,10900,10700,10850,
    10800,10850,11000,11050,10650,10800,10700,11000,
    10900,10950,10950,10800,11000,11100,11900,13400,
    13800,13400,12000,11000,10800,10800,10700,10800,
    10800,11000,10900,11050,11800,13100,14600,16100,
    16600,16400,14400,12800,11800,11000,10950,10800,
    10800,10800,10800,10800,10900,10850,10850,10800,
    10800,11000,11000,11000,11400,11900,13000,14000,
    14800,15800,16200,15800,14700,13700,12200,12100,
    11100,11000,10900,10800,10700,11000,11000,10800,
    10900,10700,10900,10800,10750,10950,10900,10800
]

r=remote('2018shell3.picoctf.com',3693)

r.recvuntil('num_IPs')
info = r.recv().strip()
info = info.split('\n')

ans = []
groups = len(info)
for i in range(groups):
    info[i] = info[i].split()
    t = info[i][2].split(':')

    flow = info[i][3]
    time = int(t[0])*4 + int(t[1])//15

    if int(flow) > traffic[time]:
        ans.append(info[i][0])

r.sendline(' '.join(ans))

print r.recvall()
r.close()