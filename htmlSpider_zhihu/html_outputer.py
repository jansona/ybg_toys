class HtmlOutputer(object):

    def __init__(self):
        # self.datas = []
        self.fout = open("./result/text.txt", 'w')

    def collect_data(self, new_data):
        if new_data is None or new_data=="":
            return
        if not ("知乎" in new_data):
            self.fout.write(new_data)
            self.fout.write("\n")
    

    # def output_html(self):
    #     fout = open("text.txt", 'w')

    #     for data in self.datas:
    #         fout.write("%s" %data['text'])
    #         print(data["text"])

        # fout.close()
