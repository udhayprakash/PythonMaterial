from gazpacho import get, Soup

url = 'https://scrape.world/books'
html = get(url)
soup = Soup(html)
books = soup.find('div', {'class': 'book-'}, partial=True)

def parse(book):
    name = book.find('h4').text
    price = float(book.find('p').text[1:].split(' ')[0])
    return name, price

[parse(book) for book in books]