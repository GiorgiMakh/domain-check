# Domain Check with Whois Library (Python)

## Overview

This Python script allows you to check domain information using the Whois library. You can use it to retrieve details about a domain name, such as its registrar, creation date, expiration date, and more.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x: You can download Python from the official website at https://www.python.org/downloads/.

## Installation

1. Clone this repository to your local machine or download the script directly.
   
   ```
   git clone https://github.com/GiorgiMakh/domain-check.git
   ```

2. Navigate to the project directory.

   ```
   cd domain-check
   ```

3. Install the required Python library, Whois.

   ```
   pip install python-whois
   ```

## Usage

You can use this script to check domain information by providing the domain name as a command-line argument. Here's how to use it:

```
python domain-check.py example.com
```

Replace `example.com` with the domain name you want to check.

## Example

```bash
python domain-check.py google.com
```

Output:

```
Domain Name: google.com
Registrar: MarkMonitor Inc.
Creation Date: 1997-09-15T04:00:00Z
Expiration Date: 2028-09-13T04:00:00Z
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the [python-whois](https://pypi.org/project/python-whois/) library for making domain information retrieval easy.

---

Feel free to customize this README to fit your specific project, and make sure to include any additional information or instructions that might be relevant. The goal is to provide clear and concise guidance to users and potential contributors.
