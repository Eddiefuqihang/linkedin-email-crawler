# LinkedIn First-degree Connection Email Crawler

This tool allows you to extract email addresses from your LinkedIn first-degree connections.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a LinkedIn account
* You have exported your LinkedIn connections to a CSV file
* You have Python 3.x installed on your machine
* You have Chrome browser installed

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/eddiefuqihang/linkedin-email-crawler.git
   cd linkedin-email-crawler
   ```

2. Set up the environment:
   ```
   source ./setup.sh
   ```

## Usage

1. Export your LinkedIn connections:
   - Follow the instructions in this article: https://www.linkedin.com/help/linkedin/answer/a566336/export-connections-from-linkedin
   - Download the `Connections.csv` file

2. Place the `Connections.csv` file in the same directory as `myprogram.py`

3. Run the program from the command line:
   ```
   python myprogram.py your_linkedin_email your_linkedin_password
   ```

Replace `your_linkedin_email` and `your_linkedin_password` with your actual LinkedIn credentials.

## Note

This tool is for educational purposes only. Please respect LinkedIn's terms of service and others' privacy when using this tool.

## License

This project uses the MIT License. See the [LICENSE](LICENSE) file for details.
