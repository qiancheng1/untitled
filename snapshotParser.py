#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import json
import os
import xml.sax

from numpy.f2py.crackfortran import requiredpattern


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
            # print('project name %s' % self.name)
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

    def get_info(self,brname1,brname2):
        with open('./info.txt', 'r') as fr:
            for line in fr:
                project = json.loads(line)
                print(project,brname1,brname2)
                # ssh -p 29418 10.0.30.9 gerrit create-branch "$project" "$new_branch_name" "old_branch"
                # os.popen('ssh -p 29418 10.0.30.9 gerrit create-branch "%s" "%s" "%s" % (project,brname1,brname2)')
        fr.close()
        os.remove('./info.txt')


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    snapshot_handler = SnapshotParser()
    parser.setContentHandler(snapshot_handler)

    parser.parse('snapshot.xml')

    # 创建一个命令解析器的句柄
    mArgsParser = argparse.ArgumentParser()
    mArgsParser.add_argument(
        '--new_branch',
        help='type new branch name',
        required = True
    )
    mArgsParser.add_argument(
        '--old_branch',
        help='type old branch name',
        required = True
    )

    args = mArgsParser.parse_args()
    print(args)
    if args.new_branch is not None:
        mNewbranch = args.new_branch
        print(mNewbranch)
    else:
        pass
    if args.old_branch is not None:
        mOldbranch = args.old_branch
        print(mOldbranch)
    else:
        pass

    snapshot_handler.get_info(mNewbranch,mOldbranch)
