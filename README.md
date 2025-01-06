# Monitoring Plant Health and Diseases for Sustainable Agriculture 🌾🌱
Revolutionizing sustainable agriculture, this project empowers farmers and researchers to combat wheat plant diseases using cutting-edge AI techniques.

## About the Project
- **Researched & Built** the largest Wheat Disease Dataset with 14,000+ images, aiding in accurate disease diagnosis.
- **Developed** a CNN-based model with 91% accuracy, further enhanced by integrating Random Forest and Decision Tree classifiers using symptom-based user input.
- **Created** a real-time disease identification dashboard, reducing diagnosis time and cutting crop loss.
- **Leveraged AI** to provide detailed disease insights and user feedback, refining diagnosis precision and enabling timely interventions.

## About the Dataset

### Wheat Plant Diseases Dataset
#### <a target="_blank" href="https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases">Dataset Link</a>
```
https://www.kaggle.com/datasets/kushagra3204/wheat-plant-diseases
```
This dataset is designed to empower researchers and developers in creating robust machine learning models for classifying various wheat plant diseases. It offers a collection of high-resolution images showcasing real-world wheat diseases without the use of artificial augmentation techniques.

#### Content
- **Number of Images:** 14,155
- **Image Quality:** High-resolution images
- **Disease Classes:**
    - Aphid [Pest]
    - Mite [Pest]
    - Stem Fly [Pest]
    - Rusts
        - Black Rust / Stem Rust
        - Brown Rust / Leaf Rust
        - Yellow Rust / Stripe Rust
    - Smut (Loose, Flag)
    - Common Root Rot
    - Helminthosporium Leaf Blight / Leaf Blight
    - Wheat Blast
    - Fusarium head blight / Scab
    - Septoria Leaf Blotch
    - Spot Blotch
    - Tan Spot
    - Powdery Mildew

#### Disease Cause and Monitoring Information
- **Wheat Disease Cause:** Wheat plants can contract diseases from various sources, including fungi, bacteria, viruses, and environmental conditions.
- **Disease Monitoring Using Images:** This guide provides valuable information on leveraging visual inspection of wheat plants and dataset images for disease identification.

#### Benefits
- **Large and Diverse:** With over 14,155 high-quality images, the dataset provides a substantial foundation for training and testing machine learning models.
- **Real-world Images:** The absence of artificial augmentation ensures the images represent natural variations of diseases, leading to improved model generalizability.
- **Comprehensive Disease Coverage:** The inclusion of a wide range of wheat disease types allows for the development of models that can identify a broad spectrum of threats.
- **Monitoring Guidance:** The additional information on disease causes and image-based monitoring empowers users to leverage the dataset for practical applications in real-world scenarios.

## Directory Structure
```
kushagra3204-Plant-Disease-Monitoring/
├── backend/
│   ├── app.py
│   ├── .gitignore
│   ├── .gitattributes
│   ├── evaluation/
│   │   └── analysis.py
│   ├── labels/
│   │   ├── labels_train.csv
│   │   └── labels_test.csv
│   ├── predict.py
│   ├── vercel.json
│   ├── preprocess/
│   │   ├── add_image_label_to_csv.py
│   │   ├── ArrangeImages.py
│   │   └── model_conversion_h5_2_tflite.py
│   ├── requirements.txt
│   ├── train.py
│   └── model/
│       └── model_new.tflite
├── frontend/
│   ├── .gitignore
│   ├── public/
│   │   ├── manifest.json
│   │   ├── index.html
│   │   └── robots.txt
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── src/
│       ├── setupTests.js
│       ├── index.css
│       ├── assets/
│       │   └── index.js
│       ├── components/
│       │   └── FileUploader.jsx
│       ├── App.js
│       ├── reportWebVitals.js
│       ├── App.css
│       ├── App.test.js
│       └── index.js
└── README.md
```

## Steps to Run the Code

### Prerequisites
- Python 3.8+ and Node.js installed.

### Backend
1. Navigate to the backend/ directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (if needed):
   ```bash
   python train.py
   ```
4. Start the backend server:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to the frontend/ directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend server:
   ```bash
   npm start
   ```

Access the dashboard at http://localhost:3000.

## Future Scope
- **Expand the dataset** to include more diverse images and disease types.
- **Improve model accuracy** by experimenting with different architectures and hyperparameters.
- **Integrate additional machine learning techniques** for better disease prediction and classification.
- **Develop a mobile application** for real-time disease diagnosis in the field.

## Collaborators
We warmly invite researchers, developers, and enthusiasts from around the world to join us in making this project even more impactful. Your unique skills and ideas can help elevate this work to new heights, revolutionizing the field of plant disease detection and sustainable agriculture.

Whether you're contributing code, refining models, expanding datasets, or sharing feedback, your collaboration is invaluable in advancing this mission. Together, we can create a groundbreaking tool that empowers farmers, protects crops, and fosters a healthier planet.

Let’s work together to push the boundaries of innovation and take this remarkable project to extraordinary levels of excellence! Feel free to fork the repository, raise issues, or submit pull requests—we’re excited to collaborate with you!
## Keywords and Tags
**Keywords:** Plant Disease Monitoring, CNN, Wheat Disease Dataset, Sustainable Agriculture, Machine Learning, AI in Agriculture, Disease Diagnosis, Real-time Identification, Plant Health, AI in Farming, Deep Learning, Agriculture Technology

**Tags:** #PlantHealth #Agriculture #MachineLearning #CNN #WheatDisease #AI #SustainableAgriculture #DataScience #DeepLearning #SmartFarming #PlantDiseaseAI #WheatHealth #DeepLearningInAg #AIForGood #AgricultureTech #InnovationInFarming #CropProtection #FoodSecurity

