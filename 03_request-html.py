from requests_html import HTMLSession

# Initialize an HTML session
session = HTMLSession()

# Send a GET request to the website
r = session.get('https://www.blender.org/')

# Print all links found on the page
print("Links on the page:", r.html.links)

# Try to find the 'About' section (check for the correct selector)
# Assuming 'About' could be a section or an element with a specific ID or class
about = r.html.find('section.about', first=True)  # Adjust selector based on actual structure

# Check if the 'about' section exists before accessing its text
if about:
    print("\nAbout section content:", about.text)
else:
    print("\n'About' section not found.")
