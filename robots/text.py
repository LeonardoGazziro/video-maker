import Algorithmia
from nltk.tokenize import sent_tokenize
import re
from credentials import ALGORITHMIA
import pprint


class Robot():

    def fetch_content_from_wikipedia(self, content):
        # Authenticate with your API key
        _api_key = ALGORITHMIA['api_key']

        _input = {
            "articleName": content['search_term'],
            "lang": "en"
        }

        # Create the Algorithmia client object
        _client = Algorithmia.client(_api_key)
        _wikipedia_algo = _client.algo('web/WikipediaParser/0.1.2')
        _wikipedia_content = _wikipedia_algo.pipe(_input).result

        return _wikipedia_content

    def sanitize_content(self, content):
        sanitized = re.sub(r'/\((?:\([^()]*\)|[^()])*\)/gm', '', content)
        sanitized = sanitized.split('\n')
        sanitized = [line for line in sanitized if line.strip() and '==' not in line]

        return str(sanitized).replace("\\", "")

    def break_content_into_sentences(self, content):
        sentences = sent_tokenize(content)

        sentences_list = []
        for sentence in sentences:
            d = {}
            d['text'] = sentence
            d['key_words'] = []
            d['images'] = []

            sentences_list.append(d)

        return sentences_list
