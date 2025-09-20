import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from core.security import get_current_user
from schemas.user import EmailAnalysisCreate, EmailAnalysisRead
from services.ai_service import fetch_emails_since, analyze_email, assign_priority

router = APIRouter()

@router.post("/analyze")
def analyze_single_email(
    email_data: EmailAnalysisCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    analysis = analyze_email(email_data.body)
    try:
        parsed = json.loads(analysis)
    except json.JSONDecodeError:
        parsed = {"raw_output": analysis}
    return  {
            "id": email_data.email_id,
            "subject": email_data.subject,
            "from": email_data.sender,
            "analysis": parsed
        }

@router.get("/emails/since-yesterday")
def analyze_emails_since_yesterday(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    emails = fetch_emails_since(days=7)
    results = []
    results = []
    for mail in emails:
        parsed = None
        result = analyze_email(mail["body"])
        print(result)
        try:
            parsed = json.loads(result)
        except json.JSONDecodeError:
            pass

        results.append({
            "id": mail["id"],
            "subject": mail["subject"],
            "from": mail["from"],
            "analysis": parsed
        })

    return results
