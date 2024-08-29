import json
import msoffcrypto
import pandas as pd
from io import BytesIO
from tkinter import messagebox
import sys  # Import sys to use sys.exit()

def load_config():
    """Load configuration from a JSON file."""
    with open('config.json') as f:
        return json.load(f)

def is_password_protected(file_path, password):
    """Check if the file is password-protected."""
    try:
        decrypted_file = BytesIO()
        with open(file_path, 'rb') as file:
            office_file = msoffcrypto.OfficeFile(file)
            office_file.load_key(password=password)
            office_file.decrypt(decrypted_file)
        decrypted_file.seek(0)
        # Attempt to read the decrypted file
        pd.read_excel(decrypted_file, engine='openpyxl')
        return True
    except Exception as e:
        # Show error message and close the application
        messagebox.showerror("Error", f"Password check failed: {e}")
        sys.exit()  # Exit the application
        return False  # This line will not be reached due to sys.exit()

def read_protected_excel(file_path, password, sheet_name):
    """Read a password-protected Excel file and return a specific sheet."""
    decrypted_file = BytesIO()
    try:
        with open(file_path, 'rb') as file:
            office_file = msoffcrypto.OfficeFile(file)
            office_file.load_key(password=password)
            office_file.decrypt(decrypted_file)
        decrypted_file.seek(0)
        return pd.read_excel(decrypted_file, engine='openpyxl', sheet_name=sheet_name)
    except Exception as e:
        raise ValueError(f"An error occurred while reading the Excel file: {e}")

def getDataFile(sheetname):
    """Get data from a specific sheet in a password-protected Excel file."""
    filename = 'data/general.xlsx'
    config = load_config()
    password = config.get('password', None)
    
    if password is None:
        messagebox.showerror("Error", "Password is not set in the configuration file 'config.json'.")
        sys.exit()  # Exit the application

    # Check if the file is password-protected
    if not is_password_protected(filename, password):
        messagebox.showerror("Error", "The file is not password-protected or the password is incorrect.")
        sys.exit()  # Exit the application
    
    try:
        df = read_protected_excel(filename, password, sheetname)
        return df
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")
        return None

def writeFile(sheetname, header, data):
    """Write data to a specific sheet in a password-protected Excel file."""
    filename = 'data/general.xlsx'
    config = load_config()
    password = config.get('password', None)
    
    if password is None:
        messagebox.showerror("Error", "Password is not set in the configuration file.")
        sys.exit()  # Exit the application

    if not is_password_protected(filename, password):
        messagebox.showerror("Error", "The file is not password-protected or the password is incorrect.")
        sys.exit()  # Exit the application

    df = pd.DataFrame([data], columns=header)

    try:
        existing_df = getDataFile(sheetname)
        if existing_df is not None:
            df = pd.concat([existing_df, df], ignore_index=True)
    except ValueError:
        pass

    try:
        with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=sheetname, index=False)
    except FileNotFoundError:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheetname, index=False)

    return True