"""
========================================================
Project 1: Social Media Campaign Analysis
SkillInfyTech Digital Marketing Internship
Intern: [Your Name]
Date: June 2026
========================================================

Description:
    This script analyzes the performance of a social media campaign
    across Instagram and LinkedIn. It tracks reach, engagement, clicks,
    visualizes weekly trends, compares organic vs paid traffic,
    and calculates the ROI of the campaign.

Skills Demonstrated:
    - Social media analytics
    - UTM tracking and reporting
    - KPI measurement
    - Data visualization
    - ROI calculation
"""

# ── Campaign Data ────────────────────────────────────────────
campaign_data = {
    "instagram": {
        "weeks": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "reach":        [1200, 2450, 3800, 4870],
        "impressions":  [1800, 3600, 5400, 7200],
        "engagement":   [3.2,  4.7,  5.5,  6.1],   # percentage
        "clicks":       [120,  245,  380,  520],
        "profile_visits":[340, 620,  890, 1050],
    },
    "linkedin": {
        "total_impressions": 12400,
        "unique_clicks":     860,
        "followers_gained":  215,
        "engagement_rate":   5.4,
        "ctr":               6.9,
    }
}

traffic_data = {
    "sources": ["Instagram Organic", "LinkedIn Organic", "Direct", "Other"],
    "visits":  [623, 410, 280, 130]
}

# ── Analysis Functions ───────────────────────────────────────
def analyze_instagram(data):
    ig = data["instagram"]
    print("\n" + "="*55)
    print("  INSTAGRAM CAMPAIGN PERFORMANCE (4 Weeks)")
    print("="*55)
    print(f"{'Week':<10} {'Reach':<10} {'Impressions':<14} {'Engagement':<12} {'Clicks'}")
    print("-"*55)
    for i, week in enumerate(ig["weeks"]):
        print(f"{week:<10} {ig['reach'][i]:<10,} {ig['impressions'][i]:<14,} "
              f"{ig['engagement'][i]:<12}% {ig['clicks'][i]:,}")

    total_reach = sum(ig["reach"])
    avg_engagement = sum(ig["engagement"]) / len(ig["engagement"])
    total_clicks = sum(ig["clicks"])
    growth = ((ig["reach"][-1] - ig["reach"][0]) / ig["reach"][0]) * 100

    print("-"*55)
    print(f"{'Total Reach:':<25} {total_reach:,}")
    print(f"{'Avg Engagement Rate:':<25} {avg_engagement:.1f}%")
    print(f"{'Total Clicks:':<25} {total_clicks:,}")
    print(f"{'Reach Growth (W1→W4):':<25} {growth:.1f}%")


def analyze_linkedin(data):
    li = data["linkedin"]
    print("\n" + "="*55)
    print("  LINKEDIN CAMPAIGN PERFORMANCE")
    print("="*55)
    metrics = [
        ("Total Impressions",    f"{li['total_impressions']:,}"),
        ("Unique Clicks",        f"{li['unique_clicks']:,}"),
        ("Followers Gained",     f"+{li['followers_gained']}"),
        ("Engagement Rate",      f"{li['engagement_rate']}%"),
        ("Click-Through Rate",   f"{li['ctr']}%"),
    ]
    for label, value in metrics:
        print(f"  {label:<28} {value}")


def organic_vs_paid():
    print("\n" + "="*55)
    print("  ORGANIC vs PAID TRAFFIC COMPARISON")
    print("="*55)
    comparison = [
        ("Cost",           "Free (Rs. 0)",        "Budget required"),
        ("Reach Speed",    "Slower, steady",       "Faster, immediate"),
        ("Sustainability", "Long-term",            "Short-term"),
        ("Trust Level",    "High",                 "Moderate"),
        ("Best For",       "Brand building",       "Quick conversions"),
    ]
    print(f"  {'Metric':<18} {'Organic':<22} {'Paid'}")
    print("-"*55)
    for metric, organic, paid in comparison:
        print(f"  {metric:<18} {organic:<22} {paid}")
    print("\n  This campaign used 100% ORGANIC strategy.")


def calculate_roi(data):
    ig = data["instagram"]
    li = data["linkedin"]

    total_reach       = sum(ig["reach"]) + li["total_impressions"]
    total_clicks      = sum(ig["clicks"]) + li["unique_clicks"]
    followers_gained  = 300   # Instagram + LinkedIn combined
    leads_generated   = 45
    cost              = 0     # organic campaign

    print("\n" + "="*55)
    print("  ROI EVALUATION")
    print("="*55)
    print(f"  {'Total Combined Reach:':<30} {total_reach:,}")
    print(f"  {'Total Clicks:':<30} {total_clicks:,}")
    print(f"  {'Followers Gained:':<30} +{followers_gained}")
    print(f"  {'Leads Generated:':<30} {leads_generated}")
    print(f"  {'Total Campaign Cost:':<30} Rs. {cost}")
    print(f"  {'ROI Verdict:':<30} EXCELLENT (Zero-cost, high reach)")


def traffic_sources(data):
    print("\n" + "="*55)
    print("  WEBSITE TRAFFIC SOURCES")
    print("="*55)
    total = sum(data["visits"])
    print(f"  {'Source':<28} {'Visits':<10} {'Share'}")
    print("-"*55)
    for src, visits in zip(data["sources"], data["visits"]):
        pct = (visits / total) * 100
        bar = "█" * int(pct / 5)
        print(f"  {src:<28} {visits:<10,} {pct:.1f}% {bar}")


def utm_tracking():
    print("\n" + "="*55)
    print("  UTM TRACKING PARAMETERS (Sample)")
    print("="*55)
    utm_examples = [
        ("Instagram Reel", "utm_source=instagram&utm_medium=reel&utm_campaign=edunova_june"),
        ("LinkedIn Post",  "utm_source=linkedin&utm_medium=post&utm_campaign=edunova_june"),
        ("Email Campaign", "utm_source=email&utm_medium=newsletter&utm_campaign=edunova_june"),
    ]
    for channel, utm in utm_examples:
        print(f"\n  Channel  : {channel}")
        print(f"  UTM Link : https://edunova.com/signup?{utm}")


def weekly_trend(data):
    ig = data["instagram"]
    print("\n" + "="*55)
    print("  WEEKLY REACH TREND (Instagram)")
    print("="*55)
    max_reach = max(ig["reach"])
    for i, (week, reach) in enumerate(zip(ig["weeks"], ig["reach"])):
        bar_len = int((reach / max_reach) * 40)
        bar = "█" * bar_len
        print(f"  {week}: {bar} {reach:,}")


# ── Main ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "★"*55)
    print("  SOCIAL MEDIA CAMPAIGN ANALYSIS")
    print("  SkillInfyTech Digital Marketing Internship")
    print("  Project 1 | Intern: [Your Name] | June 2026")
    print("★"*55)

    analyze_instagram(campaign_data)
    analyze_linkedin(campaign_data)
    organic_vs_paid()
    calculate_roi(campaign_data)
    traffic_sources(traffic_data)
    utm_tracking()
    weekly_trend(campaign_data)

    print("\n" + "="*55)
    print("  ANALYSIS COMPLETE")
    print("  All KPIs tracked. Campaign ROI: EXCELLENT")
    print("="*55 + "\n")
