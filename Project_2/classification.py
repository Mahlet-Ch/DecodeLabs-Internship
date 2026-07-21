
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset

df = pd.read_csv("student_data.csv")

print("===== Student Dataset =====")
print(df)

# Step 2: Separate features and label

X = df[["Hours", "Attendance"]]
y = df["Result"]

# Step 3: Split the dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 4: Create the model

model = DecisionTreeClassifier()

# Step 5: Train the model

model.fit(X_train, y_train)

# Step 6: Test the model

predictions = model.predict(X_test)

print("\n===== Predictions =====")
print(predictions)

print("\n===== Actual Results =====")
print(y_test.values)

# Step 7: Calculate accuracy

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

#Step 8: Predict new students

print("\n===== New Student Predictions =====")

student1 = [[6, 88]]
student2 = [[2, 35]]

prediction1 = model.predict(student1)
prediction2 = model.predict(student2)

print("Student (6 study hours, 88% attendance):", prediction1[0])

print("Student (2 study hours, 35% attendance):", prediction2[0])