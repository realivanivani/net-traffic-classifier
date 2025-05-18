"""
This script defines a function `parse_http_request` to parse individual HTTP requests from raw text data.

**Function Input:**

- `text`: A string containing the raw HTTP request text.

**Function Output:**

- A dictionary (`request_data`) containing the parsed information about the HTTP request, including:
    - Method (e.g., GET, POST)
    - URL
    - HTTP Version
    - Headers (key-value pairs)
    - Body (if present)

**Logic:**

1. The function splits the input text by double newline (`\n\n`) to separate the request line, headers, and body (if any).
2. It initializes an empty dictionary `request_data` to store the parsed information.
3. It parses the first line (request line) to extract:
    - Method (GET, POST, etc.)
    - URL
    - HTTP Version (e.g., HTTP/1.1)
    - These are stored in the corresponding keys of `request_data`.
4. It iterates through the remaining lines in the first part (headers) and splits each line by colon (':') to:
    - Extract the header key and value.
    - Store them in `request_data` using the header key as the dictionary key.
5. If there are more than one part after splitting by double newline, it indicates a body section.
    - The body content is stored in the `Body` key of `request_data`.
    - If no body is present, an empty string is assigned to the `Body` key.
6. Finally, the function returns the `request_data` dictionary containing the parsed HTTP request information.

"""

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
