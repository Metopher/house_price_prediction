# 🏠 House Price Prediction App

A machine learning-powered web application that estimates house prices in India based on property specifications. This project utilizes a dataset of housing features to train predictive models and serves them via an interactive Streamlit interface.

## 📋 Project Overview

This project demonstrates the end-to-end process of building a data science application:
1.  **Data Analysis:** Exploratory Data Analysis (EDA) on housing data.
2.  **Model Training:** Training and tuning machine learning models (Linear Regression, Decision Trees, Random Forest) using Scikit-Learn.
3.  **Deployment:** Building a user-friendly web interface using Streamlit.

## ✨ Features

*   **Interactive UI:** Clean, custom-styled interface built with Streamlit.
*   **Real-time Valuation:** Instant price estimation based on user inputs.
*   **Key Parameters:** Considers factors such as:
    *   Number of Bedrooms & Bathrooms
    *   Living Area (sq ft)
    *   Condition of the House
    *   Number of Schools Nearby
*   **Custom Styling:** Enhanced visual experience using custom CSS.

## 🛠️ Tech Stack

*   **Python** (Core Language)
*   **Pandas & NumPy** (Data Manipulation)
*   **Scikit-Learn** (Machine Learning & GridSearch)
*   **Streamlit** (Web Framework)
*   **Joblib** (Model Serialization)

## 📂 Project Structure

```text
├── app.py                 # Main Streamlit application script
├── notebook.ipynb         # Jupyter Notebook for EDA and Model Training
├── style.css              # Custom CSS for UI styling
├── House Price India.csv  # Dataset source
└── README.md              # Project documentation
```

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/house-price-prediction.git
    cd house-price-prediction
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy scikit-learn streamlit joblib
    ```

3.  **Generate the Model:**
    *   Open `notebook.ipynb` in Jupyter Notebook or VS Code.
    *   Run all cells to perform data analysis and train the model.
    *   Ensure the notebook saves the trained model as `model.pkl` in the root directory.

4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## 📊 Model Details

The project explores multiple regression algorithms to determine the best fit for the data. The `notebook.ipynb` file contains:
*   Data cleaning and preprocessing.
*   Feature selection (`number of bedrooms`, `living area`, etc.).
*   Hyperparameter tuning using `GridSearchCV`.
*   Evaluation of models like Linear Regression, Decision Tree Regressor, and Random Forest Regressor.

## 📝 Dataset

The dataset used in this project is `House Price India.csv`, sourced from Kaggle. It contains various features regarding houses in India, including location coordinates, area details, and amenities.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/house-price-prediction/issues).

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).