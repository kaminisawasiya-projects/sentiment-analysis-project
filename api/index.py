from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load dataset
data = pd.read_csv("reviews.csv")


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin":
            return redirect(url_for("profile"))  # ✅ redirect after login
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

# ---------------- PREDICT PAGE ----------------
@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")



@app.route("/register")
def register():
    return render_template("register.html")


# ---------------- PREDICTION LOGIC ----------------
@app.route("/predict", methods=["POST"])
def predict():
    user_text = request.form["user_text"]
    text_vec = vectorizer.transform([user_text])
    prediction = model.predict(text_vec)[0]

    return render_template("predict.html", prediction=prediction)



# ---------------- INDEX / PREDICTION PAGE ----------------
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html",user_name="Admin")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    total = len(data)
    positive = len(data[data["sentiment"] == "positive"])
    negative = len(data[data["sentiment"] == "negative"])

    return render_template(
        "dashboard.html",
        total=total,
        positive=positive,
        negative=negative
    )


if __name__ == "__main__":
    app.run(debug=True)