import imaplib, email
from datetime import datetime, timedelta
import json
from core.config import IMAP_SERVER, EMAIL_ACCOUNT, APP_PASSWORD
from utils.helpers import get_llm
from langchain_core.prompts import ChatPromptTemplate

def fetch_emails_since(days: int = 1):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, APP_PASSWORD)
    mail.select("inbox")
    since_date = (datetime.today() - timedelta(days=days)).strftime("%d-%b-%Y")
    result, data = mail.search(None, f'(SINCE "{since_date}")')
    emails = []
    for eid in data[0].split():
        result, raw = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(raw[0][1])
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        emails.append({
            "id": eid.decode(),
            "subject": msg["subject"],
            "from": msg["from"],
            "date": msg["date"],
            "body": body.strip()
        })
    return emails

def analyze_email(email_text: str, provider: str = None, model: str = None):
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
    You are an email analysis assistant.
    Analyze the following email and select only one option for urgency and priority:
    ---
    {email}
    ---
    Return insights in **strict JSON** format:
    {{
      "sentiment": "positive | neutral | negative",
      "urgency": "high | medium | low",
      "priority": "High | Medium | Low",
      "entities": ["list of people, companies, or dates mentioned"],
      "summary": "short 2-3 sentence summary"
    }}
    """)

    chain = prompt | llm
    result = chain.invoke({"email": email_text})

    return result

def assign_priority(subject: str, body: str):
    high_keywords = ["urgent", "immediate", "deadline", "asap"]
    medium_keywords = ["important", "review", "schedule"]
    text = f"{subject} {body}".lower()
    if any(word in text for word in high_keywords):
        return "High"
    elif any(word in text for word in medium_keywords):
        return "Medium"
    return "Low"
