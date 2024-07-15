from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/en/onboarding")
def en_onboarding():
    return render_template("en/2-onboarding.html")

@app.route("/en/select-assistant")
def en_select_assistant():
    return render_template("en/3-select-assistant.html")

@app.route("/en/select-input")
def en_select_input():
    return render_template("en/4-select-input.html")

@app.route("/en/text-input")
def en_text_input():
    return render_template("en/5-text-input.html")

@app.route("/en/image-input")
def en_image_input():
    return render_template("en/6-image-input.html")

@app.route("/en/face-scan")
def en_face_scan():
    return render_template("en/7-face-scan-input.html")

@app.route("/en/report")
def en_report():
    return render_template("en/8-report.html")

@app.route("/en/chat")
def en_chat():
    return render_template("en/9-chat.html")





@app.route("/ig/onboarding")
def ig_onboarding():
    return render_template("ig/2-onboarding.html")

@app.route("/ig/select-assistant")
def ig_select_assistant():
    return render_template("ig/3-select-assistant.html")

@app.route("/ig/select-input")
def ig_select_input():
    return render_template("ig/4-select-input.html")

@app.route("/ig/text-input")
def ig_text_input():
    return render_template("ig/5-text-input.html")

@app.route("/ig/image-input")
def ig_image_input():
    return render_template("ig/6-image-input.html")

@app.route("/ig/face-scan")
def ig_face_scan():
    return render_template("ig/7-face-scan-input.html")

@app.route("/ig/report")
def ig_report():
    return render_template("ig/8-report.html")

@app.route("/ig/chat")
def ig_chat():
    return render_template("ig/9-chat.html")



if __name__ == "__main__":
    app.run(debug=True)