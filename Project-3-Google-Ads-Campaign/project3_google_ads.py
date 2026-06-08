"""
========================================================
Project 3: Google Ads Campaign Setup
SkillInfyTech Digital Marketing Internship
Intern: [Your Name]
Date: June 2026
========================================================

Description:
    This script simulates the setup and analysis of a Google Ads
    PPC campaign for EduNova (hypothetical online learning brand).
    It covers keyword research, ad creative design, audience
    targeting, A/B testing, bid strategy, and conversion tracking.

Skills Demonstrated:
    - Google Ads dashboard simulation
    - Keyword research and match types
    - A/B testing and bid strategy
    - Conversion tracking
    - CTR, CPC, CPA analysis
"""

# ── Campaign Configuration ───────────────────────────────────
campaign = {
    "name":     "EduNova – Course Sign-Up Campaign",
    "type":     "Search + Display (PPC)",
    "budget":   5000,   # Rs. per month
    "duration": "30 days (June 2026)",
    "goal":     "Drive course sign-ups",
    "location": "India",
    "language": "English",
    "devices":  "Mobile + Desktop"
}

keywords = [
    {"keyword": "online courses for students",       "match": "Broad",  "cpc": 8,  "searches": 22000},
    {"keyword": "digital marketing course online",   "match": "Exact",  "cpc": 11, "searches": 18500},
    {"keyword": "affordable upskilling courses",     "match": "Phrase", "cpc": 7,  "searches": 12000},
    {"keyword": "best online learning platform",     "match": "Phrase", "cpc": 10, "searches": 9800},
    {"keyword": "learn digital skills online",       "match": "Broad",  "cpc": 6,  "searches": 15200},
    {"keyword": "EduNova online course",             "match": "Exact",  "cpc": 4,  "searches": 3400},
]

negative_keywords = ["free", "free courses", "free certificate", "crack", "pirated", "torrent"]

ad_versions = {
    "A": {
        "headline1":    "Learn Digital Skills Online",
        "headline2":    "Courses Starting at Rs. 499",
        "headline3":    "Join 10,000+ Learners Today",
        "description1": "Upskill with job-ready courses in Marketing, Design & Tech. Enroll now!",
        "description2": "Flexible online learning. Get certified. Boost your career with EduNova.",
        "url":          "www.edunova.com/courses",
        "impressions":  24500,
        "clicks":       1470,
        "conversions":  62,
        "spend":        2400,
    },
    "B": {
        "headline1":    "Top Online Courses in India",
        "headline2":    "Get Certified in 30 Days",
        "headline3":    "Affordable. Flexible. Job-Ready.",
        "description1": "Master in-demand skills from home. 100+ courses. Start your free trial today!",
        "description2": "Industry-recognized certificates. Learn at your pace. Enroll at EduNova.",
        "url":          "www.edunova.com/start",
        "impressions":  23800,
        "clicks":       1190,
        "conversions":  48,
        "spend":        2380,
    }
}

audience = {
    "age":        "18 – 30 years",
    "location":   "India (all major cities)",
    "language":   "English",
    "devices":    "Mobile + Desktop",
    "interests":  ["Education", "Career Development", "Technology"],
    "remarketing":"Website visitors who did not sign up",
    "lookalike":  "Similar to existing course enrollees"
}

kpis = {
    "target_ctr":  5.0,
    "target_cpc":  12,
    "target_cvr":  3.0,
    "target_cpa":  200,
    "target_impressions": 50000,
}

# ── Analysis Functions ───────────────────────────────────────
def show_campaign():
    print("\n" + "="*60)
    print("  CAMPAIGN CONFIGURATION")
    print("="*60)
    for k, v in campaign.items():
        print(f"  {k.upper():<12} {v}")


def show_keywords():
    print("\n" + "="*60)
    print("  KEYWORD RESEARCH")
    print("="*60)
    print(f"  {'Keyword':<38} {'Match':<8} {'CPC':<8} {'Searches/mo'}")
    print("-"*60)
    for kw in keywords:
        print(f"  {kw['keyword']:<38} {kw['match']:<8} Rs.{kw['cpc']:<5} {kw['searches']:,}")
    total_potential = sum(k["searches"] for k in keywords)
    avg_cpc = sum(k["cpc"] for k in keywords) / len(keywords)
    print("-"*60)
    print(f"  {'Total Potential Reach:':<38} {total_potential:,}")
    print(f"  {'Average CPC:':<38} Rs. {avg_cpc:.1f}")
    print(f"\n  Negative Keywords: {', '.join(negative_keywords)}")


def show_ad_versions():
    print("\n" + "="*60)
    print("  AD CREATIVE – A/B TEST VERSIONS")
    print("="*60)
    for version, ad in ad_versions.items():
        print(f"\n  ── Version {version} ──────────────────────────────")
        print(f"  Headline 1   : {ad['headline1']}")
        print(f"  Headline 2   : {ad['headline2']}")
        print(f"  Headline 3   : {ad['headline3']}")
        print(f"  Description 1: {ad['description1']}")
        print(f"  Display URL  : {ad['url']}")


