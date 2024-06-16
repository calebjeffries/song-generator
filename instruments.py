#!/bin/python3

import tomllib
import math
import notes
import struct
import tqdm

# Generate a song based on the data given
def gensong(length, filename, samplerate, tempo, instrument, volume, ts, progression, melody):
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
      gennote(progression[barnum], instrumentharmonics, instrumentenvelope, melody[address], volume, (samplerate * 60) / (tempo * (int(ts[1]) / 4)), samplerate, address)
  for i in range(0, len(outarray)):
    if outarray[i] > 32767:
      outarray[i] = 32767
    elif outarray[i] < -32767:
      outarray[i] = -32767
  return outarray

# Add a note to the data file
def gennote(chord, harmonics, envelope, melody, vol, notelength, samplerate, addr):
  for address in range(0, int(notelength + envelope[3] * srms)):
    if address < envelope[0] * srms:
      volume = address / (envelope[0] * srms) * vol
    elif address < (envelope[1] + envelope[0]) * srms:
      volume = vol - (((100 - envelope[2]) / 100) * vol * (address - envelope[0] * srms) / (envelope[1] * srms))
    elif address < notelength:
      volume = (envelope[2] / 100) * vol
    else:
      volume = (envelope[2] / 100) * vol - ((address - notelength) / (envelope[3] * srms) * (envelope[2] / 100) * vol)
    output = chordwaves(chord, address, 15 * (volume / 100), samplerate, notelength, harmonics) + instrumentwave(notes.tofreq(melody), address, 20 * (volume / 100), samplerate, notelength, harmonics)
    outarray[int(addr * notelength + address)] += int(output)

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
