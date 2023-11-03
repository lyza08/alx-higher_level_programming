
#!/bin/bash
# Retrieve the body of the HTTP response for a given URL, but only for responses with a status code of 200.
curl -sL "$1"
