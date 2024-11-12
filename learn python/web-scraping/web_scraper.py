from bs4 import BeautifulSoup  # Correct import

# Open the HTML file and parse it
with open('file.html', 'r') as f:
    html = f.read()
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    
    # Pretty print the parsed HTML
    print(soup.prettify())  # Corrected 'pretify' to 'prettify'
    
    # Print the title of the HTML
    print(soup.title)
