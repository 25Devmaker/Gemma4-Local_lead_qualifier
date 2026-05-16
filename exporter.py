# exporter.py
# Takes qualified leads and writes them to Excel
# Output is clean and ready to hand to a client

import pandas as pd
from datetime import datetime

def export_to_excel(leads: list[dict], output_path: str = None):
    """
    Exports qualified leads to a formatted Excel file.
    Auto-generates filename with timestamp if none given.
    """
    
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"qualified_leads_{timestamp}.xlsx"
    
    df = pd.DataFrame(leads)
    
    # Reorder columns for clean output
    columns = ["name", "company", "industry", 
               "linkedin_url", "score", 
               "reason", "outreach_message"]
    
    # Only keep columns that exist
    columns = [c for c in columns if c in df.columns]
    df = df[columns]
    
    # Write to Excel with formatting
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Qualified Leads")
        
        # Auto-adjust column widths
        worksheet = writer.sheets["Qualified Leads"]
        for col in worksheet.columns:
            max_len = max(len(str(cell.value or "")) 
                         for cell in col) + 5
            worksheet.column_dimensions[
                col[0].column_letter].width = min(max_len, 60)
    
    print(f"\n✅ Exported to: {output_path}")
    return output_path