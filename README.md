# Generate_music_using_librarie_MIDIUtil
this script generates a MIDI file with a single track containing a sequence of four notes. It uses the `midiutil` library to create the MIDI file.

## Prerequisites

Make sure you have Python installed on your system. You can install the required library using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/NoorMahammad-S/Generate_music_using_librarie_MIDIUtil.git
cd Generate_music_using_librarie_MIDIUtil
```

2. Run the script:

```bash
python main.py
```

The script will generate a MIDI file named `output_channel_0.mid` in the same directory.

## Customization

- **MIDI Channels:** The script currently uses channel 0. You can customize the channel in the `main.py` file if needed.

- **Note Duration:** Adjust the `duration` variable based on your desired tempo and musical structure.

- **Note Range:** Experiment with the starting pitch and the range of notes to achieve the desired musical output.

- **Output File Name:** The script saves the MIDI file with a dynamic name based on the channel used.
