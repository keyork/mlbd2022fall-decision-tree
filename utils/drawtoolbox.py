"""
@ File Name     :   drawtoolbox.py
@ Time          :   2022/10/25
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   None
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""

from utils.toolbox import LOGGER


def draw_tree(data: dict, label: list, target_path: str):

    graph_info = [[], [], [], []]
    walk_dict(data, graph_info, label, "")
    with open(target_path, "w+") as f:
        f.write("```mermaid\n")
        f.write("graph TB\n")
        f.write("A0[ROOT] -->A1\n")
        f.writelines(graph_info[0])
        f.write("```\n")
    print("Tree -> {}".format(target_path))
    # print("-" * 10)
    LOGGER.info("NOTE")
    print("Using mermaid in Markdown to plot the tree.")
    print("To see the result, you may need to install the plugin: ")
    print("     |Markdown Preview Mermaid Support|")
    print("in Microsoft Visual Studio Code,")
    print("or other tools to render markdown.")


def walk_dict(data: dict, graph_info: list, label: list, root: str):

    for key in data.keys():

        sub_data = data[key]

        if key in label:
            graph_info[1].append(key)
            key_label = "A{}".format(len(graph_info[1]))
            graph_info[0].append("{}({})\n".format(key_label, key))
            walk_dict(sub_data, graph_info, label, key_label)
        else:
            # class
            graph_info[2].append(key)
            if isinstance(sub_data, dict):
                # still dict
                subdata_label = "A{}".format(len(graph_info[1]) + 1)
                graph_info[0].append("{} -->|{}|{}\n".format(root, key, subdata_label))
                walk_dict(sub_data, graph_info, label, root)
            else:
                # yes / no
                graph_info[3].append(sub_data)
                judge_label = "C{}".format(len(graph_info[3]))
                graph_info[0].append("{}(({}))\n".format(judge_label, sub_data))
                graph_info[0].append("{} -->|{}|{}\n".format(root, key, judge_label))
