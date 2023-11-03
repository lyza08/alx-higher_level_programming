#!/bin/bash
# Show the list of HTTP methods that the server for a specified URL supports.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
