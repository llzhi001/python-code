html_doc = """
<bookstore>
<book category="children">
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29.99</price>
</book>

<book category="cooking">
<title lang="en">Everyday Italian</title>
<author>Giada De Laurentiis</author>
<year>2005</year>
<price>30.00</price>
</book>

<book category="web" cover="paperback">
<title lang="en">Learning XML</title>
<author>Erik T. Ray</author>
<year>2003</year>
<price>39.95</price>
</book>

<book category="web">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>
</bookstore>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")
print(soup.prettify())
print(soup.book)
print(soup.find_all('book'))

for book in soup.find_all('book'):
    print(book.title)
    for ath in book.find_all('author'):
        print(ath)

for book in soup.find_all('book'):
    print("title:",book.title.contents[0])
    for ath in book.find_all('author'):
        print("author:",ath.contents[0])
    print("**************************")

for book in soup.find_all('book'):
    print("title:", book.title.string)
    for ath in book.find_all('author'):
        print("author:", ath.string)
    print("**************************")