# qualifier.py
# Sends each lead to Gemma 4 running locally via Ollama
# Gets back a score and personalized outreach message

import ollama

def qualify_lead(lead: dict, client_industry: str) -> dict:
    """
    Takes one lead dict, sends to Gemma 4, returns
    the same dict with score and outreach message added.
    """
    
    # Build the prompt
    prompt = f"""
You are a sales qualification expert.

Analyze this lead and respond in exactly this format:
SCORE: [number 1-10]
REASON: [one sentence why]
OUTREACH: [personalized outreach message under 50 words]

Lead details:
- Name: {lead.get('name')}
- Company: {lead.get('company')}
- Industry: {lead.get('industry')}
- LinkedIn: {lead.get('linkedin_url')}

Client sells services to: {client_industry}

Respond only in the format above. Nothing else.
"""

    # Send to Gemma 4 running locally
    response = ollama.chat(
        model="gemma4:e2b",
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response["message"]["content"]
    
    # Parse the response
    score = "N/A"
    reason = "N/A"
    outreach = "N/A"
    
    for line in raw.split("\n"):
        if line.startswith("SCORE:"):
            score = line.replace("SCORE:", "").strip()
        elif line.startswith("REASON:"):
            reason = line.replace("REASON:", "").strip()
        elif line.startswith("OUTREACH:"):
            outreach = line.replace("OUTREACH:", "").strip()
    
    # Add results back to lead dict
    lead["score"] = score
    lead["reason"] = reason
    lead["outreach_message"] = outreach
    
    print(f"  ✅ Qualified: {lead.get('name')} → Score: {score}")
    return lead


def qualify_all_leads(leads: list[dict], client_industry: str) -> list[dict]:
    """
    Loops through all leads and qualifies each one.
    """
    print(f"\n🔍 Qualifying {len(leads)} leads...\n")
    qualified = []
    
    for i, lead in enumerate(leads, start=1):
        print(f"  Processing {i}/{len(leads)}: {lead.get('name')}")
        result = qualify_lead(lead, client_industry)
        qualified.append(result)
    
    return qualified