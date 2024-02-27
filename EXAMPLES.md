# Example usage
Options to make different sounding songs

## Generate a song quickly
These options decrease the generation time
- `-s 16000` will decrease the sample rate, which won't sound as good. You can lower this even more if you want to generate really quickly. High pitches may be affected by this option 
- `--harmonics 1` will make the song sound less full. This will significantly decrease the generation time.

## Angry
- `-V 1000` will make the sine waves distorted. You can increase/decrease the number to make it sound more/less distorted. Anything lower than 100 will not sound distorted.
- `-c -100 -m 50` will choose angry chords.
- `-t 140` will speed up the song. You can increase this number even more.

## Calm
- `-c 100 -m 50` will choose calm chords.
- `-t 100` will make it slower. You can decrease this number even more.

## Happy
- `-H 100 -m 50` will choose happy chords.
- `-T 4/4` will make a time signature similar to a lot of pop music.

## Sad
- `-H -100 -m 50` will choose sad chords.
- `-t 100` will make it slower. You can decrease this number even more.

## Different wave forms
- Square waves can be made by increasing the volume, and distorting the waves. `-V 1000` will make square waves. The value can be increased if you want to make it sound even more similar.
- Sawtooth waves can be made by adding more and more harmonics. `--harmonics 50` will make sawtooth waves. The value can be increased more if you want it to sound even more similar. Setting this too high will greatly affect the generation time.
- Sine waves are the default, but they have other frequencies added. `--harmonics 1` will not add these extra frequencies.
