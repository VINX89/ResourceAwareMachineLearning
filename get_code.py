from __future__ import print_function

import os
import subprocess

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz



def get_code(tree, feature_names, target_names, spacer_base="    "):
    """Produce psuedo-code for decision tree.
        
        Args
        ----
        tree -- scikit-leant DescisionTree.
        feature_names -- list of feature names.
        target_names -- list of target (class) names.
        spacer_base -- used for spacing code (default: "    ").
        
        Notes
        -----
        based on http://stackoverflow.com/a/30104792.
        """
    left      = tree.tree_.children_left
    right     = tree.tree_.children_right
    threshold = tree.tree_.threshold
#    print(tree.tree_.feature)
#    print(feature_names)
    features  = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value
    
    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if (threshold[node] != -2):
            print(spacer + "if ( 2*" + features[node] + " <= " + str(int(2*threshold[node])) + " ) {")
            if left[node] != -1:
                recurse(left, right, threshold, features, left[node], depth+1)
            print(spacer + "}\n" + spacer +"else {")
            if right[node] != -1:
                recurse(left, right, threshold, features, right[node], depth+1)
            print(spacer + "}")
        else:
            target = value[node]
            target_count_vec = []
            target_name_vec = []
            for i, v in zip(np.nonzero(target)[1], target[np.nonzero(target)]):
                target_name = target_names[i]
                target_count = int(v)
                target_count_vec.append(target_count)
                target_name_vec.append(target_name)

            index = target_count_vec.index(min(target_count_vec))
            target_name = target_name_vec[index]
            print(spacer + "return " + str(int(target_name)) + ";" )

    recurse(left, right, threshold, features, 0, 0)
















