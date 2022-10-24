"""
@ File Name     :   decisiontree.py
@ Time          :   2022/10/21
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   None
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""


import numpy as np
import pandas as pd

DATA = pd.DataFrame(
    np.array(
        [
            ["new", "good", "high", "yes"],
            ["new", "bad", "low", "no"],
            ["old", "medium", "high", "no"],
            ["old", "bad", "low", "no"],
            ["old", "good", "low", "yes"],
            ["new", "good", "low", "yes"],
            ["new", "bad", "high", "no"],
            ["old", "good", "low", "yes"],
            ["new", "medium", "high", "yes"],
            ["old", "bad", "low", "yes"],
            ["new", "medium", "high", "no"],
            ["new", "good", "low", "yes"],
            ["old", "good", "low", "yes"],
            ["new", "medium", "high", "no"],
            ["old", "bad", "low", "yes"],
        ]
    )
)

# DATA = pd.DataFrame(
#     np.array(
#         [
#             ["new", "yes"],
#             ["new", "yes"],
#             ["new", "yes"],
#             ["new", "no"],
#             ["new", "no"],
#             ["new", "no"],
#         ]
#     )
# )

LABEL = ["fashion", "situation", "price"]


class DecisionTree:
    def __init__(self, data, label):

        self.data = data
        self.label = label
        self.tree = {}
        self.feats = []

    def tree_handler(self, data, processed_num):
        processed_num += 1
        process_data = data

        if (
            len(process_data.iloc[:, process_data.shape[1] - 1].value_counts().index)
            == 1
        ):
            # all judge is yes/no
            # print(process_data.iloc[0, [process_data.shape[1] - 1]].values[0])
            return process_data.iloc[0, [process_data.shape[1] - 1]].values[0]

        if processed_num == self.data.shape[1]:
            # end tree
            return self.get_most_label(process_data)

        data_list = [
            process_data.iloc[:, [i, process_data.shape[1] - 1]]
            for i in range(process_data.shape[1] - 1)
        ]

        tree_node = self.grow_tree(data_list)
        dec_tree = {self.label[tree_node]: {}}
        sub_tree_list = process_data[tree_node].value_counts().index
        for sub_tree in list(sub_tree_list):
            sub_process_data = process_data.loc[process_data[tree_node] == sub_tree]
            sub_process_data = sub_process_data.drop(columns=[tree_node])
            dec_tree[self.label[tree_node]][sub_tree] = self.tree_handler(
                sub_process_data, processed_num
            )

        return dec_tree

    def grow_tree(self, data_list: list):
        """get min entropy, select the node

        Args:
            data_list (list): dataset [[data, y/n], ...]

        Returns:
            tree_node: id of min entropy
        """
        entropy_list = np.array([self.get_tree_entropy(data) for data in data_list])
        tree_node = data_list[
            int(np.argwhere(entropy_list == entropy_list.min()))
        ].columns.tolist()[0]
        return tree_node

    def get_tree_entropy(self, data: pd.DataFrame):
        """calculate entropy

        Args:
            data (pd.DataFrame): [data, y/n]

        Returns:
            tree_entropy: average entropy
        """
        data_num = len(data.iloc[:, 0])
        data_class_list = data.iloc[:, 0].value_counts()
        data_group = data.iloc[:, 1].groupby(data.iloc[:, 0]).value_counts()
        tree_entropy = 0
        for data_class in data_class_list.index:
            in_class_num = data_class_list[data_class]
            in_class = data_group[data_class]
            entropy = 0
            if len(in_class) == 1:
                # only yes or no
                pass
            else:
                for yn in in_class.index:
                    entropy += (
                        -(np.float32(in_class_num) / np.float32(data_num))
                        * (np.float32(in_class[yn]) / np.float32(in_class_num))
                        * np.log2(np.float32(in_class[yn]) / np.float32(in_class_num))
                    )
            tree_entropy += entropy
        return tree_entropy

    def get_most_label(self, data: pd.DataFrame):
        """if the top of the tree, return the max times

        Args:
            data (pd.DataFrame): dataset

        Returns:
            label: yes/no
        """
        data_group = data.value_counts()
        if data_group[0] >= data_group[1]:
            return data_group.index[0][0]
        else:
            return data_group.index[1][0]


if __name__ == "__main__":
    model = DecisionTree(DATA, LABEL)
    model.tree = model.tree_handler(model.data, 0)
    print(model.tree)
