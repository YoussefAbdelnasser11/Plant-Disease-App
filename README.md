# 🌿 Plant Disease Classifier

A deep learning-powered web application that classifies plant diseases from leaf images using a trained Convolutional Neural Network (CNN). This tool can help farmers, researchers, and agricultural experts to quickly identify diseases in crops.

![Plant Disease Classifier Screenshot](./screenshot.png)

---

## 📌 Features

- ✅ Image upload and real-time disease prediction.
- 🧠 Trained on the PlantVillage dataset.
- 🪴 Supports 38 different plant disease categories.
- 💻 Built with Streamlit for an interactive UI.
- 📊 Uses a CNN model for accurate classification.
- ⚙️ Easy to run locally or deploy online.

---

## 📂 Dataset

- **Source:** [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
- **Categories:** Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato.
- **Labels Example:**
  - `Apple___Black_rot`
  - `Potato___Early_blight`
  - `Tomato___Leaf_Mold`
  - `Soybean___healthy`
  - ... and 34 more.

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/plant-disease-classifier.git
   cd plant-disease-classifier
## 🛠️ Folder Structure
plant-disease-app/
├── app.py
├── requirements.txt
├── class_indices.json
├── .gitignore
└── utils/
    └── download_model.py  

