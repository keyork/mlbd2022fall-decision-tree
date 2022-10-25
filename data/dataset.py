"""
@ File Name     :   dataset.py
@ Time          :   2022/10/24
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

DATA = []
LABEL = []
DATA.append(
    pd.DataFrame(
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
)

LABEL.append(["fashion", "situation", "price"])

DATA.append(
    pd.DataFrame(
        np.array(
            [
                [">5", "=3", "long", "high", "setosa"],
                [">5", "<3", "long", "low", "versicolor"],
                ["<5", "<3", "short", "high", "setosa"],
                ["<5", "<3", "long", "low", "versicolor"],
                [">5", ">3", "short", "low", "setosa"],
                ["<5", "<3", "short", "low", "virginica"],
                [">5", ">3", "long", "high", "virginica"],
                ["=5", ">3", "long", "low", "virginica"],
                ["=5", ">3", "long", "high", "virginica"],
                ["<5", "<3", "short", "low", "setosa"],
                [">5", "<3", "short", "high", "versicolor"],
                ["=5", "<3", "short", "low", "setosa"],
                ["<5", "=3", "long", "low", "versicolor"],
                [">5", ">3", "long", "high", "setosa"],
                [">5", ">3", "short", "low", "setosa"],
                ["<5", "<3", "short", "low", "setosa"],
                [">5", "<3", "short", "high", "versicolor"],
                ["=5", "<3", "short", "low", "setosa"],
                ["<5", "=3", "long", "low", "versicolor"],
                [">5", "=3", "long", "high", "setosa"],
                [">5", "<3", "long", "low", "versicolor"],
                ["<5", "<3", "short", "high", "setosa"],
                ["<5", "<3", "long", "low", "versicolor"],
                [">5", ">3", "short", "low", "setosa"],
            ]
        )
    )
)

LABEL.append(["sepal length / cm", "sepal width / cm", "petal length", "height"])
