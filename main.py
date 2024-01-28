#!/bin/python3

import os
import struct
import math
import random
import argparse
import notes

def main():
  ts = args.time_signature.split("/")
  songkey = genkey()
  verboseinfo("key: " + songkey)
  verboseinfo("time signature: " + args.time_signature)
  verboseinfo("tempo: " + str(args.tempo) + "bpm")
  verboseinfo("number of bars: " + str(args.length))
  verboseinfo("samplerate: " + str(args.samplerate))
  songprogression = genchords(songkey, args.length)
  for barnum in range(0, args.length):
    addbar(songprogression[barnum], args.file + ".data", (args.samplerate * 60) / (args.tempo * (int(ts[1]) / 4)), int(ts[0]), args.samplerate)
  datasize = os.path.getsize(args.file + ".data")
  wavheader(args.file, datasize, args.samplerate, 8)
  datafile = open(args.file + ".data", "rb")
  data = datafile.readlines()
  datafile.close()
  os.remove(args.file + ".data")
  outfile = open(args.file, "ab")
  for line in data:
    outfile.write(line)
  outfile.close()

def verboseinfo(msg):
  if args.verbose == True:
    print(msg)

def addbar(chord, filename, notelength, notenum, samplerate):
  datafile = open(filename, "ab")
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

def gentimesig():
  commontimesigs = ["2/2", "2/4", "3/4", "4/4", "5/4", "7/4", "6/8", "9/8", "12/8"]
  return commontimesigs[int(random.random() * len(commontimesigs))]

def genkey():
  return notes.names[int(random.random() * len(notes.names))]

def genchords(key, bars):
  progressionfile = open("progressions.txt", "r")
  progressions = progressionfile.readlines()
  progressionfile.close()
  progression = progressions[int(random.random() * len(progressions))]
  verboseinfo("chord progression: " + progression)
  progression = progression.split()
  scale = notes.scale(key)
  chords = []
  for barnum in range(0, bars):
    chords.append(notes.romanchord(progression[barnum % len(progression)], key))
  return chords

def genmelody(chord):
  return notes.removeoctave(chord[int(random.random() * len(chord))]) + str(4 + int(random.random() * 2))

def chordwaves(chord, addr, vol, samplerate):
  amplitude = 127
  for i in range(0, len(chord)):
    amplitude += sine(notes.tofreq(chord[i]), addr, vol, samplerate)
  return amplitude

def sine(freq, addr, vol, samplerate):
  return int(math.sin(addr / ((samplerate / (math.pi * 2)) / freq)) * vol)

argparser = argparse.ArgumentParser(description = "Generate some music")
argparser.add_argument("file", type=str, help="File to write to")
argparser.add_argument("-v", "--verbose", default=False, action="store_true", help="Print extra information")
argparser.add_argument("-s", "--samplerate", default=48000, type=int, action="store", help="The number of samples per second in the output file")
argparser.add_argument("-t", "--tempo", default=120, type=int, action="store", help="The tempo (in beats per minute) for your song")
argparser.add_argument("-l", "--length", default=32, type=int, action="store", help="The number of bars for your song")
argparser.add_argument("-T", "--time-signature", type=str, action="store", default=gentimesig(), help="The time signature for your song (e.g. '4/4')")
args = argparser.parse_args()

main()
