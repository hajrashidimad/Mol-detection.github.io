
## Challenge
The main goal is to deploy a camputer vision model that can detect if a given mole image is cancerous or not.

#### The Mission

"skinCare", a health care company need a tool that would be able to detect moles that need to be handle by doctors.   
For that, they ask us to build an AI model that can detect when the mole is dangerous. To be able to use the AI, it must be deployed in a simple web page where the user could upload a picture of the mole and see the result.


#### Objectives
   
- Be able to apply a CNN in a real context
- Be able to preprocess data for computer vision


## The dataset
The dataset is avalaible on this [URL](https://we.tl/t-uHuOlrbaC2). It contain 3 sets of image and an excel file that contains clinical diagnostic of the moles. The total amount of images in this dataset is 2937.   
Images are in colour (RGB) and each of them have a size of (387, 632, 3).   
 

#### The dataset

- Shape: (3000, 6) 
- Missing values : 63

<details>
  <summary>More details</summary>

![View file](assets/dts.png)


</details>  
   

#### Images

- High: 387
- Width: 632
- Color: 3

![View file](assets/mole.png)
 


## Preprocessing
This step understand many sub-steps: 

### The dataset
For the dataset, a classic preprocessing is made.   
We first check the unique values of the target `kat.Diagnose` and then replace and regroup them into two categories: `Benign` and `Malignant`.  
From the preprocessed one, we filter our images from the different sets.   

### Mole images
After saving them into two main folders (train and test), we now re-upload them into: `benign_train`, `malign_train`, `benign_test`, `malign_test`; by resizing them (224,224,3).  
The following steps are creating labels, converting to numerical values and splitting into train test variables.   
As the dataset is highly imbalanced (far more Malignant than Benign), we then use a generator to automatically generate modified image from the original one and then provide a balanced train test sets.



## The model
This step is not the easiest but can be considered as the simplest one!  
We choose a simple baseline, simple but good enough, as our model to detect cancerous mole.  
The model has 6 layers (input, output and 4 hidden layers). For the hidden layers, we use a GlobalAveragePooling2D layer, a dense layer, a Dropout layer and finally a BatchNormalization layer. With an input shape = (224, 224, 3) and an output of 2.

<details>
  <summary>More details</summary>

![View file](assets/summ.png)

</details>  

   
### Some parameters   
    - Optimizer =  Adam
    - Learning rate = 0.001
    - loss = binary_crossentropy 
    - metrics = accuracy
    - epochs = 20
 

### Score
Now it comes to fit the model with our train sets.  
The first results are satisfying even if it can be more improved.   

``Test Accuracy = 0.8064865``  

You can see below the `Accuracy` and `Loss` graphs of the train sets.

![View file](assets/accu.png)   


![View file](assets/loss.png)   


## Installation
This project is made with  Google Colab.
So almost all the requirements are already there except the followings:
- efficientnet (_!pip install -U efficientnet_)



## Authors

- [Abdellah El ghilbzouri](https://github.com/abdellahML)
- [Haj Rashid Imad](https://github.com/hajrashidimad)
- [Ousmane DIOP](https://github.com/Nooreyni)
- [Reza Nasrollahi](https://github.com/RezaNasrollahi)

__becode - Liege, Thomas 1.26 - 2021__