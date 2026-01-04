# Chronic Kidney Disease Prediction using Logistic Regression

### **Project Title**
Chronic Kidney Disease Prediction

### **Problem Statement**
CKD is a critical health condition that often remains asymptomatic until the advanced stages. A machine learning-based approach to screen patients based on common lab metrics can help in early identification and management of the disease.

### **Objective**
To build a reliable diagnostic tool using **Logistic Regression** that classifies patients into "CKD" or "Not-CKD" categories based on clinical features like Creatinine levels, Hemoglobin, and Specific Gravity.

### **Dataset Description**
The project utilizes the **Chronic Kidney Disease Dataset**, focusing on these primary metrics:
* **Age** 
* **Blood Pressure (bp)**: Diastolic blood pressure
* **Specific Gravity (sg)**: Indicator of urine concentration.
* **Albumin (al)**: Protein levels indicating kidney filtration damage.
* **Blood Glucose Random (bgr)**
* **Serum Creatinine (sc)**: Critical waste product filtered by kidneys.
* **Hemoglobin (hemo)**: Low levels are common in CKD patients.

### **Methodology / Approach**
1. **Data Preprocessing**: Cleaned the dataset and handled missing values using mean imputation.
2. **Algorithm**: Implemented **Logistic Regression**, which uses the Sigmoid function for binary classification.
3. **Evaluation**: Evaluated the model on a 20% test split to ensure accuracy.
4. **Deployment**: Developed a web interface using **Streamlit** for real-time user interaction.

### **Tools & Technologies Used**
* **Language**: Python
* **Libraries**: Pandas, Scikit-Learn, NumPy, Streamlit
* **Deployment**: GitHub / Streamlit Cloud

### **Steps to Run the Project**
1. Install dependencies: `pip install -r requirements.txt`
2. Run training: `python train_ckd.py`
3. Launch App: `streamlit run app.py`

### **Results / Output**
- **Model Performance**: The Logistic Regression model achieved a high accuracy during testing.
- **Web Interface**: A fully functional frontend was developed using Streamlit.
- **Deployment**: The project is live and accessible via the link below.

<img width="1074" height="734" alt="Screenshot 2026-01-04 at 2 11 23 PM" src="https://github.com/user-attachments/assets/ffc125c3-0744-4835-b1af-184e55a5def0" />

<img width="1074" height="734" alt="Screenshot 2026-01-04 at 2 10 56 PM" src="https://github.com/user-attachments/assets/397e2be2-a0a1-460f-ba91-cd40273e67c4" />

**Live Link**: [https://ckd-prediction-ai.streamlit.app/](https://ckd-prediction-ai.streamlit.app/)
