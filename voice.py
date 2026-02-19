import edge_tts
import asyncio

async def generate_voice():
    text = "Hello everyone, welcome to my YouTube channel! "
    voice = "en-US-GuyNeural"  # Male voice 
    # voice = "en-US-ChristopherNeural"
    
    tts = edge_tts.Communicate(text, voice=voice)
    await tts.save("output.mp3")
    print("Voice saved as output.mp3")

asyncio.run(generate_voice())


# import edge_tts
# import asyncio

# async def generate(text, filename, voice="en-US-ChristopherNeural"):
#     tts = edge_tts.Communicate(
#         text,
#         voice=voice,
#         rate="-10%",
#         pitch="-5Hz"
#     )
#     await tts.save(filename)

# async def main():
#     # Split your script into parts and add pauses manually
#     parts = [
#         ("In 2008, one man lost everything.", "part1.mp3"),
#         ("His house. His family. His money.", "part2.mp3"),
#         ("But what happened next changed his life forever.", "part3.mp3"),
#     ]
    
#     for text, filename in parts:
#         await generate(text, filename)
#         print(f"Saved: {filename}")

# asyncio.run(main())

# from pydub import AudioSegment
# import os

# def combine_with_pauses():
#     files = ["part1.mp3", "part2.mp3", "part3.mp3"]
#     pause_800ms = AudioSegment.silent(duration=800)   # 800ms pause
#     pause_1s = AudioSegment.silent(duration=1000)     # 1 second pause
    
#     final = AudioSegment.empty()
    
#     final += AudioSegment.from_mp3("part1.mp3") + pause_1s
#     final += AudioSegment.from_mp3("part2.mp3") + pause_800ms
#     final += AudioSegment.from_mp3("part3.mp3")
    
#     final.export("final_output.mp3", format="mp3")
#     print("Final video voice ready!")

# combine_with_pauses()
# import edge_tts
# import asyncio
# from datetime import datetime

# async def generate_voice_for_text(text="Hello everyone, welcome to my YouTube channel!", num_variations=5):
#     """
#     Generate multiple voice versions of the SAME text with different voices
#     """
    
#     # Different voices to use for the same text
#     voices = [
#         {"name": "en-US-GuyNeural", "description": "US Male"},
#         {"name": "en-US-JennyNeural", "description": "US Female"}, 
#         {"name": "en-GB-RyanNeural", "description": "British Male"},
#         {"name": "en-GB-SoniaNeural", "description": "British Female"},
#         {"name": "en-AU-WilliamNeural", "description": "Australian Male"},
#         {"name": "en-AU-NatashaNeural", "description": "Australian Female"},
#         {"name": "en-CA-ClaraNeural", "description": "Canadian Female"},
#         {"name": "en-IN-PrabhatNeural", "description": "Indian Male"},
#         {"name": "en-IE-ConnorNeural", "description": "Irish Male"},
#         {"name": "en-NZ-MollyNeural", "description": "New Zealand Female"}
#     ]
    
#     print(f"📝 Text: '{text}'\n")
#     print(f"🎙️ Generating {num_variations} voice variations...\n")
    
#     for i in range(min(num_variations, len(voices))):
#         voice_info = voices[i]
#         voice = voice_info["name"]
        
#         # Create unique filename with voice name and timestamp
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         voice_short = voice.split('-')[1]  # Get country code
#         filename = f"output_{voice_short}_{i+1:02d}_{timestamp}.mp3"
        
#         print(f"Voice {i+1}: {voice_info['description']} ({voice})")
#         print(f"   Saving as: {filename}")
        
#         tts = edge_tts.Communicate(text, voice=voice)
#         await tts.save(filename)
#         print(f"   ✅ Done!\n")
    
#     print(f"✨ Successfully generated {num_variations} voice files with the same text!")

# # Example 1: Generate for a specific text with all voices
# async def main():
#     # Your specific text here
#     custom_text = "Thanks for watching this video! Please subscribe to my channel for more content."
    
#     await generate_voice_for_text(
#         text=custom_text,
#         num_variations=5  # Generate 5 different voice versions
#     )

# # Run it
# asyncio.run(main())