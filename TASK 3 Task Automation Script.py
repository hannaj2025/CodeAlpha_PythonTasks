import re

text = """
Hello team,
Please contact support@example.com for help.
You can also reach us at sales@company.org and admin123@test.co.in.
Thank you!
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}", text)

for email in emails:
    print(email)
