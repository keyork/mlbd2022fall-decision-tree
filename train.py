"""
@ File Name     :   train.py
@ Time          :   2022/10/25
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   None
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""

from data.dataset import DATA, LABEL
from model.decisiontree import DecisionTree
from utils.drawtoolbox import draw_tree


def train():

    model = DecisionTree(DATA, LABEL)
    model.tree = model.tree_handler(model.data, 0)
    return model.tree


def main():

    dec_tree = train()
    draw_tree(dec_tree, LABEL, "./img/demo.md")


if __name__ == "__main__":
    main()
