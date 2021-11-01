---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Comparative performances of machine learning methods for classifying Crohn
  Disease patients using genome-wide genotyping data.
subtitle: ''
summary: ''
authors:
- Alberto Romagnoni
- Simon Jegou
- Kristel Van Steen
- Gilles Wainrib
- Jean-Pierre Hugot
tags: []
categories: []
date: '2019-07-01'
lastmod: 2021-11-01T08:41:10-04:00
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
publishDate: '2021-11-01T12:41:10.107662Z'
publication_types:
- '2'
abstract: 'Crohn Disease (CD) is a complex genetic disorder for which more than 140
  genes have been identified using genome wide association studies (GWAS). However,
  the genetic architecture of the trait remains largely unknown. The recent development
  of machine learning (ML) approaches incited us to apply them to classify healthy  and
  diseased people according to their genomic information. The Immunochip dataset containing
  18,227 CD patients and 34,050 healthy controls enrolled and genotyped by the international
  Inflammatory Bowel Disease genetic consortium (IIBDGC) has been re-analyzed using
  a set of ML methods: penalized logistic regression (LR), gradient boosted trees
  (GBT) and artificial neural networks (NN). The main score used to compare the methods
  was the Area Under the ROC Curve (AUC) statistics. The impact of quality control
  (QC), imputing and coding methods on LR results showed that QC methods and imputation
  of missing genotypes may artificially increase the scores. At the opposite, neither
  the patient/control ratio nor marker preselection or coding strategies significantly
  affected the results. LR methods, including Lasso, Ridge and ElasticNet provided
  similar results with a maximum AUC of 0.80. GBT methods like XGBoost, LightGBM and
  CatBoost, together with dense NN with one or more hidden layers, provided similar
  AUC values, suggesting limited epistatic effects in the genetic architecture of
  the trait. ML methods detected near all the genetic variants previously identified
  by GWAS among the best predictors plus additional predictors with lower effects.
  The robustness and complementarity of the different methods are also studied. Compared
  to LR, non-linear models such as GBT or NN may provide robust complementary approaches
  to identify and classify genetic markers.'
publication: '*Scientific reports*'
doi: 10.1038/s41598-019-46649-z
---
