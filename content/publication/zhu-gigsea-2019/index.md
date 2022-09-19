---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'GIGSEA: genotype imputed gene set enrichment analysis using GWAS summary level
  data'
subtitle: ''
summary: ''
authors:
- Shijia Zhu
- Tongqi Qian
- Yujin Hoshida
- Yuan Shen
- Jing Yu
- Ke Hao
tags:
- '"Computational Biology"'
- '"Polymorphism"'
- '"Single Nucleotide"'
- '"Software"'
- '"Genome-Wide Association Study"'
- '"Genotype"'
- '"Quantitative Trait Loci"'
- '"Linear Models"'
categories: []
date: '2019-01-01'
lastmod: 2021-11-01T08:41:48-04:00
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
publishDate: '2021-11-01T12:41:48.128101Z'
publication_types:
- '2'
abstract: 'Summary: level data of GWAS becomes increasingly important in post-GWAS
  data mining. Here, we present GIGSEA (Genotype Imputed Gene Set Enrichment Analysis),
  a novel method that uses GWAS summary statistics and eQTL to infer differential
  gene expression and interrogate gene set enrichment for the trait-associated SNPs.
  By incorporating empirical eQTL of the disease relevant tissue, GIGSEA naturally
  accounts for factors such as gene size, gene boundary, SNP distal regulation and
  multiple-marker regulation. The weighted linear regression model was used to perform
  the enrichment test, properly adjusting for imputation accuracy, model incompleteness
  and redundancy in different gene sets. The significance level of enrichment is assessed
  by the permutation test, where matrix operation was employed to dramatically improve
  computation speed. GIGSEA has appropriate type I error rates, and discovers the
  plausible biological findings on the real data set. Availability and implementation:
  GIGSEA is implemented in R, and freely available at www.github.com/zhushijia/GIGSEA.
  Supplementary information: Supplementary data are available at Bioinformatics online.'
publication: '*Bioinformatics (Oxford, England)*'
doi: 10.1093/bioinformatics/bty529
---
