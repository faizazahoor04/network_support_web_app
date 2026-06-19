from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

texts = [
    "internet is slow",
    "wifi speed is very slow",
    "no internet connection",
    "internet not working",
    "router light is blinking",
    "router problem",
    "how to pay bill",
    "billing issue",
    "new internet connection",
    "apply for new connection",
    "i want to complain",
    "register complaint"
]

labels = [
    "slow_internet",
    "slow_internet",
    "no_internet",
    "no_internet",
    "router_issue",
    "router_issue",
    "billing",
    "billing",
    "new_connection",
    "new_connection",
    "complaint",
    "complaint"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "support_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully")
