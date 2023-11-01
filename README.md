# Lazy-GatherContact
An advanced tool that automates the process of gathering potential employee names and designations associated with a company using Google search results. This enhanced version not only retrieves names but also generates potential email addresses based on common formats, offering a more comprehensive approach to OSINT for email enumeration.
Ideal for penetration testers, red teamers, and security researchers aiming for a more efficient and extended recon process.

This script allows you to gather potential names and designations associated with a company from Google search results, and then create potential email addresses based on common email formats.

## Requirements
Before running the script, ensure you have the necessary packages installed:

```
pip install selenium
```

In addition, you need to have the appropriate WebDriver for Selenium to work with your browser. For Chrome, download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/), Ensure you have ChromeDriver downloaded and in your system's PATH.

## Usage
Run the script:
```
python3 lazyGC.py
Enter the company name: EXAMPLE INC
Enter the domain name(e.g., company.com): example.com
Specify the directory where you'd like to save the results: User/Profile/Downloads/
```

After executing the search, you'll be prompted to scroll through the Google search results manually. Once you've scrolled through all results, press Enter in terminal.

Next, select the email format you want:

```
Select email format:
1. flast@domain.com
2. firstname.lastname@domain.com
3. lastf@domain.com
4. firstnamel@domain.com
```
The script will then generate potential email addresses and save them to an output file in the specified directory, along with the names and designations gathered.

## Credits
This script is based on the original [GatherContacts](https://github.com/clr2of8/GatherContacts) tool. The enhancements provide a more user-friendly experience and additional features.
