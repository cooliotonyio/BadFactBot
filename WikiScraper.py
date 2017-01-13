from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from multiprocessing import Process

class ParagraphSpider(scrapy.Spider):
    name = "paragraph"

    def start_requests(self):
        urls = [
            'https://simple.wikipedia.org/wiki/Special:Random'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): #returns dictionary with page topic as key along with list form of content
        content = response.css('div.mw-content-ltr')
        raw_paragraph = response.css('p')[0]
        title = raw_paragraph.css('b::text').extract_first()
        text=raw_paragraph.css('::text').extract()
        unrefined_fact = []
        phrase=''
        for tidbit in text:
            if tidbit == title:
                unrefined_fact.append(phrase)
                unrefined_fact.append('[SUBJECT]')
                phrase=''
            else:
                phrase+=tidbit
        unrefined_fact.append(phrase)
        with open('paragraph.txt','w') as f:
        	f.write(str({title:unrefined_fact}))

def retrieve():
	configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
	runner = CrawlerRunner()
	d = runner.crawl(ParagraphSpider)
	d.addBoth(lambda _: reactor.stop())
	reactor.run() # the script will block here until the crawling is finished

def load_phrase():
    p = Process(target=retrieve)
    p.start()
    p.join()