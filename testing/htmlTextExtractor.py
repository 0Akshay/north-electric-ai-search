from bs4 import BeautifulSoup
import re

def extract_text_from_html(file_path):
    # Open and read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    html_content = re.sub(r"{%.*?%}|{{.*?}}", "", html_content, flags=re.DOTALL)
    
    # Parse HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract only text (strip out tags, scripts, styles)
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()  # remove scripts and styles

    text = soup.get_text(separator="\n")  # separate lines with newline
    clean_text = "\n".join(line.strip() for line in text.splitlines() if line.strip())  # remove blank lines

    return clean_text

if __name__ == "__main__":
    file_path = "../templates/faqs.html"  # Path to your HTML file
    extracted_text = extract_text_from_html(file_path)
    print(extracted_text)
