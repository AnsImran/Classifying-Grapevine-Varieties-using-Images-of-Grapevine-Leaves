# Classifying-Grapevine-Varieties-Using-images-of-Grapevine-Leaves 
_Note: There are 2 notebooks [grapevine_leaves_classification.ipynb](grapevine_leaves_classification.ipynb) (models were initially created and ensembled here) and [production.ipynb](production.ipynb) (already saved models were loaded and used in production)_


### I have tried to classify Grapevine varieties using images of leaves of different varieties of Grapevine
### Motivations:
Large catalogs of unlabelled stellar objects are available. Labelling these stellar objects is important for a number of reasons. E.g: for statistical poulation analyses and for [testing cosmological models](https://academic.oup.com/mnras/article/444/1/2/1016765) to name a few. Although these stellar objects can be classified by analyzing their optical spectrums but that process is time consuming. [Next generation of telescopes](https://ui.adsabs.harvard.edu/abs/2019ApJ...873..111I/abstract) will increase the quantity of available unlabelled data even more! That's why we have tried to use the photometric data and a combination of machine learning approaches to label the stellar objects.

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

### Features Used
| Feature Name   | Description                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| u             | Ultraviolet filter in the photometric system                                                                   |
| g             | Green filter in the photometric system                                                                        |
| r             | Red filter in the photometric system                                                                          |
| i             | Near Infrared filter in the photometric system                                                                |
| z             | Infrared filter in the photometric system                                                                     |
| redshift      | Redshift value based on the increase in wavelength                                                            |
| class         | Object class (galaxy, star, or quasar object)                                                                 |


### Skills demonstarted:

(pandas, numpy, tensorflow/keras, scikit-learn & matplotlib)

## [Based on Kaggle Dataset](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17)

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
