# Quotes Scraper

### Endpoint: Default

Using a basic scrapy spider in this case to crawl the url, parse it and generate an output json of quotes, authors, tags.

####Command to run on terminal
```
$ scrapy crawl quotes_default -o output/quotes_default.json
```


### Endpoint: Scroll

In this case, the page is dynamically loaded so inspected the elements and network and found the correct url which is invoked during scrolling and then parse it and generate an output json of quotes, authors, tags.

####Command to run on terminal
```
$ scrapy crawl quotes_scroll -o output/quotes_scroll.json
```