import datetime

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader
from pytickersymbols import PyTickerSymbols
import random

ts = PyTickerSymbols()

def stock_url(index: str, name: str):
    name_url = name.lower().replace(" ", "-").replace(".", "").replace(",", "")
    index_url = index.lower().replace(" ", "-").replace(".", "").replace(",", "")
    return f"{index_url}/{name_url}.html"

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

def create_html_table(data):
    # Create HTML table
    html_table = '<table border="1">\n'

    # Add table headers
    html_table += '<tr><th>Attribute</th><th>Value</th></tr>\n'

    # Add table rows with data
    for key, value in data.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        elif isinstance(value, dict):
            value = ', '.join([f"{k}: {v}" for k, v in value.items()])
        html_table += f'<tr><td>{key}</td><td>{value}</td></tr>\n'

    # Close HTML table
    html_table += '</table>'

    return html_table


def addStocks(articleGenerator):
    settings = articleGenerator.settings
    baseReader = BaseReader(settings)
    indices = ts.get_all_indices()
    for index in indices:
        stocks_of_index = ts.get_stocks_by_index(index)
        content = ""
        for stock in stocks_of_index:
            content = create_html_table(stock)

            rand_data = [random.random() for _ in range(100)]
            name = stock["name"]
            content += f'<div id="chartContainer" data-chart-title="My Chart {name}" data-chart-data="{rand_data}" style="height: 300px;"></div>'
            newArticle = Article(content, {
                "title": f"{index} {stock['name']}",
                "url": stock_url(index, stock['name']),
                "save_as": stock_url(index, stock['name']),
                "date": datetime.datetime.now(),
                "category": baseReader.process_metadata("category", "stocks"),
                "tags": baseReader.process_metadata("tags", f"{index}")
            })
            articleGenerator.articles.insert(0, newArticle)

def register():
    signals.article_generator_pretaxonomy.connect(addIndices)
    signals.article_generator_pretaxonomy.connect(addStocks)