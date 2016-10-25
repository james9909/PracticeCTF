ebx = 533
eax = 8842
ecx = 16131
if ebx < eax:
    ebx = eax * ebx
    ebx = eax + ebx
    eax = ebx
    eax = eax - ecx
else:
    ebx = eax * ebx
    ebx = eax - ebx
    eax = ebx
    eax = ecx + eax

print eax
