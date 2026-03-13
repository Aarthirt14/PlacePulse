"""
recommendation_engine.py
------------------------
Advanced targeted recommendation generator.
Returns prioritised recommendation dicts with action items,
category, resources, and estimated impact.
"""

from utils.weakness_detector import detect_weaknesses, get_weakness_tags

# --------------------------------------------------------------------------- #
# Recommendation templates keyed by weakness tag
# --------------------------------------------------------------------------- #
_RECS = {
    "low_cgpa": [
        {
            "title": "Academic Recovery Plan",
            "category": "Academics",
            "icon": "🎓",
            "description": (
                "A low CGPA is one of the most critical placement blockers. "
                "Many companies (TCS, Infosys, Cognizant, Wipro) enforce a hard "
                "7.0 CGPA cut-off. Focus on improving internal marks, clearing "
                "backlogs, and excelling in upcoming semesters."
            ),
            "action_items": [
                "Re-appear in backlogs / supplementary exams at the earliest opportunity",
                "Request internal mark recalculation or assignment re-submission",
                "Spend 3–4 hours/day on weak subjects using NPTEL lectures",
                "Form a study group and practice previous 5-year question papers",
                "Compensate with strong projects and certifications to offset low CGPA"
            ],
            "resources": [
                {"name": "NPTEL Courses", "url": "https://nptel.ac.in"},
                {"name": "GeeksforGeeks DSA Sheet", "url": "https://geeksforgeeks.org"},
                {"name": "PlaceIQ Skill Plan", "url": "/plan?skill=low_cgpa"}
            ],
            "estimated_impact": "High — directly expands number of eligible companies",
            "timeframe": "2–3 semesters"
        }
    ],
    "backlogs": [
        {
            "title": "Clear All Backlogs Immediately",
            "category": "Academics",
            "icon": "⚠",
            "description": (
                "Backlogs are placement killers. Over 90% of mass-recruiting companies "
                "in India (TCS, Infosys, Capgemini) disqualify candidates with any "
                "active backlog. This must be your #1 priority — no other improvement "
                "matters until your backlog count is zero."
            ),
            "action_items": [
                "List all backlog subjects and their next examination dates",
                "Gather 5 years of previous exam papers for each subject",
                "Spend 5–6 hours/day on backlog subjects — prioritize high-scoring chapters",
                "Talk to seniors who cleared the same paper and get their notes",
                "Register for supplementary exams immediately if registration is open"
            ],
            "resources": [
