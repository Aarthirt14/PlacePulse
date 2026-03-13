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
