
# Keylogger Project

A simple keylogger built with **Python Flask** for the backend and **HTML, CSS, and JavaScript** for the frontend. This project captures keyboard inputs from users and sends them to the server for processing. 


## Project Overview

This project implements a keylogger that runs in the background of a webpage. It records the keystrokes of a user in real-time and sends them to the server where they are stored or processed. The backend is built using **Flask**, a lightweight Python web framework, while the frontend consists of **HTML**, **CSS**, and **JavaScript**.

The goal of this project is to understand how web applications can interact with the browser environment and collect user input.

## Features

- **Real-time Keystroke Capture**: Captures every keystroke as it happens on the frontend.
- **Backend Server**: A Flask backend that receives and processes the captured keystrokes.
- **Simple Frontend Interface**: A basic web interface where the keylogger captures input from a text field or form.

---

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Web Server**: Flask Development Server
---

## Setup and Installation

git clone https://github.com/ShashwatSecure/KeyLogger.git
cd KeyLogger

python -m venv venv

### On Windows

venv\Scripts\activate

### On MacOS/Linux

source venv/bin/activate


pip install flask


python3 server.py 

### Port 5000 would be activated and you can access it using any browser
### Visit : localhost:5000
