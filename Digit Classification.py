
"""

# read MNIST digits classification dataset
from tensorflow import keras

(data_train, out_train), (data_test, out_test) = keras.datasets.mnist.load_data(path="mnist.npz")
(data_train.shape, out_train.shape, data_test.shape, out_test.shape)

"""# Preprocessing"""

# Transformation
in_train = data_train/255.0
in_test = data_test/255.0
in_train.min(), in_train.max(), in_test.min(), in_test.max()

# EDA on out
#out_train.min(), out_train.max(), out_test.min(), out_test.max()
import numpy as np
np.unique(out_train), np.unique(out_test)

# Enumerate out classes
class_names = {
0 : 'Zero',
1	: 'One',
2	: 'Two',
3	: 'Three',
4	: 'Four',
5	: 'Five',
6	: 'Six',
7	: 'Seven',
8	: 'Eight',
9	: 'Nine'}
print(class_names)

"""# Training Set"""

# Define Function to display Images
import math
import matplotlib.pyplot as plt

def plot(images, labels, predictions=None):
    n_cols = min(10, len(images))
    n_rows = math.ceil(len(images)/n_cols)
    fig, axes = plt.subplots(n_rows,n_cols, figsize=(n_cols+3,n_rows+2))
    if predictions is None:
        predictions = [None] * len(labels)
    for index, (image, label,label_pred) in enumerate(zip(images,labels,predictions)):
        ax = axes.flat[index]
        ax.imshow(image,cmap=plt.cm.binary)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(class_names[label])
        if label_pred is not None:
            ax.set_xlabel(class_names[label_pred])

# Prompting user for number of rows to review for training images
num_rows_train = int(input('How many rows of training images (in 10 images per row) would you like to review? '))
plot(in_train[:num_rows_train * 10], out_train[:num_rows_train * 10])

"""# Model in Keras"""

#Generating Models
model1 = keras.Sequential(layers=[
    keras.layers.Flatten(input_shape=[28,28]),
    keras.layers.Dense(500,activation='sigmoid'),
    keras.layers.Dense(10,activation='softmax')
    ])
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
# https://keras.io/api/metrics/
# https://www.tensorflow.org/api_docs/python/tf/keras/losses
model1.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model1.fit(in_train,out_train,batch_size=60,epochs=2,validation_split=0.2) #Original Model from ACT

model2 = keras.Sequential(layers=[
    keras.layers.Flatten(input_shape=[28,28]),
    keras.layers.Dense(500,activation='sigmoid'),
    keras.layers.Dense(10,activation='softmax')
    ])
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
# https://keras.io/api/metrics/
# https://www.tensorflow.org/api_docs/python/tf/keras/losses
model2.compile(optimizer='adadelta', # Changed the Optimizer to "adadelta"
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model2.fit(in_train,out_train,batch_size=80,epochs=2,validation_split=0.2) # Changed the batch_size

model3 = keras.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(500, activation='relu'),  # Changed the activation to "Relu"
    keras.layers.Dense(10, activation='softmax')
])
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
# https://keras.io/api/metrics/
# https://www.tensorflow.org/api_docs/python/tf/keras/losses
model3.compile(optimizer='sgd',  # Changed the Optimizer to "SGD"
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])
model3.fit(in_train, out_train, batch_size=128, epochs=10, validation_split=0.2)  # Changed the batch_size and epochs

model4 = keras.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(500, activation='relu'),  # Changed the activation to "Relu"
    keras.layers.Dense(10, activation='softmax')
])
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
# https://keras.io/api/metrics/
# https://www.tensorflow.org/api_docs/python/tf/keras/losses
model4.compile(optimizer='adamax',  # Changed the Optimizer to "adamax"
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])
model4.fit(in_train, out_train, batch_size=150, epochs=7, validation_split=0.15)  # Changed batch_size, epochs, and validation_split

model5 = keras.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(500, activation='sigmoid'),
    keras.layers.Dense(10, activation='softmax')
])
# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
# https://keras.io/api/metrics/
# https://www.tensorflow.org/api_docs/python/tf/keras/losses
model5.compile(optimizer='nadam',  # Changed the Optimmizer to "Nadam"
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])
model5.fit(in_train, out_train, batch_size=180, epochs=15, validation_split=0.1)  # Changed the batch_size, epochs, and validation_split

"""# Test Set"""

# Evaluating Models to find out highest accuracy; Model 5 yields highest accuracy, hence that is the best model
model1.evaluate(in_test,out_test)
model2.evaluate(in_test,out_test)
model3.evaluate(in_test,out_test)
model4.evaluate(in_test,out_test)
model5.evaluate(in_test,out_test)

# Predictions
probs = model5.predict(in_test)

preds = probs.argmax(axis=1)
preds

# Prompting user for number of rows to review for test images
num_rows_test = int(input('How many rows of randomly selected test images (in 10 images per row) would you like to review? '))
plot(in_test[:num_rows_test * 10], out_test[:num_rows_test * 10], preds[:num_rows_test * 10])

"""# Application"""

import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import widgets, interact, Layout
img_idx_slider = widgets.IntSlider(value=0, min=0, max=len(in_test) - 1,
                                   description='Image Index',
                                   layout=Layout(width='100%'))
@interact(index=img_idx_slider)
def visualize_prediction(index=0):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(in_test[index], cmap=plt.cm.binary)
    ax1.set_title(f'Label: {class_names[out_test[index]]}')
    ax1.xaxis.tick_top()
    ax1.set_xlabel(f'Predict: {class_names[preds[index]]}')
    ax1.set_ylabel('Pixel Location Index')
    ax1.set_xticks(range(28))
    ax1.set_yticks(range(28))
    ax1.tick_params(axis='x', labelrotation=90)
    bar = sns.barplot(y=[class_names[ind] for ind in range(10)],
                      x=probs[index]*100)
    bar.set_xlim(0, 100)
    bar.set_xlabel('Probability (%)')
    bar.set_ylabel('Prediction Label')
    bar.set_title('Prediction Probabilities')
    fig.tight_layout()
    plt.show()
