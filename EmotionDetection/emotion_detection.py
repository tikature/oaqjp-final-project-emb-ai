"""Emotion detection using the Watson NLP Emotion Predict service."""

import requests


WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

WATSON_HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_emotions():
    """Return the expected emotion format for invalid input."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str):
    """Analyze text and return emotion scores and dominant emotion."""
    if not text_to_analyze or not text_to_analyze.strip():
        return _empty_emotions()

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        WATSON_URL,
        json=input_json,
        headers=WATSON_HEADERS,
        timeout=30,
    )

    if response.status_code == 400:
        return _empty_emotions()

    response.raise_for_status()

    emotions = response.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions