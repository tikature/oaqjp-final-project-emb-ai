"""Flask web application for Watson NLP emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

application = Flask(__name__)


@application.route("/emotionDetector")
def handle_emotion_detector():
    """Analyze text supplied through the textToAnalyze query parameter."""
    text_to_analyze = request.args.get("textToAnalyze")
    predicted_emotions = emotion_detector(text_to_analyze)

    return (
        "For the given statement, the system response is "
        f"'anger': {predicted_emotions['anger']}, "
        f"'disgust': {predicted_emotions['disgust']}, "
        f"'fear': {predicted_emotions['fear']}, "
        f"'joy': {predicted_emotions['joy']} and "
        f"'sadness': {predicted_emotions['sadness']}. "
        f"The dominant emotion is "
        f"{predicted_emotions['dominant_emotion']}."
    )


@application.route("/")
def render_index_page():
    """Render the main emotion detection page."""
    return render_template("index.html")


if __name__ == "__main__":
    application.run(host="localhost", port=5000)