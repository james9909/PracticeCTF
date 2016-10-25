#!/bin/bash
counter=0

while true; do
    onemore=$(expr $counter + 1)
    output=$(sh mystery.$counter)
    if [[ $output =~ "flag" ]]; then
        echo $output
        break
    fi
    output=$(sh mystery.$counter | rev | cut -c 7- | rev | tee mystery.$onemore)
    ((counter++))
    echo Output: $output
    if [[ $output =~ "flag" ]]; then
       break
    fi
done
