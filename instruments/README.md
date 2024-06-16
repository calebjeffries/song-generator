# Customizable instruments

## Format
The instrument data is written in TOML

## Parameters
- harmonicnum (int): the number of harmonics (adding more will make the generation time longer)
- harmonics (array): the harmonics (starting with the fundamental) and their amplitude (a percentage)
- envelope (array): each index means something different
	1. the attack time (in ms)
	2. the decay time (in ms)
	3. the sustain level (as a percentage of the the starting volume)
	4. the release time (in ms)

## Example
```
harmonicnum = 4
harmonics = [ 100, 50, 25, 13 ]
envelope = [ 10, 500, 75, 200 ]
```
