#!/bin/bash

ls | grep -o "_[0-9]\+$" | cut -c2- | cut -d "-" -f 1 | paste -sd+ - | bc
