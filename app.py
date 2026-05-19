# app.py
# Lead Qualifier Bot — Telegram Version
# User sends lead details, Gemma 4 qualifies it
# Run: python app.py

import ollama
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler
)

# Conversation states
NAME, COMPANY, INDUSTRY, LINKEDIN, CLIENT_INDUSTRY = range(5)

# ── HANDLERS ─────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Lead Qualifier Bot — Powered by Gemma 4\n\n"
        "I'll qualify your leads locally. No API costs.\n\n"
        "Let's start. What's the lead's name?"
    )
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Company name?")
    return COMPANY

async def get_company(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["company"] = update.message.text
    await update.message.reply_text("Industry? (e.g. SaaS, Recruitment, Edtech)")
    return INDUSTRY

async def get_industry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["industry"] = update.message.text
    await update.message.reply_text("LinkedIn URL?")
    return LINKEDIN

async def get_linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["linkedin"] = update.message.text
    await update.message.reply_text(
        "What does your client sell? "
        "(e.g. AI automation services, lead generation)"
    )
    return CLIENT_INDUSTRY

async def qualify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_industry = update.message.text
    data = context.user_data

    await update.message.reply_text("⏳ Qualifying lead with Gemma 4...")

    prompt = f"""
You are a sales qualification expert.

Analyze this lead and respond in exactly this format:
SCORE: [number 5-10]
REASON: [one sentence why]
OUTREACH: [personalized outreach message under 50 words]

Lead details:
- Name: {data['name']}
- Company: {data['company']}
- Industry: {data['industry']}
- LinkedIn: {data['linkedin']}

Client sells: {client_industry}

Respond only in the format above. Nothing else.
"""

    response = ollama.chat(
        model="gemma4:e2b",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response["message"]["content"]

    score = reason = outreach = "N/A"
    for line in raw.split("\n"):
        if line.startswith("SCORE:"):
            score = line.replace("SCORE:", "").strip()
        elif line.startswith("REASON:"):
            reason = line.replace("REASON:", "").strip()
        elif line.startswith("OUTREACH:"):
            outreach = line.replace("OUTREACH:", "").strip()

    result = (
        f"✅ Lead Qualified!\n\n"
        f"👤 {data['name']} — {data['company']}\n"
        f"🏭 Industry: {data['industry']}\n\n"
        f"⭐ Score: {score}/10\n"
        f"💡 Reason: {reason}\n\n"
        f"📨 Outreach Message:\n{outreach}\n\n"
        f"_Powered by Gemma 4:E2B— running locally_"
    )

    await update.message.reply_text(result, parse_mode="Markdown")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled. Send /start to begin again.")
    return ConversationHandler.END

# ── MAIN ─────────────────────────────────────────

def main():
    TOKEN = "your_telegram_bot_token"  # replace this

    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME:            [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            COMPANY:         [MessageHandler(filters.TEXT & ~filters.COMMAND, get_company)],
            INDUSTRY:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_industry)],
            LINKEDIN:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_linkedin)],
            CLIENT_INDUSTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, qualify)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)
    print("🤖 Lead Qualifier Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()