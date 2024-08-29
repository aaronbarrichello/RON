import whois 
import dns.resolver
import requests
from urllib.parse import urlparse

def print_banner():
    print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌
▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌
▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌
▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ 
    """)

def extract_domain(website):
    parsed_url = urlparse(website)
    if parsed_url.scheme:
        return parsed_url.netloc
    return website

def find_dns_info(website):
    try:
        domain = extract_domain(website)
        print(f"DNS information for {domain}:")
        dns_records = dns.resolver.resolve(domain, 'A')
        dns_info = []
        for record in dns_records:
            print("A Record:", record)
            dns_info.append(f"A Record: {record}")
        return dns_info
    except dns.resolver.NoAnswer as e:
        print(f"Error: No DNS information found. {e}")
        return None
    except dns.resolver.NXDOMAIN as e:
        print(f"Error: The domain {website} does not exist. {e}")
        return None
    except Exception as e:
        print(f"An error occurred while fetching DNS information. {e}")
        return None

def show_whois_report(website):
    try:
        domain = extract_domain(website)
        w = whois.whois(domain)
        whois_report = w.text
        print("WHOIS Report:")
        print(whois_report)
        return whois_report
    except Exception as e:
        print(f"Error: Unable to fetch WHOIS information. {e}")
        return None

def check_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print("HTTP Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"Error: Unable to fetch HTTP headers. {e}")

def main():
    print_banner()

    while True:
        features = [
            "1. Find DNS Information",
            "2. Show WHOIS Report",
            "3. Check HTTP Header",
            "4. Exit Program"
        ]

        print("\nSelect a feature to run:")
        for feature in features:
            print(feature)

        choice = input("Enter the number of the feature you want to run: ")

        if choice == "4":
            print("Goodbye!")
            break

        website = input("Enter the website domain : ")

        if choice == "1":
            find_dns_info(website)
        elif choice == "2":
            show_whois_report(website)
        elif choice == "3":
            check_http_headers(website)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
