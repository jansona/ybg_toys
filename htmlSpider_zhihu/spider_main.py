import url_manager
import html_downloader
import html_parser
import html_outputer
import sys
import cutWithJieba
# import tkinter

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        # self.targetKeywords = ['B-box', 'beatbox', 'bbox', 'Beatbox']
        self.targetKeywords = ['三峡']

    def craw(self, root_url):
        counter = 1
        total = 1
        self.urls.add_new_url(root_url)
        while not self.urls.isempty():
            try:
                total += 1
                new_url = self.urls.get_new_url()
                print("crawing No.%d / %d: %s" %(counter, total, new_url))
                html_cont = self.downloader.download(new_url)
                if(("问题为什么会被锁定？").encode("utf-8") in html_cont):
                    continue
                if(True not in  [word.encode("utf-8") in html_cont for word in self.targetKeywords]):
                    continue
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)

                if(new_data != None or new_data["text"] != None):
                    self.outputer.collect_data(new_data)
            except KeyboardInterrupt:
                break
            except:
                print(sys.exc_info()[0], " in spider_main")
            
            if total >= 10000:
                break
            counter += 1

        # self.outputer.output_html()


if __name__ == "__main__":
    '''https://www.zhihu.com/search?type=content&q=%E6%9D%8E%E5%92%8F'''

    # text = input("Please input the enter of the website:\n")
    print(sys.argv[1])
    input()
    root_url = str(sys.argv[1])
    object_spide = SpiderMain()
    object_spide.craw(root_url)

    object_spide.outputer.fout.close()

    cutWithJieba.separaNcount("./result/text.txt")
    cutWithJieba.writeResult()


