#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import json
import os
import sys
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
            # print('project name %s' % self.name)
            branch_info = json.dumps(self.name)
            # if not os.path.isfile('./info.txt'):
            with open('./info.txt', 'a') as f:
                f.write(branch_info)
                f.write('\n')
            f.close()
        self.CurrentData = ''
        self.CurrentAttributes = ''
        self.name = ''
        self.path = ''

    def characters(self, content):
        pass

    def get_info(self, obranch, nbranch):
        with open('./info.txt', 'r') as fr:
            for line in fr:
                project = json.loads(line)
                print(project, obranch, nbranch)
                # ssh -p 29418 10.0.30.9 gerrit create-branch "$project" "$new_branch_name" "old_branch"
                os.popen('ssh -p 29418 10.0.30.9 gerrit create-branch "%s" "%s" "%s"' % (project,nbranch,obranch))
        fr.close()
        os.remove('./info.txt')


if __name__ == '__main__':

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    snapshot_handler = SnapshotParser()
    parser.setContentHandler(snapshot_handler)

    # Create a handle to start command parser
    mArgsParser = argparse.ArgumentParser()
    mArgsParser.add_argument(
        '--snapshot',
        help='type a exist snapshot at the same path with this script',
        required=True
    )
    mArgsParser.add_argument(
        '--new_branch',
        help='type a new branch name',
        required=True
    )
    mArgsParser.add_argument(
        '--old_branch',
        help='type a old branch name',
        required=True
    )

    args = mArgsParser.parse_args()
    if args.snapshot is not None:
        mSnapshot = args.snapshot
    else:
        print('snapshot is invalid')
        sys.exit(1)
    if args.old_branch and args.new_branch is not None:
        mNewbranch = args.new_branch
        mOldbranch = args.old_branch
        print("new branch: %s, old branch: %s" % (mNewbranch, mOldbranch))
    else:
        print('branch info is invalid')
        sys.exit(1)

    parser.parse(mSnapshot)
    snapshot_handler.get_info(mNewbranch, mOldbranch)
