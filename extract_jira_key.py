import json
import sys

# Load the JSON data passed from the previous step
comments_data = json.load(sys.stdin)

# Loop through each comment to find the Jira issue key
for comment in comments_data:
    if "This issue has been linked to a Jira ticket:" in comment['body']:
        # Extract the Jira key from the comment body
        jira_key = comment['body'].split("This issue has been linked to a Jira ticket: ")[-1]
        print(jira_key)
        break
