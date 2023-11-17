# Classifying-Grapevine-Varieties-Using-images-of-Grapevine-Leaves 
_Note: There are 2 notebooks [grapevine_leaves_classification.ipynb](grapevine_leaves_classification.ipynb) (models were initially created and ensembled here) and [production.ipynb](production.ipynb) (already saved models were loaded and used in production)_


### I have tried to classify Grapevine varieties using images of leaves of different varieties of Grapevine

## [Based on Kaggle Dataset](https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset/data)

### Motivation:
Grapevines produce grapes, which are enjoyed fresh or used in various processed products. Additionally, grapevine leaves are harvested annually as a by-product. The specific species of grapevine leaves play a crucial role in determining both their price and taste.
Deep learning-based classification to analyze images of grapevine leaves. We focused on 500 vine leaves from 5 different species, captured using a specialized self-illuminating system. This innovative approach aims to enhance our understanding of grapevine leaf characteristics for improved classification and potential applications in the agricultural automation.

### Results
The results were:
- For objects correctly_classified as Quasars, 90.3% of them had a probability greater than 0.9 of being a Quasar.
- For objects correctly_classified as Galaxies, 86.7% of them had a probability greater than 0.9 of being a Galaxy.
- For objects correctly_classified as Stars, 99.6% of them had a probability greater than 0.9 of being a Star.
### Screenshots from the notebook [production.ipynb](production/production.ipynb):
![4](results_screenshots/4.PNG)
![1](results_screenshots/1.PNG)
![2](results_screenshots/2.PNG)
![3](results_screenshots/3.PNG)


### Skills demonstarted:

(pandas, numpy, tensorflow/keras, scikit-learn & matplotlib)


# Table of Contents (photometry.ipynb)

## 1. Importing data
   - ##### Importing data from kaggle
   - ##### Unzipping the data

## 2. Data Cleaning
   - ##### Addressing Class Imbalance

## 3. Data Transfer
   - ##### Creating relevant directories & transferring the data (train, test and validation splits)

## 4. Data Augmentation & Processing
   - ##### Setting up generators to Augment & Process the data

## 5. Data Visualisation
   - ##### Visualizing typical images in the data before & after Augmentation

## 6. Setting up a baseline performance
   - #####  Using a small convnet, setting up a baseline performance

## 5. Data Classification
 - ### Unsupervised Learning
   - ##### Gaussian Mixture Model - Clustering

 - ### Supervised Learning
   - ##### Neural Network
   - ##### XGBoost
   - ##### Random Forest 

## 4. Model Ensembling
   - ##### Simple-Random-Search for weight optimization

## 5. Conclusions

## 6. What's Next?
   - ##### How can we achieve this?
   - ##### Possible Limitations
