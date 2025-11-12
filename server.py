from flask import Flask, send_file
from pydub.generators import Sine
import io

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/audio")
def generate_audio():
    # Genera un suono sinusoidale di 440 Hz per 1 secondo
    sound = Sine(440).to_audio_segment(duration=1000)

    # Salva l’audio in memoria (senza scrivere su disco)
    buffer = io.BytesIO()
    sound.export(buffer, format="wav")
    buffer.seek(0)

    return send_file(buffer, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
