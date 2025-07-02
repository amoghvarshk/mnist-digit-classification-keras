# MNIST Digit Classification using Keras

This project builds and compares multiple dense neural networks using Keras on the classic **MNIST** dataset of handwritten digits. The goal is to optimize model architecture and training parameters for maximum classification accuracy.

## 📊 Problem Statement
Classify 28x28 grayscale images of digits (0–9) using neural networks and evaluate the performance of different optimizers, activations, and model configurations.

## 🧠 Models Built
Five different neural network models were created with varying:
- **Optimizers**: Adam, Adadelta, SGD, Adamax, Nadam
- **Activation Functions**: Sigmoid, ReLU
- **Batch Sizes**: 60 to 180
- **Epochs**: Up to 15

## ✅ Results
- **Best Validation Accuracy**: Achieved **~97.4%** using **Nadam optimizer** with ReLU activations  
- **Best Test Accuracy**: **97.6%**  
- Evaluation metrics included **loss**, **accuracy**, and visual predictions on test samples.

## 📈 Evaluation & Explainability
- Compared all models using training/validation accuracy
- Visualized test image predictions with confidence bars
- Built interactive visualization using `ipywidgets` and `seaborn`

## 🛠️ Technologies Used
- Python, NumPy, Matplotlib, Seaborn, ipywidgets  
- TensorFlow (Keras API)  
- Google Colab
