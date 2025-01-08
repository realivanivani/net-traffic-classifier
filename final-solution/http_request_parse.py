import os
import re
import pandas as pd

# Function to parse HTTP requests from a text block
def http_request_parse(text):
    # Split by double newline to separate headers and body
    parts = text.strip().split('\n\n')
    
    # Initialize dictionary for storing parsed data
    request_data = {}

    # Extract the request line (first line)
    request_line = parts[0].splitlines()[0]
    method, url, http_version = request_line.split(' ', 2)
    request_data['Method'] = method
    request_data['URL'] = url
    request_data['HTTP_Version'] = http_version

    # Extract headers (remaining lines in the first part)
    headers = parts[0].splitlines()[1:]
    for header in headers:
        key, value = header.split(': ', 1)
        request_data[key] = value

    # Extract the body if it exists
    if len(parts) > 1:
        request_data['Body'] = parts[1]
    else:
        request_data['Body'] = ''

    return request_data
