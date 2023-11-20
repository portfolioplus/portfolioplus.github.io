import datetime

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader
from pytickersymbols import PyTickerSymbols

ts = PyTickerSymbols()

def stock_url(index: str, name: str):
    name_url = name.lower().replace(" ", "-").replace(".", "")
    index_url = index.lower().replace(" ", "-").replace(".", "")
    return f"{index_url}-{name_url}.html"

def addIndices(articleGenerator):
    settings = articleGenerator.settings
    baseReader = BaseReader(settings)
    indices = ts.get_all_indices()
    for index in indices:
        stocks_of_index = ts.get_stocks_by_index(index)
        content = ""
        for stock in stocks_of_index:
            content += f"<li><a href='{stock_url(index, stock['name'])}'>{stock['name']}</a></li>"

        newArticle = Article(content, {
            "title": f"{index} stocks",
            "date": datetime.datetime.now(),
            "category": baseReader.process_metadata("category", "index"),
            "tags": baseReader.process_metadata("tags", f"{index}")
        })

        articleGenerator.articles.insert(0, newArticle)


def addStocks(articleGenerator):
    settings = articleGenerator.settings
    baseReader = BaseReader(settings)
    indices = ts.get_all_indices()
    for index in indices:
        stocks_of_index = ts.get_stocks_by_index(index)
        content = ""
        for stock in stocks_of_index:
            content = f"{stock}"
            newArticle = Article(content, {
                "title": f"{index} {stock['name']}",
                #"override_url": stock_url(index, stock['name']),
                "date": datetime.datetime.now(),
                "category": baseReader.process_metadata("category", "stocks"),
                "tags": baseReader.process_metadata("tags", f"{index}")
            })
            articleGenerator.articles.insert(0, newArticle)

def register():
    signals.article_generator_pretaxonomy.connect(addIndices)
    signals.article_generator_pretaxonomy.connect(addStocks)