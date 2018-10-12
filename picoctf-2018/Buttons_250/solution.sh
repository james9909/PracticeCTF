#!/bin/bash

curl 2018shell3.picoctf.com:21579/button2.php --data ""

# The difference between the two buttons is that the first one is a form, and the second one is a direct link
# to the next page. All we need to do is send a POST request to the second button page to get the flag

# Well done, your flag is: picoCTF{button_button_whose_got_the_button_ed306c10
