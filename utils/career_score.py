"""
career_score.py
---------------
Computes an Employability Score (0–100) and a dimension-wise breakdown
for a student profile. The score captures overall job-readiness
independently from the placement probability (which is model-driven).
"""

# --------------------------------------------------------------------------- #
# Dimension weights (must sum to 1.0)
# --------------------------------------------------------------------------- #
DIMENSION_WEIGHTS = {
    "academics":    0.28,   # CGPA + SSC + HSC
    "experience":   0.22,   # Internships + Projects
    "aptitude":     0.18,   # Aptitude test score
    "skills":       0.15,   # Soft skills + Training
    "activities":   0.10,   # Certifications + Extracurriculars
    "discipline":   0.07,   # Backlogs (penalty)
}

# Interpretation bands
BANDS = [
    (85, 100, "Excellent",    "var(--emerald)", "🏆"),
    (70,  84, "Strong",       "var(--sky)",     "✦"),
    (55,  69, "Moderate",     "var(--primary)", "◎"),
    (40,  54, "Needs Work",   "var(--yellow)",  "⚠"),
    (0,   39, "At Risk",      "var(--rose)",    "↘"),
]


def _clamp(val: float, mn: float = 0.0, mx: float = 100.0) -> float:
    return max(mn, min(mx, val))


def _f(val, default=0.0) -> float:
    try:
        return float(val)
    except (TypeError, ValueError):
        return float(default)


def _academics_score(data: dict) -> float:
    """0–100 academic subscore."""
    cgpa     = _clamp(_f(data.get("cgpa", 0)) / 10.0 * 100, 0, 100)
    ssc      = _clamp(_f(data.get("ssc_marks", 70)), 0, 100)
    hsc      = _clamp(_f(data.get("hsc_marks", 70)), 0, 100)
    return round(cgpa * 0.60 + ssc * 0.20 + hsc * 0.20, 2)


def _experience_score(data: dict) -> float:
    """0–100 experience subscore."""
    internships = _clamp(_f(data.get("internships", 0)), 0, 3)
    projects    = _clamp(_f(data.get("projects", 0)), 0, 5)
    intern_s = (internships / 3.0) * 100
    proj_s   = (projects   / 5.0) * 100
    return round(intern_s * 0.55 + proj_s * 0.45, 2)


def _aptitude_score_dim(data: dict) -> float:
    """0–100 aptitude subscore (same scale as the input)."""
    return _clamp(_f(data.get("aptitude_score", 0)), 0, 100)

