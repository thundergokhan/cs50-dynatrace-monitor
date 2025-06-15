from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    status = ""
    if request.method == "POST":
        ip = request.form.get("ip")
        try:
            output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
            status = f"🟢 {ip} sunucusu çalışıyor."
        except subprocess.CalledProcessError:
            status = f"🔴 {ip} sunucusuna ulaşılamıyor."
    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
