## End-to-End Computer Vision Project

#### Skills demonstarted:
(pandas, numpy, tensorflow, scikit-learn, matplotlib, fastapi, docker, dev-container, convolutional-neural-networks, call-backs)

### [Data Cleaning, Augmentation and Processing](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### [Visualizing Data before and after Augmentation](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### [Setting Up Baseline Performance](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### [Transfer Learning - Feature Extraction](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### [Transfer Learning - Fine Tuning](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### [Deploying the Model Using Fast-Api](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/tree/master/04_Deployment)

### [Future Improvements?](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

---
## Deployment Snapshot (fast-api)
![4](05_Results_Screenshots/cv_app_api_in_action.JPG)

---
## Further details about this Project

### Classifying-Grapevine-Varieties-Using-images-of-Grapevine-Leaves 

#### The project tries to classify grapevine varieties based on the images of their leaves.

### Motivation:
The dataset contained 500 pictures of grapevine leaves representing 5 different species. I utilized convolutional neural networks for multiclass classification on this dataset. The purpose of this project is to highlight and demonstrate my proficiency in Artificial Intelligence within the realm of computer vision. This work holds potential applications in agricultural automation.

### [Based on Kaggle Dataset](https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset/data)



## Table of Contents [grapevine_leaves_classification.ipynb](https://github.com/AnsImran/Classifying-Grapevine-Varieties-using-Images-of-Grapevine-Leaves/blob/master/02_Data_Processing__and__Model_Training/grapevine_leaves_classification.ipynb)

### 1. Importing data
   - ##### Importing data from kaggle
   - ##### Unzipping the data

### 2. Data Cleaning
   - ##### Addressing Class Imbalance

### 3. Data Transfer
   - ##### Creating relevant directories & transferring the data (train, test and validation splits)

### 4. Data Augmentation & Processing
   - ##### Setting up generators to Augment & Process the data

### 5. Data Visualisation
   - ##### Visualizing typical images in the data before & after Augmentation

### 6. Setting up a baseline performance
   - #####  Using a small convnet, setting up a baseline performance

### 7. Transfer Learning
 - #### Feature Extracton With Data Augmentation
   - ##### Freezing Convolutional Base
   - ##### Adding the Classifier Base
   - ##### Setting Up Callbacks
   - ##### Compiling & Training The Model
   - ##### Selecting the best set of weights by comparing the performance on Training, Validation & Test Datasets
   - ##### Generating Classification Report and Confusion Matrix on Test Dataset

 - #### Fine Tuning
   - ##### Unfreezing last two layers of Convolutional Base
   - ##### Adding the Classifier Base
   - ##### Setting Up Callbacks
   - ##### Compiling & Training The Model
   - ##### Selecting the best set of weights by comparing the performance on Training, Validation & Test Datasets
   - ##### Generating Classification Report and Confusion Matrix on Test Dataset

### 8. Conclusions & Future Improvements



### Results
The results were:
- For objects correctly_classified as Ak, 95% of them had a probability greater than 0.9 of being Ak.
- For objects correctly_classified as Ala_Idris, 84.2% of them had a probability greater than 0.9 of being Ala_Idris.
- For objects correctly_classified as Buzgulu, 77.7% of them had a probability greater than 0.9 of being Buzgulu.
- For objects correctly_classified as Dimnit, 76.4% of them had a probability greater than 0.9 of being Dimnit.
- For objects correctly_classified as Nazli, 95% of them had a probability greater than 0.9 of being Nazli.
- 
### Screenshots from the notebook [grapevine_leaves_classification.ipynb](grapevine_leaves_classification.ipynb):
![4](05_Results_Screenshots/1.PNG)
![1](05_Results_Screenshots/2.PNG)
![2](05_Results_Screenshots/3.PNG)
![3](05_Results_Screenshots/4.PNG)


