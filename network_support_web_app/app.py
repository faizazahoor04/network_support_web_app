from flask import Flask, render_template, request
import joblib

model = joblib.load("support_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

responses = {
    "slow_internet": "Please restart your router and check cable connections.",
    "no_internet": "We are checking your area for outages. Please wait.",
    "router_issue": "Try rebooting your router. If issue continues, contact support.",
    "billing": "You can pay your bill using our app or website.",
    "new_connection": "Please share your location. Our sales team will contact you.",
    "complaint": "Your complaint has been registered. Ticket will be issued."
}

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_message = request.form["message"]
        vector = vectorizer.transform([user_message])
        intent = model.predict(vector)[0]
        reply = responses[intent]
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
