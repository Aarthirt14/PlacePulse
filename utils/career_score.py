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
