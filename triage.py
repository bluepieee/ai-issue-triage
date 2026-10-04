from google import genai
import json
import os

client = genai.Client()

# Check if GitHub Actions provided an issue
event_path = os.getenv("GITHUB_EVENT_PATH")

if event_path and os.path.exists(event_path):
    with open(event_path, "r", encoding="utf-8") as file:
        event = json.load(file)

    issue_data = event["issue"]
    issue_number = issue_data["number"]
    issue_title = issue_data["title"]
    issue_body = issue_data.get("body") or ""

    issue = f"{issue_title}\n\n{issue_body}"

else:
    # Test issue when running locally
    issue_number = 1
    issue = """
The login button is not working for users using Google Chrome.
"""

prompt = f"""
Analyze this GitHub issue:

{issue}

Return:
1. A short summary
2. Category (Bug, Feature Request, Documentation, Performance, Other)
3. Priority (High, Medium, Low)
4. Suggested action
"""

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)

analysis = response.output_text

# Load existing results
with open("results.json", "r", encoding="utf-8") as file:
    results = json.load(file)

# Add the new result
results.append({
    "issue_number": issue_number,
    "issue": issue.strip(),
    "analysis": analysis
})

# Save results
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print("Issue analyzed successfully!")
print(analysis)