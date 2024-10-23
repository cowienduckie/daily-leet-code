import os

# Directory containing the source files
src_dir = "src"

# Initialize the README content
readme_content = """# Daily LeetCode

This repository contains my solutions to LeetCode problems. I will be solving at least one problem every day.

## Solved Problems
| # | Problem | Solution |
|---|---------|----------|
"""


# List all files in the src directory
table_rows = []
for filename in sorted(os.listdir(src_dir)):
    if filename.endswith(".py"):
        # Extract number and problem name
        number, problem_name = filename.split("_", 1)
        problem_name = problem_name.replace(".py", "")
        title_name = problem_name.replace("-", " ").title()

        # Format the table row
        row = f"| {number} | [{title_name}](https://leetcode.com/problems/{problem_name}) | [{src_dir}/{filename}]({src_dir}/{filename}) |\n"

        table_rows.append((int(number), row))

# Sort the table rows by problem number and add them to the README content
table_rows.sort(key=lambda x: x[0])
for _, row in table_rows:
    readme_content += row

# Write the content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
