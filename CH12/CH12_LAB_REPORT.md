# Chapter 12: Regression — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 05/03/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Regression is a supervised machine learning technique that models the relationship between input features and a continuous output value. The algorithm learns from labeled training data to find the best-fit line (or curve) that minimizes the error between predicted and actual values, then uses that model to predict outputs for new inputs.
- **Time complexity:** O(n × d) per training iteration for linear regression, where n is the number of data points and d is the number of features. KNN-based regression runs in O(n) at prediction time since it must compute distances to all training points.
- **When to use it:** Regression is used when the output you want to predict is a continuous number rather than a category — for example, predicting house prices, estimating crop yields, or forecasting temperatures based on historical data.

## Test Results

```
=== Chapter 12: Regression Demo ===

Dataset: Predicted bread loaves to bake based on weather features
Features: temperature (°F), rainfall (in), weekend (0/1)

Training samples: 80
Test samples:     20

--- KNN Regression (k=4) ---
Sample predictions vs actual:

  Day  | Temp | Rain | Weekend | Predicted | Actual | Error
  -----|------|------|---------|-----------|--------|------
  1    | 85°  | 0.0  | 1       | 218       | 226    | -8
  2    | 72°  | 0.2  | 0       | 184       | 179    | +5
  3    | 60°  | 1.1  | 0       | 151       | 148    | +3
  4    | 90°  | 0.0  | 1       | 235       | 240    | -5
  5    | 55°  | 2.3  | 0       | 133       | 128    | +5

Mean Absolute Error (MAE): 8.4 loaves
R² Score: 0.92

--- Comparison: KNN vs Linear Regression ---
| Model             | MAE   | R² Score |
|-------------------|-------|----------|
| KNN (k=4)         | 8.4   | 0.92     |
| Linear Regression | 11.2  | 0.87     |
```

## Reflection Questions

1. **What is the difference between classification and regression in machine learning?**
   Classification predicts a discrete category or label — such as whether an email is spam or not spam — while regression predicts a continuous numerical value, such as how many loaves of bread to bake. Both are supervised learning techniques that learn from labeled training data, but the nature of the output determines which approach is appropriate. KNN can be adapted for both: majority vote for classification, and averaging neighbor values for regression.

2. **What does the R² score measure, and what does a value close to 1.0 indicate?**
   The R² score (coefficient of determination) measures how well the model's predictions explain the variance in the actual output values, on a scale from 0 to 1. A value close to 1.0 means the model accounts for nearly all of the variability in the data and its predictions closely match the actual values. A value near 0 means the model performs no better than simply predicting the average of the dataset for every input.

3. **Why is feature selection especially important in regression models?**
   In regression, irrelevant features add noise to the model without improving its predictive power, which can cause it to overfit the training data and perform poorly on new inputs. Redundant features can also distort the model by artificially inflating the apparent importance of a characteristic. Choosing features that have a genuine causal or correlational relationship with the output — such as temperature and weekend status for bread sales — leads to a model that generalizes better to unseen data.

## Challenges Encountered
The most challenging aspect of this lab was understanding the difference between using KNN for classification versus regression, and specifically how averaging neighbor output values produces a continuous prediction. Normalizing the input features before computing distances was also easy to overlook — without normalization, features with larger numeric ranges dominated the distance calculation and skewed predictions significantly. Running the model both with and without normalization and comparing the MAE scores made the importance of that step very concrete.
