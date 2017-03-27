#!/bin/bash

# Fetches the object file from the server so we can get the files
hash="${1}";
dir="${hash:0:2}";
file="${hash:2:38}";
mkdir -p ".git/objects/${dir}";
path=".git/objects/${dir}/${file}";
curl -s "http://edge2.web.easyctf.com/${path}" > "${path}";
