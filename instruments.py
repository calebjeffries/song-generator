#!/bin/python3

import tomllib
import math
import notes
import struct

# Add a note to the data file
def gennote(chord, instrumentfile, melody, vol, notelength, samplerate, datafile):
  global srover2pi
  srover2pi = samplerate / (2 * math.pi)
  instrumentfile = open(instrumentfile, "rb")
  instrumentdata = tomllib.load(instrumentfile)
  instrumentharmonics = instrumentdata['harmonics']
  envelope = instrumentdata['envelope']
  for address in range(0, int(notelength)):
    if address < envelope[0] * (samplerate / 1000):
      volume = address / (envelope[0] * (samplerate / 1000)) * vol
    elif address < (envelope[1] + envelope[0]) * (samplerate / 1000):
      volume = vol - (((100 - envelope[2]) / 100) * vol * (address - envelope[0] * (samplerate / 1000)) / (envelope[1] * (samplerate / 1000)))
    elif address < notelength - envelope[3] * (samplerate / 1000):
      volume = (envelope[2] / 100) * vol
    else:
      volume = (envelope[2] / 100) * vol - ((address - notelength + envelope[3] * (samplerate / 1000)) / (envelope[3] * (samplerate / 1000)) * (envelope[2] / 100) * vol)
    output = chordwaves(chord, address, 15 * (volume / 100), samplerate, notelength, instrumentharmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), samplerate, notelength, instrumentharmonics)
    if output > 32767:
      output = 32767
    elif output < -32767:
      output = -32767
    datafile.write(struct.pack("@h", int(output)))

# Generate the waves for a chord
def chordwaves(chord, addr, vol, samplerate, notelength, instrumentharmonics):
  amplitude = 0
  for i in range(0, len(chord)):
    amplitude += instrumentwave(notes.tofreq(chord[i]), addr, vol, samplerate, notelength, instrumentharmonics)
  return amplitude

# Generate waves for a certain instrument
def instrumentwave(freq, addr, vol, samplerate, notelength, instrumentharmonics):
  amplitude = 0
  for harmonicnum in range(1, len(instrumentharmonics)):
    amplitude += math.sin(addr / (srover2pi / (freq * harmonicnum))) * ((vol * 255) * (instrumentharmonics[harmonicnum] / 100))
  return amplitude
