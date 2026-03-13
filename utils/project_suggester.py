"""
project_suggester.py
--------------------
Suggests project ideas based on detected weakness tags and student stream.
Loads from data/project_suggestions.json.
"""

import os
import json

_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "project_suggestions.json"
)

_STREAM_CATEGORY_MAP = {
    "computer science":      ["machine_learning", "web_development", "data_science", "python_automation"],
    "information technology":["web_development", "machine_learning", "python_automation", "mini_projects"],
    "electronics":           ["python_automation", "machine_learning", "mini_projects", "data_science"],
    "mechanical":            ["python_automation", "data_science", "mini_projects", "web_development"],
    "civil":                 ["data_science", "python_automation", "mini_projects", "web_development"],
}

_WEAKNESS_CATEGORY_MAP = {
