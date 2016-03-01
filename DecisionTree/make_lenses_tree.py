# -*- coding=utf-8 -*-
"""
make_lenses_tree
Date: 16/2/27
Company: Copyright (c) 2016 Ninlgde co.,Ltd. All right reserved.
"""

import trees
import treePlotter as tp

__author__ = 'Ninlgde'

if __name__ == '__main__':
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree = trees.createTree(lenses, lensesLabels)
    trees.storeTree(lensesTree, 'lenses_tree.bin')
    tree = trees.grabTree('lenses_tree.bin')
    tp.createPlot(tree)
