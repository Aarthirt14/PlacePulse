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
