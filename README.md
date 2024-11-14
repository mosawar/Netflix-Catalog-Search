Here is a refined README file for your Netflix Catalog Checker program, including detailed instructions for setup and running the program:

---

# Netflix Catalog Checker

A Python-based GUI application for checking if a movie, TV show, actor, or director is available on Netflix's catalog. Once a match is found, you can send the information directly to your phone via SMS for future reference.

## Features
- Search for titles, directors, or cast members in the Netflix catalog.
- Sends SMS notifications with the search results using Twilio.
- User-friendly GUI built with Tkinter.

## Prerequisites
1. **Python 3.x** - Ensure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **Twilio Account** - Sign up for an account on [Twilio](https://www.twilio.com/) to get the `Account SID`, `Auth Token`, and a Twilio phone number.
   - Note: You’ll need to verify your phone number in Twilio to receive SMS messages.
3. **Netflix Catalog Data** - The program requires a CSV file containing Netflix's catalog data. Place the `netflix_titles.csv` file in the same directory as this script, or update the path in the code.

## Required Python Libraries
Install the following libraries:
- **Twilio**: To send SMS notifications.
- **Tkinter**: GUI support (comes pre-installed with Python).
- **Requests**: For HTTP requests (if needed in future updates).
- **Pandas**: For CSV data manipulation.

### Installation of Required Libraries
Use the following commands to install the required libraries:
```bash
pip install twilio
pip install pandas
```

## Setup Instructions
1. **Twilio Credentials**:
   - In the script, locate the variables `account_sid`, `auth_token`, and `twilio_number` and replace them with your Twilio account details.

   ```python
   account_sid = 'your_account_sid'
   auth_token = 'your_auth_token'
   twilio_number = 'your_twilio_number'
   ```

2. **Phone Number**:
   - Replace `my_phone_number` with your verified phone number in the following format: `+1234567890`.

3. **CSV File**:
   - Ensure the `netflix_titles.csv` file is downloaded and available in the directory specified by the script, or update the `os.chdir()` path in the code to match the file's location.

## Running the Program
1. **Launch the Program**:
   - Open a terminal or command prompt in the directory containing the script.
   - Run the following command:
     ```bash
     python netflix_catalog_checker.py
     ```
   - This will open the Tkinter GUI window.

2. **Using the Application**:
   - Select the category from the dropdown list (`Title`, `Director`, or `Cast`).
   - Click on **Search**.
   - If the search is successful, you’ll receive a confirmation message in the GUI.
   - Click **Send to Phone** to receive the search result via SMS.

3. **Close the Program**:
   - Click the **Close** button on the main window to exit.

## Troubleshooting
- If you do not receive SMS notifications, ensure your phone number is verified in Twilio.
- Check the directory path to confirm `netflix_titles.csv` is correctly referenced.

---

This README should help you set up, run, and troubleshoot the Netflix Catalog Checker application. Let me know if you have any further questions!
