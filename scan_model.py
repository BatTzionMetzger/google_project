import os
import pickle
import sys


def scan_file(tree, path):
    with open(path, 'r', encoding='utf-8') as file:
        tree.add_lines_to_tree(path, file.readlines())


def scan_directory(tree, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            scan_file(tree, os.path.join(root, file))


def create_pkl_file(tree):
    max_rec = 0x100000
    sys.setrecursionlimit(max_rec)
    with open('tree.pkl', 'wb') as output:
        pickle.dump(tree, output, pickle.HIGHEST_PROTOCOL)
