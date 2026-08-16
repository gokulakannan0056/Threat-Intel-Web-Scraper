# Simple Web Scraper for Threat Intel

## Overview

This project is a simple **Python-based Web Scraper for Threat Intelligence** developed for cybersecurity learning and educational purposes.

The program collects publicly available cybersecurity advisory information from the CISA website and displays the advisory titles and links.

## Objectives

* Understand the basics of web scraping.
* Learn how to collect publicly available cybersecurity information.
* Practice Python HTTP requests.
* Learn how to parse HTML using BeautifulSoup.
* Understand how threat intelligence information can be gathered from public sources.

## Technologies Used

* **Python**
* **Requests** – used to send HTTP requests.
* **BeautifulSoup** – used to parse HTML content.
* **datetime** – used to display the collection time.

## Features

* Connects to a public cybersecurity advisory page.
* Retrieves webpage content.
* Extracts advisory titles and links.
* Displays up to 10 collected entries.
* Displays the source and collection timestamp.
* Handles connection errors.

## How It Works

```text
Public CISA Advisory Page
          ↓
      HTTP Request
          ↓
      HTML Response
          ↓
     BeautifulSoup
          ↓
Extract Titles and Links
          ↓
 Threat Intelligence Output
```

## Installation

Make sure Python 3 is installed.

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## How to Run

Run the following command:

```bash
python threat_intel_scraper.py
```

The program will retrieve publicly available cybersecurity advisory information and display the results in the terminal.

## Example Output

```text
============================================================
SIMPLE THREAT INTELLIGENCE WEB SCRAPER
============================================================
Source: https://www.cisa.gov/news-events/cybersecurity-advisories
Time: 2026-08-16 10:30:00
============================================================

Title: Example Cybersecurity Advisory
Link: https://www.cisa.gov/...

============================================================
Collected 10 entries.
============================================================
```

The actual results may change because the source website is updated regularly.

## Project Structure

```text
Threat-Intel-Web-Scraper/
├── README.md
└── threat_intel_scraper.py
```

## Security and Ethical Considerations

This project is intended for **educational purposes and authorized security research**.

The scraper is designed to access publicly available information. It should not be used to bypass authentication, access restricted information, or overload websites with excessive requests.

Always respect the target website's terms of use and applicable policies.

## Future Improvements

* Store collected advisories in a CSV file.
* Add keyword-based threat filtering.
* Add automatic duplicate detection.
* Add a simple graphical interface.
* Add scheduled collection of new advisories.
* Add basic threat-intelligence categorization.

## Disclaimer

This project is created for cybersecurity education and authorized research purposes. It should only be used with publicly accessible information and in accordance with applicable rules and website policies.
