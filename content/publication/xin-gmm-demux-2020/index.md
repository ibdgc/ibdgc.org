---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'GMM-Demux: sample demultiplexing, multiplet detection, experiment planning,
  and novel cell-type verification in single cell sequencing'
subtitle: ''
summary: ''
authors:
- Hongyi Xin
- Qiuyu Lian
- Yale Jiang
- Jiadi Luo
- Xinjun Wang
- Carla Erb
- Zhongli Xu
- Xiaoyi Zhang
- Elisa Heidrich-O'Hare
- Qi Yan
- Richard H. Duerr
- Kong Chen
- Wei Chen
tags:
- '"Demultiplex"'
- '"Multiplets"'
- '"Phony cell type"'
- '"Rare cell type"'
- '"Sample barcoding"'
- '"Single cell RNA"'
categories: []
date: '2020-07-01'
lastmod: 2021-11-01T08:41:41-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-11-01T12:41:41.022040Z'
publication_types:
- '2'
abstract: Identifying and removing multiplets are essential to improving the scalability
  and the reliability of single cell RNA sequencing (scRNA-seq). Multiplets create
  artificial cell types in the dataset. We propose a Gaussian mixture model-based
  multiplet identification method, GMM-Demux. GMM-Demux accurately identifies and
  removes multiplets through sample barcoding, including cell hashing and MULTI-seq.
  GMM-Demux uses a droplet formation model to authenticate putative cell types discovered
  from a scRNA-seq dataset. We generate two in-house cell-hashing datasets and compared
  GMM-Demux against three state-of-the-art sample barcoding classifiers. We show that
  GMM-Demux is stable and highly accurate and recognizes 9 multiplet-induced fake
  cell types in a PBMC dataset.
publication: '*Genome Biology*'
doi: 10.1186/s13059-020-02084-2
---
