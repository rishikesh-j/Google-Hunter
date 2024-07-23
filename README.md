# Google Hunter

This tool is designed to automate Google dorking using predefined dorks to identify potential security vulnerabilities, exposed documents, and other sensitive information related to a given target domain.

## Features

- Automates the execution of Google dorks.
- Supports various categories such as General Dorks, Database-Related Dorks, Vulnerability Searches, and more.
- Extracts URLs from Google search results in real-time.
- Filters out duplicate results.
- Customizable dorks with support for target domain substitution.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```sh
pip install requests beautifulsoup4
```

## Usage

1. **Run the Script**: Execute the script and provide the target domain when prompted.

```sh
python google_dorking_tool.py
```

2. **View Results**: The script will output unique URLs found during the dorking process.



## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.
