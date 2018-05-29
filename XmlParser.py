#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.sax


class MoviesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData  = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        # 意思是把所有的tag节点给CurrentData
        self.CurrentData  = tag
        if tag == 'movie':
            title = attributes["title"]
            print('title %s' % title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print('type %s' % self.type)
        elif self.CurrentData == "format":
            print('format %s' % self.format)
        elif self.CurrentData == "year":
            print('year %s' % self.year)
        elif self.CurrentData == "rating":
            print('rating %s' % self.rating)
        elif self.CurrentData == "stars":
            print('stars %s' % self.stars)
        elif self.CurrentData == "description":
            print('description %s' % self.description)
            print('*******************************')
        self.CurrentData  = ""

    def characters(self, content):
        # 判断都是用的CurrentData,Current is tag info, content is a trunk of character data, or many trunk info as below
        if self.CurrentData  == 'type':
            self.type = content
        elif self.CurrentData  == 'format':
            self.format = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'rating':
            self.rating = content
        elif self.CurrentData == 'stars':
            self.stars = content
        elif self.CurrentData == 'description':
            self.description = content


if __name__ == '__main__':
    # create xml reader
    parser = xml.sax.make_parser()
    # turn off namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override ContentHandler
    Handler = MoviesHandler()
    parser.setContentHandler(Handler)

    # start to parser
    parser.parse("movies.xml")
