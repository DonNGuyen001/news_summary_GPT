import re
from newspaper import Article
from configparser import ConfigParser
from chatgpt import ChatGPT
from PyQt6.QtWidgets import QTextEdit

config = ConfigParser()
config.read('api_key.ini')
API_KEY = config.get('openai', 'APIKEY')
AI = ChatGPT(API_KEY)  # chatgpt to perform requested task
default_temperature = 1.0
max_token_size = 1024


# extract news from external link
def website_extract(url):
    article = Article(url)
    article.download()
    article.parse()
    news_data = 'content: ' + article.text
    non_empty_lines = [line for line in news_data.splitlines() if line.strip() != '']
    news_data = '\n'.join(non_empty_lines)
    return news_data


# handle website
def url_detect(user_input):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', user_input)
    return url[0]


# process input if the input is url then extract from the link
def process_input(user_input):
    data = ''
    if len(url_detect(user_input)) > 0:
        data = website_extract(url_detect(user_input))
    else:
        data = data
    return data


# use chatgpt to summarize the article send_cmd(self, mess, maximum_token=2048, temperature=1.00)
def summarize(input_data, max_size, temperature):
    result = ''
    data = ''
    prompt = 'Please summarize this article in Vietnamese: \n'
    data = process_input(input_data)
    # handle input that is longer than 2048 token
    data_chunk = [data[i:i + max_size] for i in range(0, len(data), max_size)]
    for chunk in data_chunk:
        request = prompt + chunk
        result += AI.send_cmd(request, max_size, temperature) + ' '
    return result


# translate text to language requested by user
def translate_text(input_data, max_size, temperature, language='Spanish'):
    result = ''
    prompt = 'Please translate this article to ' + language + ': '
    data = process_input(input_data)
    # handle input that is longer than limit token
    data_chunk = [data[i:i + max_size] for i in range(0, len(data), max_size)]
    for chunk in data_chunk:
        request = prompt + chunk
        result += AI.send_cmd(request, max_size, temperature) + ' '
    return result



