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

from lxml import etree
from io import StringIO

doc = StringIO(html_doc)
book_tree = etree.parse(doc)
print(type(book_tree))

first_book = book_tree.xpath("/bookstore/book[1]")
print(type(first_book))
print(first_book[0].xpath("./title/text()")[0])

last_book = book_tree.xpath("/bookstore/book[last()]")
print(last_book[0].xpath("./title/text()")[0])

titles = book_tree.xpath("//title[@lang]/text()")
print(titles)

books_above35 = book_tree.xpath("/bookstore/book[price>35.00]")
for book in books_above35:
    print(book.xpath("./title/text()")[0])

titles_and_prices = book_tree.xpath("/bookstore/book/title | //price")
for tp in titles_and_prices:
    print(tp.xpath("./text()")[0])

