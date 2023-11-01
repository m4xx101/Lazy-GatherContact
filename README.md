# Lazy-GatherContact
An advanced tool that automates the process of gathering potential employee names and designations associated with a company using Google search results. This enhanced version not only retrieves names but also generates potential email addresses based on common formats, offering a more comprehensive approach to OSINT for email enumeration.
Ideal for penetration testers, red teamers, and security researchers aiming for a more efficient and extended recon process.

This script allows you to gather potential names and designations associated with a company from Google search results, and then create potential email addresses based on common email formats.

## Requirements
Before running the script, ensure you have the necessary packages installed:

```
pip install selenium
```

In addition, you need to have the appropriate WebDriver for Selenium to work with your browser. For Chrome, download the ChromeDriver from here.

## Usage
Run the script:
```
python3 improved-gathercontact.py
Enter the company name for the Google dork query: EXAMPLE
Enter the domain of the company (e.g., company.com):example.com
Specify the directory where you'd like to save the results: User/Profile/Downloads/
```

After executing the search, you'll be prompted to scroll through the Google search results manually. Once you've scrolled through all results, press Enter in terminal.

Next, select the email format you want:

```
Select email format:
1. f.l@domain
2. firstname.lastname@domain
3. l.f@domain
4. firstname.l@domain
```
The script will then generate potential email addresses and save them to an output file in the specified directory, along with the names and designations gathered.

Example
For a company named "NetSPI" with the domain "netspi.com", the script might generate emails such as:
```
a.shilts@netspi.com
Based on the Google search result:
```
Aaron Shilts - President and CEO - NetSPI
Output
The script will save the emails to a file named like netspi.com-YYYYMMDD-HHMMSS-emails.txt and the names with designations to a file named like netspi.com-YYYYMMDD-HHMMSS-names.txt.
