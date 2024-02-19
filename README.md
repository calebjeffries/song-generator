# Song generator
A random song generator

## Format
- The program generates WAVE (.wav) audio
- The sample rate is cusomizable
- It is limited to 8 bits per sample (for now)

## About the music
- The key is randomly generated
- It uses a randomly selected chord progression from `progressions.txt`
- It will generate a random melody with only the notes of the chords
- The melody has no rests or variation in the rhythm

## Usage
./main.py [-v] [-s samplerate] [-t tempo] [-l length] [-T time-signature] file
- `-v`, `--verbose`: run in verbose mode
- `-s`, `--samplerate`: specify samplerate (default 48000Hz)
- `-t`, `--tempo`: specify tempo (default 120bpm)
- `-l`, `--length`: specify length in bars (default 32)
- `-T`, `--time-signature`: specify time signature (otherwise, it is randomly chosen)
