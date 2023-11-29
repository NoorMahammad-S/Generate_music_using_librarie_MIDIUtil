from midiutil import MIDIFile

def generate_music():
    # Create a MIDI file with one track
    midi = MIDIFile(1)

    # Add a track name and tempo
    midi.addTrackName(0, 0, "Sample Track")
    midi.addTempo(0, 0, 120)

    # Add notes
    channel = 0
    start_time = 0  # Start time for the first note
    volume = 100  # 0-127, as per the MIDI standard

    # Add a series of notes to the track
    for i in range(4):
        pitch = 60 + i  # MIDI note number for middle C and higher
        duration = 1  # in beats
        midi.addNote(channel, 0, pitch, start_time, duration, volume)
        start_time += duration  # Move to the next beat for the next note

    # Save the MIDI file
    with open("output.mid", "wb") as midi_file:
        midi.writeFile(midi_file)

if __name__ == "__main__":
    generate_music()
