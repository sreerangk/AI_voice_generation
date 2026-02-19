import edge_tts
import asyncio

async def generate_voice():
    text = "Hello everyone, welcome to my YouTube channel!"
    voice = "en-US-GuyNeural"  # Male voice
    
    tts = edge_tts.Communicate(text, voice=voice)
    await tts.save("output.mp3")
    print("Voice saved as output.mp3")

asyncio.run(generate_voice())