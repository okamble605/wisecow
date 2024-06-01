#!/bin/bash

# URL to check
URL="https://majhinaukri.in/"

# Function to check application health
check_application_health() {
    HTTP_RESPONSE=$(curl --write-out "%{http_code}" --silent --output /dev/null "$URL")

    if [ "$HTTP_RESPONSE" -eq 200 ]; then
        echo "Application is up"
    else
        echo "Application is down. HTTP Status Code: $HTTP_RESPONSE"
    fi
}

# Main script
check_application_health
