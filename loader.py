# loader.py
# Reads the leads CSV and returns a list of dictionaries
# Each dictionary = one lead's data

import pandas as pd

def load_leads(filepath: str) -> list[dict]:
    """
    Reads leads.csv and returns list of lead dicts.
    Expected columns: name, company, industry, linkedin_url
    """
    df = pd.read_csv(filepath)
    
    # Fill any empty cells with "Unknown" to avoid errors
    df = df.fillna("Unknown")
    
    # Convert each row to a dictionary
    leads = df.to_dict(orient="records")
    print(f"✅ Loaded {len(leads)} leads from {filepath}")
    return leads