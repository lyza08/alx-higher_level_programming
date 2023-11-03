#!/bin/bash
# Determine the size in bytes of the HTTP response header for a specified URLL.
curl -s "$1" | wc -c
