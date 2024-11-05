import requests, json, random

# Fetch a random quote from the quote API
quote_res = requests.get("https://zenquotes.io/api/random")
quote_data = json.loads(quote_res.text)
random_quote = quote_data[0]['q']  # Quote text
quote_author = quote_data[0]['a']  # Quote author

# Write output to README.md
with open("./README.md", "w") as f:
    f.write(f'''<h3 align="center">You have been greeted by - <b>{quote_author}</b></h3>
    <h4 align="center">"{random_quote}" - <i>{quote_author}</i></h4>
    <h3 align="center">Have a wonderful day!</h3>
    ''')
