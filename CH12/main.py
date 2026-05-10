import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_bakery_data():
    data = {
        'weather': [3, 5, 2, 4, 1, 5, 3, 4, 2, 5, 1, 3, 4, 2, 5, 3, 4, 1, 2, 4],
        'weekend_holiday': [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        'game_on': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        'loaves': [42, 95, 30, 72, 38, 55, 78, 50, 58, 85, 22, 52, 88, 44, 70, 65, 62, 48, 70, 75]
    }
    return pd.DataFrame(data)

def prepare_features_and_target(df):
    X = df[['weather', 'weekend_holiday', 'game_on']].values  # shape: (20, 3)
    y = df['loaves'].values                                    # shape: (20,)
    return X, y

def train_knn_model(X, y, k=4):
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X, y)
    return model

def predict_loaves_for_today(model, weather, weekend_holiday, game_on):
    today_features = np.array([[weather, weekend_holiday, game_on]])  # shape: (1, 3)
    prediction = model.predict(today_features)[0]
    return prediction

def main():
    df = load_bakery_data()
    print("Bakery Data:")
    print(df)
    print()

    X, y = prepare_features_and_target(df)
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)
    print()

    model = train_knn_model(X, y, k=4)
    print("KNN model trained with k=4")
    print()

    today_weather = 4
    today_weekend_holiday = 1
    today_game_on = 0

    print(f"Today's conditions: Weather={today_weather}, Weekend/Holiday={today_weekend_holiday}, Game={today_game_on}")

    predicted_loaves = predict_loaves_for_today(model, today_weather, today_weekend_holiday, today_game_on)
    print(f"Predicted loaves to bake: {predicted_loaves}")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['weather'], df['loaves'], alpha=0.7, label='Historical Data')
    plt.xlabel('Weather (1-5 scale)')
    plt.ylabel('Loaves Sold')
    plt.title('Bakery Sales vs Weather')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.close()

if __name__ == "__main__":
    main()
