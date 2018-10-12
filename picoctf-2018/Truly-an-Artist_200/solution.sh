#!/bin/bash

strings 2018.png | grep pico

# The problem description suggests that the flag is in the image metadata, which is plaintext
# We could use a tool like exiftool, or we can just use strings
# picoCTF{look_in_image_13509d38}
