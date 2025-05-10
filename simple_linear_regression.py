class SimpleLinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.slope = 0
        self.intercept = 0

    def fit(self):
        mean_x = sum(self.x) / self.n
        mean_y = sum(self.y) / self.n

        numerator = sum((self.x[i] - mean_x) * (self.y[i] - mean_y) for i in range(self.n))
        denominator = sum((self.x[i] - mean_x) ** 2 for i in range(self.n))

        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x

    def predict(self, x_val):
        return self.intercept + self.slope * x_val

    def get_params(self):
        return self.intercept, self.slope


# Dataset
advertising = [30, 40, 45, 50, 60, 70]
sales = [225, 275, 295, 325, 350, 400]

# Model
model = SimpleLinearRegression(advertising, sales)
model.fit()

b0, b1 = model.get_params()
print(f"Intercept (b0): {b0:.2f}")
print(f"Slope (b1): {b1:.2f}")

# Example prediction
ad_value = 55
predicted_sales = model.predict(ad_value)
print(f"Predicted Sales for Advertising = {ad_value}: {predicted_sales:.2f}")
