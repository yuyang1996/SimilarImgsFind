# SimilarImgsFind
一个基于imagededup的图片查重GUI工具

此项目依赖了imagededup

pip install imagededup

打包成exe命令
实测python3.9.13可用
pyinstaller -F -w -n  图片查重  main.py --add-data="icon.png;." --hidden-import sklearn.metrics._pairwise_distances_reduction._base --hidden-import sklearn.metrics._pairwise_distances_reduction._datasets_pair --hidden-import sklearn.metrics._pairwise_distances_reduction._middle_term_computer --hidden-import sklearn.metrics._pairwise_distances_reduction._radius_neighbors
