# Benetton Sales Prediction using Simple Linear Regression (SLR)

This project implements a Simple Linear Regression model using Object-Oriented Programming (OOP) in Python. It uses real-world data from the **Benetton Case Study** to predict sales based on advertising investment.

---

## 📊 Project Description

The goal is to create a predictive model that estimates **Sales (in Million Euros)** based on the amount spent on **Advertising (in Million Euros)** using the **Ordinary Least Squares (OLS)** method.

This is part of a university assignment for the course **Intelligence of Data Classification**.

---

## 📁 Dataset: Benetton Case

The dataset is sourced from [Displayr's Linear Regression Tutorial](https://www.displayr.com/what-is-linear-regression/).

| Year | Advertising (M €) | Sales (M €) |
|------|--------------------|-------------|
| 1991 | 30                 | 225         |
| 1992 | 40                 | 275         |
| 1993 | 45                 | 295         |
| 1994 | 50                 | 325         |
| 1995 | 60                 | 350         |
| 1996 | 70                 | 400         |

---

## 🧠 Mathematical Model

We use the **Simple Linear Regression** formula:

\[
Y = b_0 + b_1 X
\]

Where:
- \( Y \): Predicted Sales
- \( X \): Advertising investment
- \( b_0 \): Intercept
- \( b_1 \): Slope

Using the **Ordinary Least Squares (OLS)** method:

\[
b_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \quad b_0 = \bar{y} - b_1 \bar{x}
\]

 How to Run the Project
git clone https://github.com/your-username/benetton-slr-predictive-model.git
cd benetton-slr-predictive-model
python simple_linear_regression.py

Example Output

Intercept (b0): 150.00
Slope (b1): 3.57
Predicted Sales for Advertising = 55: 346.43

📌 Learning Outcomes
Apply linear regression to real-world data

Understand and implement OLS algorithm

Use Python classes to structure machine learning code

Interpret regression coefficients and predictions

📚 References
Displayr - What is Linear Regression?

University Course: Intelligence of Data Classification

🧑‍🎓 Author
DiegoPalma 

Student of Informatics Engineering

University of Gudalajara



