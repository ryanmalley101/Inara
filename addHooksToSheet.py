import re

def add_event_handlers_to_inputs(html_file):
    with open(html_file, 'r') as file:
        html = file.read()

    modified_html = re.sub(
        r'(<(?:input|textarea)[^>]*\bname="([^"]+)".*?)(\/?>)',
        r'\1 value={character.\2} onChange={handleInputChange} onBlur={handleInputBlur}\3',
        html,
        flags=re.IGNORECASE
    )

    with open("new_html.html", 'w') as file:
        file.write(modified_html)
# Usage
add_event_handlers_to_inputs('charsheet.html')
