import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        counter = 1
        self.urls.add_new_url(root_url)
        while not self.urls.isempty():
            try:
                new_url = self.urls.get_new_url()
                print("crawing No.%d: %s" %(counter, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                if "python" in html_cont or "Python" in html_cont or "Perl" in html_cont:
                    print('*' * 10 ,"Find it!", '*' * 10)
                    self.outputer.collect_data(new_data)
            except:
                print("crawing failed")
            if counter >= 1000:
                break
            counter += 1

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://en.wikipedia.org/wiki/Compiled_language"
    object_spide = SpiderMain()
    object_spide.craw(root_url)


