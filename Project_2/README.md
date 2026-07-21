# Student Pass or Fail Classification

## Project Goal

This project builds a simple machine learning classification model that predicts whether a student will pass or fail.

## Dataset

The dataset contains:

- Hours Studied
- Attendance
- Result (Pass/Fail)

## Technologies Used

- Python
- Pandas
- Scikit-learn

## Machine Learning Algorithm

Decision Tree Classifier

## Project Workflow

1. Load the dataset.
2. Separate features and labels.
3. Split the data into training and testing sets.
4. Train the model.
5. Make predictions.
6. Evaluate the model using accuracy.
7. Predict results for new students.

## How to Run

Install the required libraries:

---bash
pip install -r requirements.txt

Run the project:

--bash
python classification.py

## Example Output

Accuracy: 1.0

Student (6 study hours, 88% attendance): Pass

Student (2 study hours, 35% attendance): Fail
