"""
report_generator.py
-------------------
Generates a full student placement report as a formatted TXT string.
Optionally produces a PDF if reportlab is installed.
All output is self-contained — no external network calls.
"""

import os
from datetime import datetime


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _line(char: str = "─", width: int = 70) -> str:
    return char * width


def _center(text: str, width: int = 70) -> str:
    return text.center(width)


def _section(title: str) -> str:
    return f"\n{_line()}\n  {title.upper()}\n{_line()}\n"


def _wrap(text: str, indent: int = 4, width: int = 66) -> str:
    """Simple word-wrap."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 <= width:
            current = (current + " " + word).strip()
        else:
            lines.append(" " * indent + current)
            current = word
    if current:
        lines.append(" " * indent + current)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# TXT Report
# --------------------------------------------------------------------------- #
def generate_txt_report(result: dict) -> str:
    """
    Generate a plain-text report from a prediction result dict.

    Parameters
    ----------
    result : dict — must contain keys returned by the prediction API:
             student_name, probability, risk_score, prediction, category,
             model_used, recommendations, feature_importance,
             weaknesses (optional), career_score (optional).

    Returns
    -------
    str — formatted multi-line report
    """
    now = datetime.now().strftime("%d %B %Y  |  %I:%M %p")
    name        = result.get("student_name", "Unknown Student")
    prob        = result.get("probability", 0)
    risk        = result.get("risk_score", 0)
    prediction  = result.get("prediction", "Unknown")
    category    = result.get("category", "")
    model_used  = result.get("model_used", "")
    recs        = result.get("recommendations", [])
    fi          = result.get("feature_importance", {})
    weaknesses  = result.get("weaknesses", [])
    career      = result.get("career_score", {})
    emp_score   = career.get("score", "N/A") if career else "N/A"
    emp_band    = career.get("band", {}).get("label", "") if career else ""

    lines = []

    # ---- Header ----
    lines += [
        _line("═"),
        _center("PLACEIQ  —  AI PLACEMENT INTELLIGENCE SYSTEM"),
        _center("STUDENT PLACEMENT REPORT"),
        _center(f"Generated on: {now}"),
        _line("═"),
        "",
    ]

    # ---- Student Summary ----
    lines += [
        _section("Student Summary"),
        f"  Name            : {name}",
        f"  Prediction      : {prediction}  ({category})",
        f"  Probability     : {prob}%",
        f"  Risk Score      : {risk} / 100",
        f"  Employ. Score   : {emp_score} / 100  [{emp_band}]",
        f"  Model Used      : {model_used}",
        "",
    ]

    # ---- Profile Inputs ----
    profile_keys = [
        ("cgpa",             "CGPA"),
        ("ssc_marks",        "SSC Marks (%)"),
        ("hsc_marks",        "HSC Marks (%)"),
        ("internships",      "Internships"),
        ("projects",         "Projects"),
        ("workshops",        "Workshops/Certs"),
