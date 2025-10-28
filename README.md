# 🏠 House Price Prediction Project

This project predicts house prices using a **multiple linear regression model** built with Python.  
The dataset includes features such as **square footage, number of bedrooms, bathrooms, and living rooms**.  
By training and evaluating the model, we can estimate housing prices based on these parameters.

---

## 📊 Features
- **Data Visualization:**  
  When you run the program, a **pairplot table** will appear showing the relationships between all variables  
  (`square_feet`, `bedrooms`, `bathrooms`, `living_rooms`, and `price`).  
  This helps visualize how each feature correlates with house prices.  
- **Machine Learning:**  
  Linear Regression model implemented using scikit-learn  
- **Evaluation:**  
  Mean Squared Error (MSE) is used to measure prediction accuracy  

---

## 🧠 Technologies Used
- Python  
- Pandas & NumPy  
- Scikit-learn  
- Seaborn & Matplotlib  

---

## 🚀 How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/KaanOzgurr/HouseProject.git


2. Navigate to the project folder:

cd HouseProject


3. Run the Python script:

python house_price_model.py

📈 Example Output

A pairplot table visualizing feature relationships will appear first.

Then, a scatter plot comparing real vs predicted prices is displayed.

The console shows both the actual prices and the model’s predictions with the Mean Squared Error value.
