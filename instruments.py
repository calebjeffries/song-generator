#!/bin/python3

import tomllib
import math
import notes
import tqdm

# Generate a song based on the data given
def gensong(length, samplerate, tempo, instrument, volume, ts, progression, melody):
  global srover2pi
  srover2pi = samplerate / (2 * math.pi)
  global srms
  srms = samplerate / 1000
  instrumentfile = open("instruments/" + instrument + ".toml", "rb")
  instrumentdata = tomllib.load(instrumentfile)
  instrumentharmonics = instrumentdata['harmonics']
  instrumentenvelope = instrumentdata['envelope']
  global outarray
  outarray = [0] * int((length * int(ts[0]) * (samplerate * 60) / (tempo * (int(ts[1]) / 4)) + instrumentenvelope[3] * srms))
  for barnum in tqdm.tqdm(range(0, length)):
    for beatnum in range(0, int(ts[0])):
      address = barnum * int(ts[0]) + beatnum
      gennote(progression[barnum], instrumentharmonics, instrumentenvelope, melody[address], volume, (samplerate * 60) / (tempo * (int(ts[1]) / 4)), address)
  for i in range(0, len(outarray)):
    if outarray[i] > 32767:
      outarray[i] = 32767
    elif outarray[i] < -32767:
      outarray[i] = -32767
  return outarray

# Add a note to the data file
def gennote(chord, harmonics, envelope, melody, vol, notelength, addr):
  # Attack
  volumecalculationconst1 = 1 / (envelope[0] * srms * vol) # Makes calculation easier
  for address in range(0, int(envelope[0] * srms)):
    volume = address * volumecalculationconst1
    output = chordwaves(chord, address, 15 * (volume / 100), harmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), harmonics)
    outarray[int(addr * notelength + address)] += int(output)
  # Decay
  volumecalculationconst1 = (100 - envelope[2]) * vol / (envelope[1] * srms * 100)
  for address in range(int(envelope[0]), int(envelope[0] + envelope[1] * srms)):
    volume = vol - volumecalculationconst1 * (address - envelope[0] * srms)
    output = chordwaves(chord, address, 15 * (volume / 100), harmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), harmonics)
    outarray[int(addr * notelength + address)] += int(output)
  # Sustain
  volume = (envelope[2] / 100) * vol
  for address in range(int(envelope[0] + envelope[1]), int(notelength)):
    output = chordwaves(chord, address, 15 * (volume / 100), harmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), harmonics)
    outarray[int(addr * notelength + address)] += int(output)
  # Release
  volumecalculationconst1 = envelope[2] * vol / 100
  volumecalculationconst2 = envelope[2] * vol / (envelope[3] * srms * 100)
  for address in range(int(notelength), int(notelength + envelope[3])):
    volume = volumecalculationconst1 - (address - notelength) * envelope[2] * volumecalculationconst2
    output = chordwaves(chord, address, 15 * (volume / 100), harmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), harmonics)
    outarray[int(addr * notelength + address)] += int(output)

# Generate the waves for a chord
def chordwaves(chord, addr, vol, instrumentharmonics):
  amplitude = 0
  for i in range(0, len(chord)):
    amplitude += instrumentwave(notes.tofreq(chord[i]), addr, vol, instrumentharmonics)
  return amplitude

# Generate waves for a certain instrument
def instrumentwave(freq, addr, vol, instrumentharmonics):
  amplitude = 0
  for harmonicnum in range(1, len(instrumentharmonics) + 1):
    amplitude += math.sin(addr * freq * harmonicnum / srover2pi) * ((vol * 255) * (instrumentharmonics[harmonicnum - 1] / 100))
  return amplitude