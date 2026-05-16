# main.py
# Entry point — runs the full pipeline
# Usage: python main.py

from loader import load_leads
from qualifier import qualify_all_leads
from exporter import export_to_excel

# ── CONFIG ───────────────────────────────────────
LEADS_FILE = "leads DATA/leads.csv"

# Change this to match what your client sells
CLIENT_INDUSTRY = "AI automation and lead generation services"
# ─────────────────────────────────────────────────

def main():
    print("🚀 Lead Qualifier Bot — Powered by Gemma 4 (Local)\n")
    
    # Step 1: Load leads
    leads = load_leads(LEADS_FILE)
    
    # Step 2: Qualify each lead
    qualified = qualify_all_leads(leads, CLIENT_INDUSTRY)
    
    # Step 3: Export to Excel
    output = export_to_excel(qualified)
    
    print(f"\n🎯 Done! {len(qualified)} leads qualified.")
    print(f"📊 Open {output} to see results.")

if __name__ == "__main__":
    main()