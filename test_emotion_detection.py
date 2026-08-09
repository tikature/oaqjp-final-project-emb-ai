import pytest

from EmotionDetection import emotion_detector


def test_emotion_detector():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    ]

    for text, expected_emotion in test_cases:
        result = emotion_detector(text)

        assert result["dominant_emotion"] == expected_emotion, (
            f"For text: {text}, "
            f"expected: {expected_emotion}, "
            f"but got: {result['dominant_emotion']}"
        )


if __name__ == "__main__":
    pytest.main()