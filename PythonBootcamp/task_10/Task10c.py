import json

user_number = input("Hello! Please select a number between 1-10")

with open ("inspirational_quotes.json", "r", encoding="utf-8") as file:
      list_quotes = json.load(file)
      user_input = int(user_number)
      quote = list_quotes[user_input-1]["quote"]
      author = list_quotes[user_input-1]["author"]
      print(f"User input: {user_input} | {quote} - by {author}")