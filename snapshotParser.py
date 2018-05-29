#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import xml.sax


class SnapshotParser(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.CurrentAttributes = ""
        self.name = ''
        self.path = ''

    def startElement(self, tag, attr):
        self.CurrentData = tag
        self.CurrentAttributes = attr
        if tag == 'manifest':
            print('****** start parser ******')
        if tag == 'project':
            self.name = attr['name']

    def endElement(self, name):
        if self.CurrentData == 'project':
            print('project name %s' % self.name)
            branch_info = json.dumps(self.name)
            if not os.path.isfile('./info.txt'):
                with open('./info.txt', 'a') as f:
                    f.write(branch_info)
                    f.write('\n')
        self.CurrentData = ''
        self.name = ''
        self.path = ''

    def characters(self, content):
        pass


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    snapshot_handler = SnapshotParser()
    parser.setContentHandler(snapshot_handler)

    parser.parse('snapshot.xml')
