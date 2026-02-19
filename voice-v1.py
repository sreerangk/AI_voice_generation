import asyncio
import edge_tts
import os


SCRIPT = """
Okay so let me just be honest with you.

Most people who want to get rich... they're looking for the one thing. The one trick. The shortcut.
And that's exactly why they stay broke.

So I'm gonna walk you through every real way people are actually making money in 2026.
Not theory. Not motivation. Just what's actually working.

Let's start with the obvious one — a job. But not just any job.
There are people making 80, 90, a hundred thousand dollars a year doing cloud computing, cybersecurity, sales.
High-income skills. You learn them, you get paid for them. Simple.
The problem is most people pick careers based on what sounds cool, not what pays.

Next — freelancing.
If you can edit videos, run ads, write emails that actually sell things, or build websites — companies will pay you.
Not because you have a degree. Because you can do the thing they need done.
I know a guy who learned video editing in four months. Now he makes six thousand dollars a month working from his apartment.
That's it. No magic.

Then there's starting a business.
And before you roll your eyes — I'm not talking about some big startup with investors.
I mean a small, boring business that solves one problem.
Pressure washing. HVAC. A bookkeeping service. A cleaning company.
These are not glamorous. But a good cleaning business in a mid-size city can clear two hundred thousand dollars a year.
Nobody talks about this because it's not sexy. But it works.

Content creation is real, but people misunderstand it.
You don't blow up and suddenly get rich. That's not how it works.
What actually happens is — you build an audience around something specific, and then you sell them something.
A course. A service. A product. A membership.
The content is just how people find you. The money comes from what you're actually selling.

Real estate. Look, I know — everyone says real estate.
But the reason everyone says it is because it actually works over time.
Buy a property. Rent it out. The tenant pays your mortgage. You build equity.
It's slow. It's not exciting. But in ten years? That property could be worth twice what you paid.
The hard part is getting that first one. After that it gets easier.

Stock market. Index funds specifically.
You put money in every single month, you don't touch it, and you let time do the work.
This is not how you get rich fast. This is how you don't end up broke at sixty.
Everyone should be doing this. Most people aren't.

Then there's buying websites or small businesses.
This one flies under the radar. People sell websites that already make money —
five hundred dollars a month, a thousand dollars a month — and you can buy them for two or three times their yearly revenue.
You buy it, you run it, you improve it, you sell it for more.
It's like real estate but on the internet.

Crypto. I'll keep this short.
Some people made a lot of money. Some people lost everything.
If you don't understand what you're buying, you're not investing — you're gambling.
Learn it properly or stay out.

And then there's sales.
Honestly one of the most underrated ways to make real money.
Commission-based sales — real estate, software, insurance, cars.
If you're good at it, there's no ceiling on what you can earn.
The best salespeople at tech companies make more than the engineers.

Here's the thing nobody tells you though.

It's not really about which path you pick.
It's about how long you stick with it.
Most people switch every six months because they're not seeing results fast enough.
But the people who actually get rich? They picked something and stayed with it for years.

That's the whole thing. That's actually it.
Pick one. Go deep. Don't quit when it gets boring.
"""

VOICE = "en-US-AndrewMultilingualNeural"   # Deep, confident male voice
# Other great options:
#   "en-US-GuyNeural"              – Classic American male
#   "en-US-ChristopherNeural"      – Professional male
#   "en-GB-RyanNeural"             – British male
#   "en-US-JennyNeural"            – Friendly female
#   "en-US-AriaNeural"             – Expressive female

OUTPUT_FILE = "rich_in_2026_voiceover.mp3"
SUBTITLE_FILE = "rich_in_2026_subtitles.vtt"  # Optional WebVTT subtitles

RATE   = "+5%"   # Speed: -50% (slow) to +100% (fast). 0% = default
VOLUME = "+0%"   # Volume: -50% to +50%
PITCH  = "+0Hz"  # Pitch: -50Hz to +50Hz


# ─────────────────────────────────────────────
#  MAIN FUNCTIONS
# ─────────────────────────────────────────────
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