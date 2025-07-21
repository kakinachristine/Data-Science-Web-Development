# Import Libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

# Split the dataset into input(x) and output(y)
x= df.drop(columns=['Outcome'],axis=1)
y = df['Outcome']

# Train the model
model=RandomForestClassifier()
model.fit(x,y)

# Save the model(using joblib to dump the model
joblib.dump(model, 'diabetesApp.pkl')
print("The model has been saved successfully")

