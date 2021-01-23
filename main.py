import pickle
import sys
from Tree import Tree
from scan_model import scan_directory, create_pkl_file, scan_file
from string_manipulations import clear_text
if __name__ == '__main__':
    print("Loading the files and preparing the system..")
    tree = Tree()
    # scan_file(tree, "C:/Users/User/Downloads/aechive/a.txt")
    # create_pkl_file(tree)
    with open('tree.pkl', 'rb') as input_file:
        tree = pickle.load(input_file)
        while True:
            text = input("The system is ready enter your text: ")
            while text[len(text) - 1] != '#':
                text = clear_text(text)
                results = tree.find_best_match(tree.root, text)
                print("Here are 5 suggestions")
                for index, item in enumerate(results):
                    #print(item)
                    print("{}. {} ({})".format(index + 1, item[1], item[0]))
                text += " "
                text += input(text)