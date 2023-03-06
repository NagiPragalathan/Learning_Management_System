import requests
from bs4 import BeautifulSoup
from googlesearch import search


def get_image_url(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    # Make a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.add(img_url)
    return list(image_urls)

def get_answer_from_given_link(question_url):

    response = requests.get(question_url)

    soup = BeautifulSoup(response.content, 'html.parser')    
    question_title = soup.find('a', class_='question-hyperlink').get_text()
    print('Question:', question_title)

    print('run next....')
    # Find the code blocks in the question and print them
    code_blocks = soup.find_all('pre')
    print(code_blocks)
    for i, code_block in enumerate(code_blocks):
        print(f'\nExample code {i+1}:')
        print(code_block.get_text())

def get_stackoverflow_link(question,site='stackoverflow.com'):

    num_results = 50

    stackoverflow_link=""
    # Search Google for the question and get the top search results
    search_results = search(question, num_results=num_results)

    # Loop through the search results and find the Stack Overflow link
    for result in search_results:
        if site in result:
            stackoverflow_link = result
            break

    return stackoverflow_link
# print('answer',get_stackoverflow_link("add two numbers"))

