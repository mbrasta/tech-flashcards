from gtts import gTTS
import os

# Arabic words for each tech item
arabic_words = {
    "mobile": "هاتف محمول",
    "laptop": "حاسوب محمول",
    "tablet": "جهاز لوحي",
    "airpods": "سماعات أيربودز",
    "smartwatch": "ساعة ذكية",
    "headphones": "سماعات رأس"
}

# Directory to save the MP3s
output_dir = "audio"
os.makedirs(output_dir, exist_ok=True)

# Generate and save each audio file
file_paths = {}
for key, word in arabic_words.items():
    tts = gTTS(word, lang='ar')
    file_path = os.path.join(output_dir, f"{key}.mp3")
    tts.save(file_path)
    file_paths[key] = file_path

print("Audio files generated:")
for path in file_paths.values():
    print(path)
