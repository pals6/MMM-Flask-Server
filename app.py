from flask import Flask, request, jsonify
from threading import Thread
from gradio_client import Client

app = Flask(__name__)
client = Client("pbichpur/MMM-Demo")

# Store latest prediction result
latest_result = None

def predict_in_background(prompt, length):
    global latest_result
    try:
        result = client.predict(
            prompt,
            length,
            api_name="/predict"
        )

        if isinstance(result, str):
            # Inject JavaScript to autoplay the motion
            result += """
<script>
setTimeout(function() {
    var plot = document.querySelector('div.plotly'); 
    if (plot) {
        var plotId = plot.id;
        if (plotId) {
            Plotly.animate(plotId, null);
        }
    }
}, 500);
</script>
"""

        latest_result = result
        print("Prediction completed.")

    except Exception as e:
        latest_result = f"Error: {e}"
        print("Prediction failed:", e)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        length = data.get("length")

        # Clear previous result
        global latest_result
        latest_result = None

        # Start background prediction
        thread = Thread(target=predict_in_background, args=(prompt, length))
        thread.start()

        return jsonify({"status": "Prediction started"}), 202

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_result", methods=["GET"])
def get_result():
    global latest_result
    if latest_result is None:
        return jsonify({"status": "Processing"}), 202
    else:
        return jsonify({"status": "Completed", "html": latest_result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
