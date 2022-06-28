.. -*- mode: rst -*-

HUNGER- Hierarchical Clustering Evaluation Library
============================================================
**HUNGER** is a python library for evaluating Hierarchical Clustering.
It includes serveral metrics for evaluating Hierarchical Clustering.
All metrics is designed for using dendrogram which see also in `scipy.cluster.hierarchy.dendrogram`.

Supported metrics
-----------------------------

* Dendrogram Purity

Installing
----------------------------
PyPI install, presuming you have an up to date pip.

.. .. code:: bash

..    pip install hunger

.. For a manual install of the latest code directly from GitHub:

.. .. code:: bash

..     pip install git+https://github.com/xhan97/hunger.git


Alternatively download the package, install requirements, and manually run the installer:

.. code:: bash

    wget https://codeload.github.com/xhan97/hunger/zip/refs/heads/master
    unzip hunger-master.zip
    rm hunger-master.zip
    cd hunger-master

    pip install -r requirements.txt

    python setup.py install

How to use HUNGER
------------------
.. code:: python

    from hunger.metrics import dendrogram_purity
    from sklearn.datasets import load_wine
    from scipy.cluster.hierarchy import linkage
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    X, y = load_wine(return_X_y=True)
    X = scaler.fit_transform(X)
    Z = linkage(X, 'single')
    dp_score = dendrogram_purity(Z, y)


To Do
_____
* F1 Score
* Dasgupta Cost


