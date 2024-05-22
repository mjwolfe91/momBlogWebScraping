from bs4 import BeautifulSoup, CData
def parse_xml(file_path):
    posts = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'xml')

        for item in soup.find_all('item'):
            print(item)
            post = {}

            # Extract title
            title_tag = item.find('title')
            if title_tag:
                if title_tag.string:
                    post['title'] = title_tag.string.strip()
                elif title_tag.contents:
                    cdata_content = title_tag.contents[0]
                    if isinstance(cdata_content, CData):
                        post['title'] = cdata_content.strip()
                    else:
                        post['title'] = cdata_content.string.strip() if cdata_content.string else ""
                else:
                    post['title'] = "Untitled"
            else:
                post['title'] = "Untitled"

            # Extract content
            content_tag = item.find('content:encoded')
            if content_tag:
                if content_tag.contents:
                    cdata_content = content_tag.contents[0]
                    if isinstance(cdata_content, CData):
                        post['content'] = cdata_content.strip()
                    else:
                        post['content'] = content_tag.get_text(strip=True)
                else:
                    post['content'] = ""
            else:
                post['content'] = ""

            posts.append(post)

    return posts

if __name__ == '__main__':

    file_path = 'data/peggyheinkel-wolfe.WordPress.2024-01-31.posts_only.xml'
    posts = parse_xml(file_path)
    for post in posts:
        print("Title:", post['title'])
        print("Content:", post['content'])
        print("-" * 50)