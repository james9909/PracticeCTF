#!/bin/bash

url="http://tunnel.web.easyctf.com/images/DaicO7460493nYSuvLPW.png"
while :; do
    response=$(curl -s $url > qr.png)
    contents=$(zbarimg qr.png)
    if ! echo "$contents" | grep "easyctf{" > /dev/null; then
        url=$(echo "$contents" | sed "s/QR-Code://g")
        url="http://tunnel.web.easyctf.com/images/${url}.png"
        echo "Going to $url"
    else
        echo "Got the flag!"
        echo "$contents"
        break
    fi
done

# easyctf{y0u_sh0uld_b3_t1r3d_tr4v3ll1ng_all_th1s_w4y!!!!!}
