
#!/bin/bash
#  Send a POST request in JSON format to a specified URL using a specified JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
