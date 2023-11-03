#!/bin/bash
# A Bash script that sends an HTTP POST request to a specified URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
