import os
import re

# Path to the CSS file
css_file_path = 'assets/css/iastatecustom3.css'
new_css_file_path = 'assets/css/iastate-copilot-consolidate.css'

# Function to extract class and ID selectors from CSS
def extract_selectors(css_content):
    class_pattern = re.compile(r'\.([a-zA-Z0-9_-]+)')
    id_pattern = re.compile(r'\#([a-zA-Z0-9_-]+)')
    classes = set(class_pattern.findall(css_content))
    ids = set(id_pattern.findall(css_content))
    return classes, ids

# Function to search for selectors in the repository
def search_selectors_in_repo(selectors, repo_path='.'):
    used_selectors = set()
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(('.html', '.js', '.jsx', '.ts', '.tsx', '.php', '.py')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    for selector in selectors:
                        if selector in content:
                            used_selectors.add(selector)
    return used_selectors

# Read the CSS file
with open(css_file_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Extract selectors from CSS
classes, ids = extract_selectors(css_content)

# Search for used selectors in the repository
used_classes = search_selectors_in_repo(classes)
used_ids = search_selectors_in_repo(ids)

# Function to remove unused CSS rules
def remove_unused_css(css_content, used_classes, used_ids):
    def is_selector_used(selector):
        if selector.startswith('.'):
            return selector[1:] in used_classes
        elif selector.startswith('#'):
            return selector[1:] in used_ids
        return True

    cleaned_css_lines = []
    inside_rule = False
    for line in css_content.splitlines():
        if '{' in line:
            selector = line.split('{')[0].strip()
            if is_selector_used(selector):
                inside_rule = True
                cleaned_css_lines.append(line)
            else:
                inside_rule = False
        elif '}' in line:
            if inside_rule:
                cleaned_css_lines.append(line)
            inside_rule = False
        elif inside_rule:
            cleaned_css_lines.append(line)
    
    return '\n'.join(cleaned_css_lines)

# Remove unused CSS rules
cleaned_css_content = remove_unused_css(css_content, used_classes, used_ids)

# Write the cleaned CSS to a new file
with open(new_css_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned_css_content)

print(f"Consolidated CSS written to {new_css_file_path}")