import requests
import json


def request(action, **params):
    return requests.post(
        "http://localhost:8765", json={"action": action, "params": params, "version": 6}
    ).json()


def search_cards(query):
    return request("findCards", query=query)


def add_note(deck_name, front, back, tags=None):
    if tags is None:
        tags = []

    request("createDeck", deck=deck_name)

    return request(
        "addNote",
        note={
            "deckName": deck_name,
            "modelName": "基本",
            "fields": {"表面": front, "裏面": back},
            "tags": tags,
        },
    )


response = request("modelFieldNames", modelName="基本")
print(response)

cards = search_cards("tag:コンピュータ構成要素")
print(cards)


result = add_note("日本語", "ばなな", "banana", ["食べ物", "果物"])
print(result)
