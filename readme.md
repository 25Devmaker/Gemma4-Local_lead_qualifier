# 🤖 Local Lead Qualifier Bot
> Powered by Gemma 4 (local) — Zero API costs. Fully private.

## What it does
Qualifies sales leads using Google's Gemma 4 model running 
locally on your machine. No cloud API. No data leaves your laptop.

Send a lead's details to Telegram → get a qualification 
score + personalized outreach message instantly.

## Demo
1. Open Telegram → search your bot
2. Send /start
3. Fill in lead details step by step
4. Get score + outreach message in seconds

## Tech Stack
- Google Gemma 4 E2B (local inference)
- Ollama (model runner)
- Python
- python-telegram-bot
- Runs 100% offline after setup

## Setup

### 1. Install Ollama
Download from https://ollama.com and install.

### 2. Pull Gemma 4
```bash
ollama pull gemma4:e2b
```

### 3. Clone the repo
```bash
git clone https://github.com/25Devmaker/local-lead-qualifier
cd local-lead-qualifier
```

### 4. Install dependencies
```bash
pip install python-telegram-bot ollama
```

### 5. Add your Telegram bot token
Open app.py and replace:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```
Create a bot via @BotFather on Telegram to get your token.

### 6. Run
```bash
python app.py
```

## Project Structure
```
local-lead-qualifier/
├── app.py              # Telegram bot entry point
├── qualifier.py        # Gemma 4 qualification logic
├── loader.py           # CSV lead loader
├── exporter.py         # Excel export
├── leads.csv           # Sample leads (bring your own)
└── requirements.txt    # Dependencies
```

## How it works
1. User sends /start → bot asks for lead details
2. Each field is captured step by step
3. Gemma 4 analyzes the lead locally
4. Returns score (1-10), reason, outreach message
5. Results displayed in Telegram + saved to Excel

## Key Features
- 100% local — no cloud APIs
- Zero API costs
- Fully private — data never leaves your laptop
- Fast — Gemma 4 runs on consumer hardware
- Simple Telegram interface
- Clean Excel output

## Use Cases
- Qualifying leads from LinkedIn scraping
- Internal sales qualification
- Automated lead scoring
- Quick outreach message generation

## Customization
- Change Telegram token in app.py
- Modify scoring logic in qualifier.py
- Add more lead fields if needed
- Change Excel output path in exporter.py

## Troubleshooting
- Ensure Ollama is running: `ollama list`
- Check model is pulled: `ollama pull gemma4:e2b`
- Verify token in app.py
- Check Python dependencies installed

## Requirements
- 8GB RAM minimum
- 2GB free disk space
- Python 3.10+
- Ollama installed

## Built by
Hari Kishan Reddy H G (25Devmaker)
- Portfolio: https://25devmaker.vercel.app/
- LinkedIn: https://www.linkedin.com/in/hari-kishan-devmaker
- Fiverr: https://www.fiverr.com/s/BRYYlwd

## Part of my AI projects series
This is Project 08 in my public AI build series.
Check my LinkedIn for the full journey.

## License
MIT

## Author
25Devmaker