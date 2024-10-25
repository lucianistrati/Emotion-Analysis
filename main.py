import os
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# Set up your IBM Watson credentials
API_KEY = os.environ.get("IBM_WATSON_TONE_ANALYZER_API_KEY")  # Set your API key
API_URL = os.environ.get("IBM_WATSON_TONE_ANALYZER_URL")      # Set your service URL

# Initialize Tone Analyzer
authenticator = IAMAuthenticator(API_KEY)
tone_analyzer = ToneAnalyzerV3(
    version='2021-11-21',  # Use the most recent version
    authenticator=authenticator
)
tone_analyzer.set_service_url(API_URL)


def analyze_emotion(text):
    """
    Analyze the emotional tone of a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: The tone analysis results.
    """
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()

    return tone_analysis


def display_tone_analysis(tone_analysis):
    """
    Display the tone analysis results in a readable format.

    Args:
        tone_analysis (dict): The tone analysis results.
    """
    print(json.dumps(tone_analysis, indent=2))

    print("\nEmotional Tones:")
    for tone in tone_analysis['tones']:
        print(f"- Tone: {tone['tone_name']}, Score: {tone['score']:.4f}")


def main():
    # Example text (could be a conversation transcript)
    conversation_transcript = (
        "I really appreciate your help with this issue. It's been quite frustrating "
        "to deal with, but your support has made a big difference. Thank you!"
    )

    # Analyze the emotional tone
    tone_analysis = analyze_emotion(conversation_transcript)
    
    # Display the results
    display_tone_analysis(tone_analysis)


if __name__ == "__main__":
    main()
