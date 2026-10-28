from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Demonstration rules only. Replace with a trained model and validated agronomic data
# before using this for real farming decisions.
def recommend_crop(n, p, k, temperature, humidity, ph, rainfall):
    crops = [
        ("rice", 80, 40, 40, 20, 35, 5.5, 7.0, 150, 300),
        ("maize", 50, 40, 20, 18, 32, 5.5, 7.5, 50, 150),
        ("chickpea", 20, 60, 20, 15, 30, 5.5, 8.0, 40, 100),
        ("kidneybeans", 20, 60, 20, 15, 25, 18, 30, 5.5, 6.5, 60, 150),
        ("cotton", 100, 40, 20, 22, 35, 5.5, 8.0, 50, 120),
        ("coffee", 100, 20, 30, 20, 30, 6.0, 7.5, 150, 250),
    ]
    # Score each crop against broad illustrative ranges.
    best_crop, best_score = "maize", -1
    for row in crops:
        name, rn, rp, rk, tmin, tmax, phmin, phmax, rmin, rmax = row
        score = 0
        score += max(0, 1 - abs(n-rn)/max(rn, 1))
        score += max(0, 1 - abs(p-rp)/max(rp, 1))
        score += max(0, 1 - abs(k-rk)/max(rk, 1))
        score += 1 if tmin <= temperature <= tmax else 0
        score += 1 if phmin <= ph <= phmax else 0
        score += 1 if rmin <= rainfall <= rmax else 0
        score += 1 if 30 <= humidity <= 95 else 0
        if score > best_score:
            best_crop, best_score = name, score
    return best_crop.replace("_", " ").title()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            values = {
                "n": float(request.form["nitrogen"]),
                "p": float(request.form["phosphorus"]),
                "k": float(request.form["potassium"]),
                "temperature": float(request.form["temperature"]),
                "humidity": float(request.form["humidity"]),
                "ph": float(request.form["ph"]),
                "rainfall": float(request.form["rainfall"]),
            }
            result = recommend_crop(**values)
        except (ValueError, KeyError):
            error = "Please enter valid numbers in every field."
    return render_template("index.html", result=result, error=error)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
