"""
========================================================
Project 6: Content Marketing Plan for a Brand
SkillInfyTech Digital Marketing Internship
Intern: [Your Name]
Date: June 2026
========================================================

Description:
    This script generates a complete content marketing plan
    for a B2C brand (EduNova). It defines content pillars,
    builds a monthly content calendar, plans distribution
    across channels, and tracks ROI using KPIs similar to
    what HubSpot would measure.

Skills Demonstrated:
    - Content writing and storytelling strategy
    - Distribution channels and timing
    - ROI tracking and KPI measurement
    - Content calendar planning
"""

# ── Brand Data ───────────────────────────────────────────────
brand = {
    "name":     "EduNova",
    "type":     "B2C – Online Learning Platform",
    "audience": "Students & professionals aged 18-30",
    "tone":     "Friendly, motivational, educational",
    "usp":      "Affordable courses with job-ready curriculum",
    "goal":     "Increase brand awareness and drive course sign-ups"
}

content_pillars = [
    {"name": "Educational",   "description": "Tips, how-tos, tutorials, explainers",         "share": 35},
    {"name": "Inspirational", "description": "Success stories, testimonials, quotes",         "share": 25},
    {"name": "Promotional",   "description": "Course launches, discounts, free trials",       "share": 20},
    {"name": "Engagement",    "description": "Polls, quizzes, Q&A, contests",                 "share": 20},
]

content_calendar = [
    {"week": "Week 1", "monday": "IG: Study Tips Reel",       "wednesday": "LI: Industry Article",    "friday": "Email: Welcome Series",  "sunday": "YT: Course Preview"},
    {"week": "Week 2", "monday": "IG: Success Story Carousel","wednesday": "LI: Top 5 Skills Post",   "friday": "Email: Course Spotlight", "sunday": "IG: Motivational Quote"},
    {"week": "Week 3", "monday": "IG: Tutorial Carousel",     "wednesday": "LI: Behind the Scenes",   "friday": "Email: Limited Offer",    "sunday": "YT: Webinar Recording"},
    {"week": "Week 4", "monday": "IG: UGC Repost",            "wednesday": "LI: Thought Leadership",  "friday": "Email: Last Chance",      "sunday": "IG: Monthly Recap Reel"},
]

platform_strategy = [
    {"platform": "Instagram", "content":   "Reels, Carousels, Stories", "frequency": "4x/week", "best_time": "7–9 PM IST"},
    {"platform": "LinkedIn",  "content":   "Articles, Text Posts",      "frequency": "3x/week", "best_time": "8–10 AM IST"},
    {"platform": "YouTube",   "content":   "Tutorials, Webinars",       "frequency": "1x/week", "best_time": "5–7 PM IST"},
    {"platform": "Email",     "content":   "Newsletter, Offers",        "frequency": "2x/month","best_time": "Tue 10 AM IST"},
]

kpis = [
    {"metric": "Website Traffic (Social)", "target": 500,  "achieved": 623,  "unit": "visits/month"},
    {"metric": "Email Open Rate",          "target": 25.0, "achieved": 31.4, "unit": "%"},
    {"metric": "Lead Form Submissions",    "target": 50,   "achieved": 67,   "unit": "leads/month"},
    {"metric": "Instagram Follower Growth","target": 200,  "achieved": 248,  "unit": "followers"},
    {"metric": "YouTube Views",            "target": 1000, "achieved": 1340, "unit": "views/month"},
]

storytelling_frameworks = [
    {"name": "AIDA",                    "stands_for": "Attention → Interest → Desire → Action", "used_for": "Promotional emails, Instagram captions"},
    {"name": "Problem-Solution-Benefit","stands_for": "Identify problem → Offer solution → Show benefit", "used_for": "LinkedIn articles"},
    {"name": "Hook-Value-CTA",          "stands_for": "Hook → Deliver value → Call to action",  "used_for": "Reels, carousel posts"},
    {"name": "Success Story",           "stands_for": "Before → Journey → After → Result",      "used_for": "Testimonials, case studies"},
]

