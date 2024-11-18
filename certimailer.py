import yagmail  # to send emails
import pandas as pd  # to analyze CSV files
import os  # to check if credential file exists

# File to store credentials
cred_file = "cred.txt"

# Function to save credentials
def save_credentials(email, app_password):
    with open(cred_file, "w") as file:
        file.write(f"{email}\n{app_password}")
    print("Credentials saved successfully!")

# Function to load credentials
def load_credentials():
    if os.path.exists(cred_file):
        with open(cred_file, "r") as file:
            lines = file.readlines()
            email = lines[0].strip()
            app_password = lines[1].strip()
            return email, app_password
    else:
        return None, None

# Check if credentials already exist
sender_email, app_password = load_credentials()

if not sender_email or not app_password:
    # Ask user for email and app password if not stored
    sender_email = input("Enter your email: ")
    app_password = input("Enter your app password: ")
    save_credentials(sender_email, app_password)

# Initialize Yagmail
yag = yagmail.SMTP(sender_email, app_password)

# Load participant data
data = pd.read_csv("participants.csv")  # Columns: Name, Email

# Send emails
for index, row in data.iterrows():
    name = row["Name"]
    recipient_email = row["Email"]
    attachment_path = f"output/{name}_certificate.png"  # Make sure you've mentioned the right path

    # Email content
    subject = "Your Participation Certificate"
    body = f"Dear {name},\n\nThank you for participating! Please find your certificate attached."

    yag.send(to=recipient_email, subject=subject, contents=body, attachments=attachment_path)
    print(f"Email sent to {recipient_email}")

