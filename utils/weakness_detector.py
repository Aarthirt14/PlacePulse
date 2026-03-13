"""
weakness_detector.py
--------------------
Analyzes a student profile dict and returns a structured list of weaknesses.
Each weakness has: field, label, severity ('CRITICAL'|'HIGH'|'MEDIUM'|'LOW'),
message, threshold, actual_value, and improvement_hint.
"""

# --------------------------------------------------------------------------- #
# Thresholds
# --------------------------------------------------------------------------- #
THRESHOLDS = {
    "cgpa":            {"critical": 5.5, "high": 6.5, "medium": 7.0},
    "aptitude_score":  {"critical": 40,  "high": 55,  "medium": 65},
    "soft_skills":     {"critical": 2.0, "high": 2.5, "medium": 3.0},
    "internships":     {"none": 0,       "low": 1},
    "projects":        {"none": 0,       "low": 2},
    "workshops":       {"none": 0,       "low": 1},
    "backlogs":        {"any": 1,        "high": 2},
    "ssc_marks":       {"critical": 50,  "high": 60},
    "hsc_marks":       {"critical": 50,  "high": 60},
}

SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


def _f(val, default=0):
    """Safe float cast."""
    try:
        return float(val)
    except (TypeError, ValueError):
        return float(default)


def detect_weaknesses(data: dict) -> list[dict]:
    """
    Parameters
    ----------
    data : dict
        Student profile. Keys match the prediction form fields:
        cgpa, aptitude_score, soft_skills, internships, projects,
        workshops (Workshops_Certifications), backlogs, ssc_marks,
        hsc_marks, extracurricular, placement_training.

    Returns
    -------
    list[dict]  – sorted by severity (CRITICAL first)
    """
    weaknesses = []

    cgpa           = _f(data.get("cgpa", 0))
    aptitude       = _f(data.get("aptitude_score", 0))
    soft_skills    = _f(data.get("soft_skills", 0))
    internships    = int(_f(data.get("internships", 0)))
    projects       = int(_f(data.get("projects", 0)))
    workshops      = int(_f(data.get("workshops", data.get("workshops_certifications", 0))))
