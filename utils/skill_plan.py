"""
skill_plan.py
-------------
Generates a structured weekly skill improvement plan based on detected weaknesses.
Loads plan templates from data/skill_plans.json.
"""

import os
import json

_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "skill_plans.json"
)

# Map weakness tags → plan keys in skill_plans.json
_TAG_TO_PLAN = {
    "low_cgpa":           "low_cgpa",
    "low_aptitude":       "low_aptitude",
    "no_internships":     "no_internships",
    "low_soft_skills":    "low_soft_skills",
    "backlogs":           "backlogs",
    "low_projects":       "low_projects",
}


def _load_plans() -> dict:
    if os.path.exists(_DATA_PATH):
        with open(_DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f).get("plans", {})
    return {}


def get_plan(plan_key: str) -> dict | None:
    """Return a single plan dict by key, or None if not found."""
    plans = _load_plans()
    return plans.get(plan_key)
