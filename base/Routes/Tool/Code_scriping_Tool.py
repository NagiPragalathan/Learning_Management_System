import requests
from bs4 import BeautifulSoup
from googlesearch import search


def get_image_url(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')
    image_url = image_tags[0]['src']
    return image_url

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

