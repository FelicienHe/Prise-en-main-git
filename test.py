import numpy as np

"""
Ici on a modifé le code dans le but de le mettre dans le branch test
"""
class Dataset:

    """
    Dataset is a class composing of
        a dataset : a list of numpy array
    """

    def __init__(self, dataset, label):
        self.datasets = dataset
        self.labels = label

