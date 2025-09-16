import markdown

# Read markdown content
with open('az_900.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content, extensions=['extra', 'toc', 'tables'])

# HTML template with CSS link
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AZ-900 Notes</title>
    <link rel="stylesheet" href="assets/styles/style.css">
</head>
<body>
<div class="markdown-body">
{html_content}
</div>
</body>
</html>
"""

# Write to az_900.html
with open('az_900.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_template)

print("az_900.html generated successfully.")
