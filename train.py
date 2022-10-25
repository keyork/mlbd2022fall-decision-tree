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

import argparse

from data.dataset import DATA, LABEL
from model.decisiontree import DecisionTree
from utils.drawtoolbox import draw_tree
from utils.toolbox import LOGGER, str2bool


def train(config):

    model = DecisionTree(
        DATA[config.test_data_id], LABEL[config.test_data_id], config.show_entropy
    )
    print("----------------------------------")
    print("           Entropy  Log           ")
    model.tree = model.tree_handler(model.data, 0)
    print("----------------------------------")
    print(model.tree)
    return model.tree


def main(config):

    LOGGER.info("config list")
    print("\ttarget_path: {}".format(config.target_path))
    print("\ttest_data_id: {}".format(config.test_data_id))
    print("\tshow_entropy: {}".format(config.show_entropy))

    LOGGER.info("Start Decision Tree")
    dec_tree = train(config)
    LOGGER.info("Draw Tree")
    result_path = config.target_path + "result_dataset-{}.md".format(
        config.test_data_id
    )
    draw_tree(dec_tree, LABEL[config.test_data_id], result_path)


if __name__ == "__main__":
    LOGGER.warning("Start!")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target_path", type=str, default="./img/", help="save result path"
    )
    parser.add_argument(
        "--test_data_id", type=int, default=0, help="test data id(0 or 1)"
    )
    parser.add_argument(
        "--show_entropy", type=str2bool, default=True, help="show entropy or not"
    )
    args = parser.parse_args()

    main(args)

    LOGGER.warning("Done!")
