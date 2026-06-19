# Network Support Web App

A lightweight, AI-powered customer support chatbot designed to help users resolve common network and internet issues. Built with Flask and scikit-learn, it classifies user messages into predefined intents and provides instant, relevant responses.

---

## 📌 Features

- **Intent Classification**: Uses a Logistic Regression model trained on a small dataset of support queries.
- **Predefined Responses**: Returns helpful replies for common issues like slow internet, no connection, router problems, billing, new connections, and complaints.
- **Web Interface**: Simple and clean HTML form for user interaction.
- **Fast & Lightweight**: Minimal dependencies, runs locally with `debug=True` for development.

---

## 🛠️ Technologies Used

- **Backend**: Python 3, Flask
- **Machine Learning**: scikit-learn (TfidfVectorizer, LogisticRegression)
- **Serialization**: joblib (model and vectorizer persistence)
- **Frontend**: HTML, CSS (optional, minimal)

---

## 📁 Project Structure

network_support_web_app/
│
├── app.py # Flask application (routes and prediction logic)
├── model.py # Training script (creates .pkl files)
├── support_model.pkl # Trained Logistic Regression model
├── vectorizer.pkl # Fitted TF-IDF vectorizer
├── templates/
│ └── index.html # Frontend form (not included, but assumed)
└── README.md # Project documentation


---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7+
- pip

### Steps

1. **Clone the repository**

   ```bash
   cd network_support_web_app

2. Create and activate a virtual environment (optional but recommended)

   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

   pip install flask scikit-learn joblib

4. Train the model (optional – pre-trained files are included)
   If you want to retrain or modify the model, run:

   python model.py

   This will generate support_model.pkl and vectorizer.pkl.

5. Run the Flask app

   python app.py

   The app will start at http://127.0.0.1:5000/.


## HOW TO USE

1. Open the web app in your browser.
2. Type your network-related issue into the text box (e.g., "internet is slow" or "billing issue").
3. Click Submit.
4. The app will display a predefined response based on the detected intent.

Example Interactions:

- User Input: "internet is slow" -> Detected Intent: slow_internet -> Response: Please restart your router and check cable connections.
- User Input: "no internet connection" -> Detected Intent: no_internet -> Response: We are checking your area for outages. Please wait.
- User Input: "router blinking" -> Detected Intent: router_issue -> Response: Try rebooting your router. If issue continues, contact support.
- User Input: "how to pay bill" -> Detected Intent: billing -> Response: You can pay your bill using our app or website.
- User Input: "new connection" -> Detected Intent: new_connection -> Response: Please share your location. Our sales team will contact you.
- User Input: "register complaint" -> Detected Intent: complaint -> Response: Your complaint has been registered. Ticket will be issued.


## MODEL TRAINING DETAILS

The model is a Logistic Regression classifier trained on a small hand-labeled dataset (model.py).

- Text Preprocessing: TF-IDF vectorization (with default parameters).
- Classes (Intents):
  - slow_internet
  - no_internet
  - router_issue
  - billing
  - new_connection
  - complaint

- Training Data: 12 examples (2 per class). This is a minimal demo – for production, a much larger dataset is required.


## CONTRIBUTING

Contributions are welcome! Please open an issue or submit a pull request for any improvements, bug fixes, or additional features.


## LICENSE

This project is open-source and available under the MIT License.


## FUTURE ENHANCEMENTS

- Integrate a more comprehensive dataset for better accuracy.
- Add more intents and dynamic responses.
- Connect to a live ticketing system or knowledge base.
- Improve UI/UX with a chat-like interface.
- Deploy to a cloud platform (Heroku, AWS, etc.).


## CONTACT

For any questions or feedback, please reach out to az9410451@gmail.com or open an issue on GitHub.

Enjoy using the Network Support Web App! 🚀
