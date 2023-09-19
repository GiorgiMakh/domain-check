import whois
import sys

def check_domain_info(domain_name):
    try:
        # Use the python-whois library to fetch domain information
        domain_info = whois.whois(domain_name)

        # Print the domain information
        print(f"Domain Name: {domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")

    except whois.parser.PywhoisError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python domain-check.py <domain_name>")
        sys.exit(1)

    domain_name = sys.argv[1]
    check_domain_info(domain_name)
