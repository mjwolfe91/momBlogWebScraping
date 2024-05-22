from bs4 import BeautifulSoup

def parse_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        print(soup.prettify())

# Example usage:
file_path = 'data/peggyheinkel-wolfe.WordPress.2024-01-31.posts_only.xml'
parse_xml(file_path)