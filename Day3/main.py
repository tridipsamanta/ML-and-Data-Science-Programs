import requests

word = input("Write Any Word: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    meaning = data[0]["meanings"][0]
    definition = meaning["definitions"][0]["definition"]

    print(f"\n{word.capitalize()} ({meaning['partOfSpeech']}):")
    print(definition)
else:
    print("Word not found")
