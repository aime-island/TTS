import os

# Preprocess function so Sunneva can be used with TTS's generic dataloader
def sunneva(root_path, meta_file):
    txt_file = os.path.join(root_path, meta_file)
    items = []
    speaker_name = 'sunneva'
    with open(txt_file, 'r') as ttf:
        for line in ttf:
            cols = line.split("\t")
            text = cols[0]
            wav_file = os.path.join(root_path, "audio", cols[1] + ".wav")
            items.append([text, wav_file, speaker_name])
    return items