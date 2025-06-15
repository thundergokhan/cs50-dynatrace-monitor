from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    status = ""
    if request.method == "POST":
        ip = request.form.get("ip")
        try:
            # For Windows, use: ["ping", "-n", "1", ip]
            # For Linux/Mac, use: ["ping", "-c", "1", ip]
            output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
            status = f"🟢 Server {ip} is up and reachable."
        except subprocess.CalledProcessError:
            status = f"🔴 Server {ip} is unreachable."
    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
