from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin
import sys


class HtmlParser(object):

    keyWords = ["question", "topic", "answer"]

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            try:
                new_url = link["href"]
                if(True in [(word in new_url) for word in self.keyWords]):
                    new_full_url = urljoin(url, new_url)
                    new_urls.add(new_full_url)
            except:
                print(sys.exc_info()[0], " in html_parser mod")
        return new_urls

    def _get_new_data(self, url, soup):

        res_data = ""
        # nodes = {}

        spans = soup.find_all("span", class_="RichText ztext CopyrightRichText-richText")
        for span in spans:
            ps = span.find_all("p")
            for p in ps:
                res_data += p.get_text()

        # try:
        #     nodes = soup.find("span", class_="RichText ztext CopyrightRichText-richText").find_all("p")
        #     print(len(nodes))
        #     if nodes == None:
        #         return None
        # except:
        #     print("fuck")
        #     return res_data
        # print(type(nodes))
        # for p in nodes:
        #     res_data += p.get_text()

        return res_data

    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

