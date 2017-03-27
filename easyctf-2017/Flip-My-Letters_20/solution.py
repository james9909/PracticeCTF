alphabet = "abcdefghijklmnopqrstuvwxyz"
sub = alphabet[::-1]

enc = "r_wlmg_vevm_mvvw_zm_zhxrr_gzyov"

dec = ""
for char in enc:
    index = alphabet.find(char)
    if index != -1:
        dec += sub[index]

print "easyctf{%s}" % dec

# easyctf{idontevenneedanasciitable}
