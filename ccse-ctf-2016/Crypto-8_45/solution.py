enc = "10-21-19-20-12-9-11-5-9-14-7-18-1-4-5-19-3-8-15-15-12".split("-")

flag = ""
for char in enc:
    flag += chr(int(char) + 96)

print flag

# justlikeingradeschool
