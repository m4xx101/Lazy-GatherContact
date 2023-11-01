from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import re

def gather_contacts(company):
    browser = webdriver.Chrome()
    browser.get('https://www.google.com')
    time.sleep(1)
    search_box = browser.find_element(By.NAME, 'q')
    search_box.send_keys(f'site:linkedin.com/in/ AND {company}')
    search_box.submit()
    time.sleep(2)

    print("Scroll through all the results and press Enter when done...")
    input()

    results = browser.find_elements(By.CSS_SELECTOR, "h3")
    names_with_designation = []
    for result in results:
        data = result.text.split('-')
        if len(data) > 1 and company.lower() in data[-1].lower():
            full_name_and_designation = data[0].strip()
            names_with_designation.append(full_name_and_designation)

    browser.close()
    return names_with_designation

def create_emails(names_with_designation, domain_name, format_option):
    emails = []

    format_options = {
        1: lambda first, last: f"{first[0]}{last}@{domain_name}",
        2: lambda first, last: f"{first}.{last}@{domain_name}",
        3: lambda first, last: f"{last}{first[0]}@{domain_name}",
        4: lambda first, last: f"{first}{last[0]}@{domain_name}",
    }

    for name_with_designation in names_with_designation:
        parts = name_with_designation.split()
        first_name = re.sub(r'[^a-zA-Z]', '', parts[0]).lower()
        last_name = re.sub(r'[^a-zA-Z]', '', parts[1]).lower()

        emails.append(format_options[format_option](first_name, last_name))

    return emails

def main():
    company = input("Enter the company name for Google dork query: ")
    domain = input(f"Enter the domain (e.g. company.com) for {company}: ")
    output_directory = input("Enter the output directory: ")

    names_with_designation = gather_contacts(company)

    print("\nSelect email format:")
    print("1. f.l@domain")
    print("2. firstname.lastname@domain")
    print("3. l.f@domain")
    print("4. firstname.l@domain")
    email_format = int(input("Enter choice (default is 1): ") or 1)

    emails = create_emails(names_with_designation, domain, email_format)

    date_time = time.strftime("%Y%m%d-%H%M%S")
    output_file = os.path.join(output_directory, f"{domain}-{date_time}-emails.txt")
    with open(output_file, 'w') as f:
        f.write("\n".join(emails))

    names_file = os.path.join(output_directory, f"{domain}-{date_time}-names.txt")
    with open(names_file, 'w') as f:
        f.write("\n".join(names_with_designation))

    print(f"\n{len(emails)} emails saved to: {output_file}")
    print(f"Names saved to: {names_file}")
    print(f"\nScript executed on {date_time}.")
    print("End of script execution.")

if __name__ == "__main__":
    main()
