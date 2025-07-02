from os import getenv
from datetime import datetime
import jinja2

# Set date variables
date_vars = {
    "month": datetime.strftime(datetime.now(), "%B"),
    "year": datetime.strftime(datetime.now(), "%Y"),
}

# Read in the template JSON file with jinja
with open("newsletter-issue-template.md") as f:
    template = jinja2.Template(f.read())

# Render the template and insert the variables
issue_body = template.render(**date_vars)
issue_title = f"Newsletter: {date_vars['month']} {date_vars['year']}"

ci = getenv("CI", None)
print(f"CI environment: {ci}")
if ci is None:
    # We're not running in a CI environment, so just print the variables
    print(issue_title)
    print(issue_body)
else:
    print("Running in CI...")
    # Save the Variable to GITHUB_OUTPUT to use in a later step
    output_file = getenv("GITHUB_OUTPUT")
    with open(output_file, "w") as f:
        f.write(f"ISSUE_TITLE={issue_title}\n")
    
    with open("output.md", "w") as f:
        f.write(issue_body)
