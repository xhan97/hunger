# Copyright 2022 Xin Han
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest

from sklearn.datasets import load_iris, load_wine, load_diabetes
from sklearn.preprocessing import MinMaxScaler

from hunger.metrics import dendrogram_purity, _get_parent, _get_node_purity

from scipy.cluster.hierarchy import dendrogram, linkage


@pytest.fixture
def data():
    return load_wine(return_X_y=True)


def test_dendrogram_purity(data):
    X, y = data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    Z = linkage(X, 'single')
    dp_score = dendrogram_purity(Z, y)
    print(dp_score)


def test_find_parent(data):
    X, y = data
    Z = linkage(X, 'single')
    n = len(X)
    parent_mat = _get_parent(Z, n)


def test_find_tc_index(data):
    X, y = data
    Z = linkage(X, 'single')
    n = len(X)
    parent_mat = _get_parent(Z, n)
    _get_node_purity(parent_mat, y)
