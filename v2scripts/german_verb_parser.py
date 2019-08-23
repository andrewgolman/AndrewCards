import requests
import json
import argparse

import spacy


def get_normalized_verbs(text):
    nlp = spacy.load('de')
    doc = nlp(text)
    return [token.norm_ for token in doc if token.pos_ == 'VERB']


def translate(text, source_lang='de', target_lang='en', key=None):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    lang = f'{source_lang}-{target_lang}'
    format = 'plain'
    response = requests.post(url, data={'key': key, 'text': text, 'lang': lang, 'format': format})
    res = json.loads(response.text)
    if res['code'] != 200:
        raise RuntimeError(string)
    return res['text'][0]


def main(input_file, output_file, lang):
    with open("ya_translate_token") as key_stream:
        api_key = key_stream.readline().strip()
        try:
            with open(input_file) as ifstream:
                with open(output_file, "w") as ofstream:
                    text = "\n".join(ifstream.readlines())

                    verbs = get_normalized_verbs(text)
                    verbs = set(verbs)
                    for v in verbs:
                        card = f"{v} - {translate(v, target_lang=lang, key=api_key)}"
                        print(card)
                        ofstream.write(f"{card}\n")

        except OSError:
            print(f"File not found: {ifstream}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("target_lang", nargs='?', default='ru')
    args = parser.parse_args()
    main(args.input_file, args.output_file, args.target_lang)