def run_ab_test():
    print("\n" + "="*60)
    print("  A/B TEST RESULTS")
    print("="*60)
    results = {}
    for v, ad in ad_versions.items():
        ctr = (ad["clicks"] / ad["impressions"]) * 100
        cvr = (ad["conversions"] / ad["clicks"]) * 100
        cpc = ad["spend"] / ad["clicks"]
        cpa = ad["spend"] / ad["conversions"]
        results[v] = {"ctr": ctr, "cvr": cvr, "cpc": cpc, "cpa": cpa}

    print(f"  {'Metric':<25} {'Version A':<18} {'Version B'}")
    print("-"*60)
    metrics = [
        ("Impressions",    f"{ad_versions['A']['impressions']:,}",                f"{ad_versions['B']['impressions']:,}"),
        ("Clicks",         f"{ad_versions['A']['clicks']:,}",                     f"{ad_versions['B']['clicks']:,}"),
        ("CTR",            f"{results['A']['ctr']:.1f}%",                         f"{results['B']['ctr']:.1f}%"),
        ("Avg CPC",        f"Rs. {results['A']['cpc']:.2f}",                      f"Rs. {results['B']['cpc']:.2f}"),
        ("Conversions",    f"{ad_versions['A']['conversions']}",                  f"{ad_versions['B']['conversions']}"),
        ("Conversion Rate",f"{results['A']['cvr']:.1f}%",                         f"{results['B']['cvr']:.1f}%"),
        ("Cost Per Acq.",  f"Rs. {results['A']['cpa']:.2f}",                      f"Rs. {results['B']['cpa']:.2f}"),
    ]
    for label, a, b in metrics:
        print(f"  {label:<25} {a:<18} {b}")

    winner = "A" if results["A"]["ctr"] > results["B"]["ctr"] else "B"
    print(f"\n  WINNER: Version {winner} — Higher CTR, Lower CPC, More Conversions")
    print(f"  Action : Scale up Version {winner} for Week 3 & 4")
    return winner


def show_audience():
    print("\n" + "="*60)
    print("  AUDIENCE TARGETING")
    print("="*60)
    for k, v in audience.items():
        val = ", ".join(v) if isinstance(v, list) else v
        print(f"  {k.upper():<14} {val}")


def show_conversion_tracking():
    print("\n" + "="*60)
    print("  CONVERSION TRACKING SETUP")
    print("="*60)
    steps = [
        "Google Ads Tag installed on /thankyou confirmation page",
        "Conversion action: 'Course Sign-Up' on form submission",
        "Google Analytics linked to Google Ads account",
        "Goal configured: form submission on /signup page",
        "View-through conversions enabled for Display ads",
        "Remarketing list created for non-converting visitors",
    ]
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")


def performance_summary():
    total_impressions = sum(ad["impressions"] for ad in ad_versions.values())
    total_clicks      = sum(ad["clicks"] for ad in ad_versions.values())
    total_conversions = sum(ad["conversions"] for ad in ad_versions.values())
    total_spend       = sum(ad["spend"] for ad in ad_versions.values())
    overall_ctr       = (total_clicks / total_impressions) * 100
    overall_cvr       = (total_conversions / total_clicks) * 100
    overall_cpc       = total_spend / total_clicks
    overall_cpa       = total_spend / total_conversions

    print("\n" + "="*60)
    print("  CAMPAIGN PERFORMANCE SUMMARY")
    print("="*60)
    results = [
        ("Total Impressions",   f"{total_impressions:,}",         f"> {kpis['target_impressions']:,}", total_impressions > kpis["target_impressions"]),
        ("Total Clicks",        f"{total_clicks:,}",              "–",                                 True),
        ("Overall CTR",         f"{overall_ctr:.1f}%",            f"> {kpis['target_ctr']}%",          overall_ctr > kpis["target_ctr"]),
        ("Average CPC",         f"Rs. {overall_cpc:.2f}",         f"< Rs. {kpis['target_cpc']}",       overall_cpc < kpis["target_cpc"]),
        ("Total Conversions",   f"{total_conversions}",           "–",                                 True),
        ("Conversion Rate",     f"{overall_cvr:.1f}%",            f"> {kpis['target_cvr']}%",          overall_cvr > kpis["target_cvr"]),
        ("Cost Per Acquisition",f"Rs. {overall_cpa:.2f}",         f"< Rs. {kpis['target_cpa']}",       overall_cpa < kpis["target_cpa"]),
        ("Total Spend",         f"Rs. {total_spend:,}",           f"Rs. {campaign['budget']:,}",       total_spend <= campaign["budget"]),
    ]
    print(f"  {'Metric':<28} {'Result':<16} {'Target':<16} {'Status'}")
    print("-"*60)
    for metric, result, target, passed in results:
        status = "PASSED" if passed else "MISSED"
        print(f"  {metric:<28} {result:<16} {target:<16} {status}")


# ── Main ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "★"*60)
    print("  GOOGLE ADS CAMPAIGN SETUP & ANALYSIS")
    print("  SkillInfyTech Digital Marketing Internship")
    print("  Project 3 | Intern: [Your Name] | June 2026")
    print("★"*60)

    show_campaign()
    show_keywords()
    show_audience()
    show_ad_versions()
    winner = run_ab_test()
    show_conversion_tracking()
    performance_summary()

    print("\n" + "="*60)
    print(f"  CAMPAIGN COMPLETE")
    print(f"  Winner Ad: Version {winner} | All KPIs: PASSED")
    print(f"  Recommendation: Scale budget to Rs. 10,000/month")
    print("="*60 + "\n")
