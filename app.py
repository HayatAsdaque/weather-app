from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔑 Replace this with your actual OpenWeatherMap API key
API_KEY = "dd9f9d0db65226b3e92f77c1b8999ac2"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather = {"error": "City not found!"}
    return render_template("index.html", weather=weather, api_key=API_KEY)


# 🔁 Run the app on all IPs so you can access from Windows browser
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
