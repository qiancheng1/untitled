class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html','w') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table>')
            for data in self.datas:
                f.write('<tr>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'].encode('utf-8'))
                f.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')