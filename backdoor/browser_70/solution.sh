#!/bin/bash

curl http://hack.bckdr.in/BRWSR/ -A "User-Agent: SDSLabs"

# The web page tells us that we need to view the web page using an SDS browser. Those don't exist, but we can
# assume that the web page is just checking to see if our user agent contains "SDSLabs". Luckily, we can use curl
# to spoof our user agent, giving us the flag:

# e77aec24943bb31c63547812d1130c67d0e7e941bf5d85bfef0492cc68050aef</div>