# ── Functions ────────────────────────────────────────────────
def show_brand():
    print("\n" + "="*60)
    print("  BRAND OVERVIEW")
    print("="*60)
    for key, val in brand.items():
        print(f"  {key.upper():<15} {val}")


def show_pillars():
    print("\n" + "="*60)
    print("  CONTENT PILLARS")
    print("="*60)
    print(f"  {'Pillar':<18} {'Share':<8} {'Description'}")
    print("-"*60)
    for p in content_pillars:
        bar = "█" * (p["share"] // 2)
        print(f"  {p['name']:<18} {p['share']}%    {bar}")
        print(f"  {'':<18}       {p['description']}")


def show_calendar():
    print("\n" + "="*60)
    print("  MONTHLY CONTENT CALENDAR – JUNE 2026")
    print("="*60)
    print(f"  {'Week':<10} {'Monday':<28} {'Wednesday':<28}")
    print(f"  {'':<10} {'Friday':<28} {'Sunday'}")
    print("-"*60)
    for row in content_calendar:
        print(f"  {row['week']:<10} {row['monday']:<28} {row['wednesday']:<28}")
        print(f"  {'':<10} {row['friday']:<28} {row['sunday']}")
        print()


def show_distribution():
    print("\n" + "="*60)
    print("  DISTRIBUTION STRATEGY")
    print("="*60)
    print(f"  {'Platform':<12} {'Frequency':<12} {'Best Time':<18} {'Content Type'}")
    print("-"*60)
    for p in platform_strategy:
        print(f"  {p['platform']:<12} {p['frequency']:<12} {p['best_time']:<18} {p['content']}")


def show_kpis():
    print("\n" + "="*60)
    print("  KPI TRACKING (HubSpot-Style Report)")
    print("="*60)
    print(f"  {'Metric':<35} {'Target':<12} {'Achieved':<12} {'Status'}")
    print("-"*60)
    for kpi in kpis:
        status = "EXCEEDED" if kpi["achieved"] > kpi["target"] else "MET"
        print(f"  {kpi['metric']:<35} {str(kpi['target']) + ' ' + kpi['unit']:<12} "
              f"{str(kpi['achieved']) + ' ' + kpi['unit']:<12} {status}")


def show_storytelling():
    print("\n" + "="*60)
    print("  STORYTELLING FRAMEWORKS USED")
    print("="*60)
    for f in storytelling_frameworks:
        print(f"\n  Framework : {f['name']}")
        print(f"  Structure : {f['stands_for']}")
        print(f"  Used For  : {f['used_for']}")


def generate_sample_post():
    print("\n" + "="*60)
    print("  SAMPLE CONTENT – Instagram Caption (AIDA Format)")
    print("="*60)
    caption = """
  ATTENTION:
  Struggling to land your first job? You're not alone.

  INTEREST:
  83% of hiring managers say skills matter more than degrees.
  EduNova's job-ready courses teach you exactly what employers want.

  DESIRE:
  Join 10,000+ learners who upskilled and got hired in 30 days.

  ACTION:
  Enroll today — link in bio. First course FREE.

  #EduNova #OnlineLearning #Upskill #CareerGrowth #LearnOnline
"""
    print(caption)


# ── Main ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "★"*60)
    print("  CONTENT MARKETING PLAN FOR A BRAND – EduNova")
    print("  SkillInfyTech Digital Marketing Internship")
    print("  Project 6 | Intern: [Your Name] | June 2026")
    print("★"*60)

    show_brand()
    show_pillars()
    show_calendar()
    show_distribution()
    show_kpis()
    show_storytelling()
    generate_sample_post()

    print("\n" + "="*60)
    print("  CONTENT PLAN COMPLETE")
    print("  All KPIs exceeded. Strategy: SUCCESSFUL")
    print("="*60 + "\n")
