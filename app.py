from flask import Flask, render_template, request, jsonify, session, redirect
from flask_session import Session
from datetime import timedelta
from flask_cors import CORS
import os
from dotenv import load_dotenv
import json
import requests
import uuid

load_dotenv()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'abcd1234'
app.permanent_session_lifetime = timedelta(minutes=30)
Session(app)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}})

endpoint = os.getenv("API_ENDPOINT")

@app.before_request
def before_request():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())

@app.route("/")
def home():
    return render_template("home.html")

# APP Routes for the English version
@app.route("/en/onboarding")
def en_onboarding():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/2-onboarding.html", name=session.get(f"{user_id}_name"))

@app.route("/en/select-assistant")
def en_select_assistant():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/3-select-assistant.html", name=session.get(f"{user_id}_name"))

@app.route("/en/select-input")
def en_select_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    
    avatar_url = None
    avatar_voice = None
    avatar_body = None
    if f"{user_id}_assistant" in session:
        if session[f"{user_id}_assistant"] == 'female':
            avatar_url = "https://models.readyplayer.me/6685cdb9539979578e51c626.glb?morphTargets=ARKit,Oculus+Visemes,mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown&textureSizeLimit=1024&textureFormat=png"
            avatar_voice = "en-GB-Standard-A"
            avatar_body = 'F'
        elif session[f"{user_id}_assistant"] == 'male':
            avatar_url = "https://models.readyplayer.me/66841b4f3a3799e2f94177e8.glb?morphTargets=ARKit,Oculus+Visemes,mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown&textureSizeLimit=1024&textureFormat=png"
            avatar_voice ="en-GB-Standard-B"
            avatar_body = 'M'
    else:
        return redirect('/en/select-assistant')
    return render_template("en/4-select-input.html", avatar_url=avatar_url, avatar_voice=avatar_voice, avatar_body=avatar_body)

@app.route("/en/text-input")
def en_text_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/5-text-input.html")

@app.route("/en/image-input")
def en_image_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/6-image-input.html")

@app.route("/en/face-scan")
def en_face_scan():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/7-face-scan-input.html")

@app.route("/en/report")
def en_report():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/8-report.html", 
                           disease1=session.get(f"{user_id}_disease1"),
                           disease2=session.get(f"{user_id}_disease2"),
                           disease3=session.get(f"{user_id}_disease3"))

@app.route("/en/chat")
def en_chat():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'english':
        return redirect("/")
    return render_template("en/9-chat.html")

# APP Routes for the IGBO version
@app.route("/ig/onboarding")
def ig_onboarding():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/2-onboarding.html", name=session.get(f"{user_id}_name"))

@app.route("/ig/select-assistant")
def ig_select_assistant():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/3-select-assistant.html", name=session.get(f"{user_id}_name"))

@app.route("/ig/select-input")
def ig_select_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    avatar_url = None
    avatar_voice = None
    avatar_body = None
    if f"{user_id}_assistant" in session:
        if session[f"{user_id}_assistant"] == 'female':
            avatar_url = "https://models.readyplayer.me/6685cdb9539979578e51c626.glb?morphTargets=ARKit,Oculus+Visemes,mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown&textureSizeLimit=1024&textureFormat=png"
            avatar_voice = "en-GB-Standard-A"
            avatar_body = 'F'
        elif session[f"{user_id}_assistant"] == 'male':
            avatar_url = "https://models.readyplayer.me/66841b4f3a3799e2f94177e8.glb?morphTargets=ARKit,Oculus+Visemes,mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown&textureSizeLimit=1024&textureFormat=png"
            avatar_voice ="en-GB-Standard-B"
            avatar_body = 'M'
        else:
            return redirect('/ig/select-assistant')
    return render_template("ig/4-select-input.html", avatar_url=avatar_url, avatar_voice=avatar_voice, avatar_body=avatar_body)

@app.route("/ig/text-input")
def ig_text_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/5-text-input.html")

@app.route("/ig/image-input")
def ig_image_input():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/6-image-input.html")

@app.route("/ig/face-scan")
def ig_face_scan():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/7-face-scan-input.html")

@app.route("/ig/report")
def ig_report():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/8-report.html", 
                           disease1=session.get(f"{user_id}_disease1"),
                           disease2=session.get(f"{user_id}_disease2"),
                           disease3=session.get(f"{user_id}_disease3"))

@app.route("/ig/chat")
def ig_chat():
    user_id = session.get('user_id')
    if not user_id or session.get(f"{user_id}_language") != 'igbo':
        return redirect("/")
    return render_template("ig/9-chat.html")

@app.route('/api/language', methods=["POST"])
def language_select():
    user_id = session.get('user_id')
    data = request.json
    name = data.get('name')
    language = data.get('language')
    session[f"{user_id}_name"] = name
    session[f"{user_id}_language"] = language
    return jsonify({}), 200

@app.route('/api/assistant', methods=["POST"])
def assistant_select():
    user_id = session.get('user_id')
    data = request.json
    assistant = data.get('assistant')
    if assistant not in ['male', 'female']:
        return jsonify({}), 400
    else:
        session[f"{user_id}_assistant"] = assistant
        return jsonify({}), 200

@app.route('/api/diagnosis', methods=["POST"])
def diagnosis():
    user_id = session.get('user_id')
    diagnosis_endpoint = f"{endpoint}/medicalai/api/v1/diagnosis-api"
    data = request.json
    language = data.get('language')
    symptoms = data.get('symptoms')
    request_body = {
        "symptoms": symptoms,
        "language": language
    }
    request_body = json.dumps(request_body, ensure_ascii=False)
    response = requests.post(diagnosis_endpoint, data=request_body)
    data = response.json()

    # Process the response
    diagnosis_text = data.get('diagnosis', '')
    lines = diagnosis_text.split('\n')

    if len(lines) >= 3:
        # Extract treatment
        treatment = lines[1].replace('Treatment is: ', '').strip()
        session[f"{user_id}_treatment"] = treatment

        # Extract diseases
        diseases = lines[2].split('-')
        session[f"{user_id}_disease1"] = diseases[0] if len(diseases) > 0 else ''
        session[f"{user_id}_disease2"] = diseases[1] if len(diseases) > 1 else ''
        session[f"{user_id}_disease3"] = diseases[2] if len(diseases) > 2 else ''

    return jsonify({}), 200

if __name__ == "__main__":
    app.run(debug=True)