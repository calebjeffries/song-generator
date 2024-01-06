#!/bin/python3

import os
import struct
import math
import random
import notes

def main():
  print("Please enter the name of the file that you will write to: ")
  filename = input()
  print("Please enter the sample rate of the output file: ")
  samplerate = int(input())
  print("Please enter the bpm for your song: ")
  bpm = int(input())
  print("Please enter the time signature (numerator) for your song: ")
  tsnum = int(input())
  print("Please enter the time signature (denominator) for your song: ")
  tsden = int(input())
  print("Please enter the length (in bars) for your song: ")
  length = int(input())
  songkey = genkey()
  for barnum in range(0, length):
    addbar(songkey, filename + ".data", (samplerate * 60) / (bpm * (tsden / 4)), tsnum, samplerate)
  datasize = os.path.getsize(filename + ".data")
  wavheader(filename, datasize, samplerate, 8)
  datafile = open(filename + ".data", "rb")
  data = datafile.readlines()
  datafile.close()
  os.remove(filename + ".data")
  outfile = open(filename, "ab")
  for line in data:
    outfile.write(line)
  outfile.close()

def addbar(key, filename, notelength, notenum, samplerate):
  datafile = open(filename, "ab")
  chord = genchord(key)
  for beatnum in range(0, notenum):
    melody = genmelody(chord)
    for address in range(0, int(notelength)):
      output = chordwaves(chord, address, 20, samplerate) + sine(notes.tofreq(melody), address, 20, samplerate)
      datafile.write(struct.pack("@B", output))
  datafile.close()

def wavheader(file, datalength, samplerate, bitspersample):
  outfile = open(file, "wb")
  outfile.write(b'RIFF')
  outfile.write(struct.pack("<I", datalength + 44))
  outfile.write(b'WAVEfmt ')
  outfile.write(struct.pack("<I", 16))
  outfile.write(struct.pack("<H", 1))
  outfile.write(struct.pack("<H", 1))
  outfile.write(struct.pack("<I", samplerate))
  outfile.write(struct.pack("<I", int((samplerate * bitspersample) / 8)))
  outfile.write(struct.pack("<H", int(bitspersample / (bitspersample / 2))))
  outfile.write(struct.pack("<H", bitspersample))
  outfile.write(b'data')
  outfile.write(struct.pack("<I", datalength))
  outfile.close()

def genkey():
  return notes.names[int(random.random() * len(notes.names))]

def genchord(key):
  scale = notes.majscale(key)
  rand = int(random.random() * 10)
  if rand < 3:
    chordkey = 4
  elif rand < 6:
    chordkey = 3
  else:
    chordkey = 0
  chord = notes.chord(scale[chordkey] + "3")
  return chord

def genmelody(chord):
  return notes.removeoctave(chord[int(random.random() * len(chord))]) + str(4 + int(random.random() * 2))

def chordwaves(chord, addr, vol, samplerate):
  amplitude = 127
  for i in range(0, len(chord)):
    amplitude += sine(notes.tofreq(chord[i]), addr, vol, samplerate)
  return amplitude

def sine(freq, addr, vol, samplerate):
  return int(math.sin(addr / ((samplerate / (math.pi * 2)) / freq)) * vol)

main()
