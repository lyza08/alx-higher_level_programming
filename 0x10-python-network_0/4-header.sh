#!/bin/bash
# GET request to a given URL with a specific header variable, you can specify the header using the appropriate curl option while sending the request.
curl -sH "X-School-User-Id: 98" "$1"
