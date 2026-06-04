import os
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

clips = [
    {
        "name": "monday_executive",
        "text": "What's our narrative here?",
        "voice_id": "pNInz6obpgDQGcFmaJgB"
    },
    {
        "name": "wednesday_engineer",
        "text": "Realistically, addressing these gaps could take between six to twelve months.",
        "voice_id": "pNInz6obpgDQGcFmaJgB"
    },
    {
        "name": "thursday_ceo",
        "text": "It's unacceptable that a 40-person team outpaces us with 1 million paid users.",
        "voice_id": "pNInz6obpgDQGcFmaJgB"
    },
    {
        "name": "friday_satya",
        "text": "Define our failure before it defines us.",
        "voice_id": "pNInz6obpgDQGcFmaJgB"
    }
]

print("🎙️ Generating voice clips...\n")

for clip in clips:
    print(f"Generating: {clip['name']}...")
    audio = client.text_to_speech.convert(
        text=clip['text'],
        voice_id=clip['voice_id'],
        model_id="eleven_turbo_v2_5"
    )
    filename = f"{clip['name']}.mp3"
    with open(filename, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"✅ Saved: {filename}")

print("\n🎉 All voice clips generated!")
