# MMM Flask Server - Deployment Guide (Render)

This repository hosts the backend Flask server for the MMM (Masked Motion Modeling) project. The server acts as a proxy between the Android app and the Hugging Face-hosted Gradio model, handling motion prompt requests and returning animated HTML for rendering in WebView.

---

## 🌐 Live Demo

Deployed via Render: * https://mmm-flask-server.onrender.com*

---

## 🧠 Features

* Accepts POST requests with motion prompts
* Uses `gradio_client` to communicate with Hugging Face model
* Injects JavaScript for auto-play animation inside iframe
* Supports polling for result readiness

---

## 🚀 Deployment on Render.com

### 🔧 1. Prerequisites

* A GitHub account
* A Render.com account (free tier is sufficient)

### 📦 2. Files in this repo

* `app.py`: Flask server logic
* `requirements.txt`: Lists Flask and gradio\_client
* `runtime.txt` (optional): Specifies Python version (e.g., `python-3.10`)

### ☁️ 3. Steps to Deploy

1. **Fork or clone this repo**
2. **Push it to your own GitHub**
3. **Login to [Render.com](https://render.com)**
4. Click **"New Web Service"**
5. Select your GitHub repo
6. Fill out the service details:

   * **Environment**: Python
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `python app.py`
   * **Instance Type**: Free
7. Click **Deploy**

Within a few minutes, Render will provide you with a public URL like:

```
https://mmm-flask-server.onrender.com
```

Use this URL in your Android app to POST and GET responses.

---

## 🔁 Endpoints

### POST `/predict`

* **Body** (JSON): `{ "prompt": "a person waves hello", "length": 156 }`
* **Response**: HTML animation (injected with autoplay)

### GET `/get_result`

* **Returns** the last available result (or status: pending)

---

## 🤖 Dependencies

* Flask
* gradio\_client

Install locally using:

```bash
pip install -r requirements.txt
```

---

## 📱 Client (Android App)

The Android app sends a motion prompt to this server and renders the HTML response using WebView. See the related [MMM Android Client Repo](https://github.com/pals6/MMM-Android-Client) for frontend integration.

---

## 🧪 Testing Locally

```bash
python app.py
```

Runs on `http://127.0.0.1:5000` by default.

---


