import asyncio
import edge_tts
import os


SCRIPT = """
What if I told you… saving money might be the reason you’re still broke?

Yeah. I said it.

Everywhere you look, people are screaming —
“Save 10% of your income.”
“Cut your coffee.”
“Don’t spend.”
“Don’t risk.”

But let me ask you something honestly…

Have you ever saved your way into wealth?

Or are you just surviving… slowly?

Today I’m going to tell you a story.
And by the end of it, you might completely change how you think about money.
"""

VOICE = "en-US-AndrewMultilingualNeural"   # Deep, confident male voice
# Other great options:
#   "en-US-GuyNeural"              – Classic American male
#   "en-US-ChristopherNeural"      – Professional male
#   "en-GB-RyanNeural"             – British male
#   "en-US-JennyNeural"            – Friendly female
#   "en-US-AriaNeural"             – Expressive female

OUTPUT_FILE = "1.mp3"
SUBTITLE_FILE = "1.vtt"  # Optional WebVTT subtitles

RATE   = "-10%"   # Speed: -50% (slow) to +100% (fast). 0% = default
VOLUME = "+0%"   # Volume: -50% to +50%
PITCH  = "+0Hz"  # Pitch: -50Hz to +50Hz



async def generate_voiceover():
    """Generate the voiceover MP3 file."""

    print("─" * 45)

    communicate = edge_tts.Communicate(
        text=SCRIPT.strip(),
        voice=VOICE,
        rate=RATE,
        volume=VOLUME,
        pitch=PITCH,
    )

    await communicate.save(OUTPUT_FILE)
    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"Voiceover saved → {OUTPUT_FILE}  ({size_mb:.2f} MB)")


async def generate_with_subtitles():
    """Generate MP3 + WebVTT subtitle file simultaneously."""
    print(f" Generating audio + subtitles …")

    communicate = edge_tts.Communicate(
        text=SCRIPT.strip(),
        voice=VOICE,
        rate=RATE,
        volume=VOLUME,
        pitch=PITCH,
    )

    submaker = edge_tts.SubMaker()

    with open(OUTPUT_FILE, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)

    with open(SUBTITLE_FILE, "w", encoding="utf-8") as vtt_file:
        vtt_file.write(submaker.get_srt())   # use .get_srt() for .srt format

    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"Audio saved    → {OUTPUT_FILE}  ({size_mb:.2f} MB)")
    print(f"Subtitles saved → {SUBTITLE_FILE}")


async def list_voices(language_filter: str = "en-"):
    """Print all available English voices."""
    voices = await edge_tts.list_voices()
    print(f"\n{'Name':<45} {'Gender':<10} {'Locale'}")
    print("─" * 75)
    for v in voices:
        if language_filter.lower() in v["ShortName"].lower():
            print(f"{v['ShortName']:<45} {v['Gender']:<10} {v['Locale']}")



if __name__ == "__main__":
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "audio"

    if mode == "list":
        # python generate_voice.py list
        asyncio.run(list_voices())
    elif mode == "subtitles":
        # python generate_voice.py subtitles
        asyncio.run(generate_with_subtitles())
    else:
        # python generate_voice.py
        asyncio.run(generate_voiceover())