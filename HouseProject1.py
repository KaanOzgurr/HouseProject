
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = {
    'square_feet': [750, 800, 1200, 1500, 1800, 2000, 2300, 2500],
    'bedrooms': [2, 2, 3, 3, 4, 4, 4, 5],
    'bathrooms': [1, 1, 2, 2, 3, 3, 3, 4],
    'living_rooms': [1,2,2,1,2,3,1,2],
    'price': [150000, 160000, 220000, 250000, 310000, 350000, 380000, 420000]
}

df = pd.DataFrame(data)


print(df.head())
sns.pairplot(df)
plt.show()


X = df[['square_feet', 'bedrooms', 'bathrooms' ,'living_rooms']]
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Real Prices:", list(y_test))
print("Guessing Prices:", list(y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))


plt.scatter(y_test, y_pred)
plt.xlabel("Real Prices")
plt.ylabel("Guessing Prices")
plt.title("Real vs Guessing Prices:")
plt.show()

plt.savefig("output.png")  # Grafiği kaydeder
plt.show()

