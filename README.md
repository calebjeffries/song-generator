# Song generator
A random song generator

## Format
- The program generates WAVE (.wav) audio
- The sample rate is cusomizable
- It generates music with signed short integer samples

## About the music
- The key is randomly generated
- It uses a randomly selected chord progression from `progressions.txt`
- It will generate a random melody with only the notes of the chords
- The melody has no rests or variation in the rhythm

## Usage
./main.py [-v] [-s samplerate] [-t tempo] [-l length] [-T time-signature] [-H happiness] [-c calmness] [-m match_percent] [-i instrument] file
- `-v`, `--verbose`: run in verbose mode
- `-s`, `--samplerate`: specify samplerate (default 48000Hz)
- `-t`, `--tempo`: specify tempo (default 120bpm)
- `-l`, `--length`: specify length in bars (default 32)
- `-T`, `--time-signature`: specify time signature (otherwise, it is randomly chosen)
- `-H`, `--happiness`: the happiness of your song from -100 (sad) to 100
- `-c`, `--calmness`: the calmness of your song from -100 (angry) to 100
- `-m`, `--match-percent`: the amount of tolerance for emotion picking
- `-i`, `--instrument`: the instrument file you will be using (e.g. "piano" for piano.toml)
- `-k`, `--key`: the key for your song (using only sharps and naturals; no flats)
