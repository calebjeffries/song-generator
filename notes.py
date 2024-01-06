#!/bin/python3

import re

notes = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6", "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7", "C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8", "G#8", "A8", "A#8", "B8"]

names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def tofreq(name):
  if name == "C0":
    freq = 16.35
  elif name == "C#0" or name == "Db0":
    freq = 17.32
  elif name == "D0":
    freq = 18.35
  elif name == "D#0" or name == "Eb0":
    freq = 19.45
  elif name == "E0":
    freq = 20.6
  elif name == "F0":
    freq = 21.83
  elif name == "F#0" or name == "Gb0":
    freq = 23.12
  elif name == "G0":
    freq = 24.5
  elif name == "G#0" or name == "Ab0":
    freq = 25.96
  elif name == "A0":
    freq = 27.50
  elif name == "A#0" or name == "Bb0":
    freq = 29.14
  elif name == "B0":
    freq = 30.87
  elif name == "C1":
    freq = 32.70
  elif name == "C#1" or name == "Db1":
    freq = 34.65
  elif name == "D1":
    freq = 36.71
  elif name == "D#1" or name == "Eb1":
    freq = 38.89
  elif name == "E1":
    freq = 41.2
  elif name == "F1":
    freq = 43.65
  elif name == "F#1" or name == "Gb1":
    freq = 46.25
  elif name == "G1":
    freq = 49
  elif name == "G#1" or name == "Ab1":
    freq = 51.91
  elif name == "A1":
    freq = 55
  elif name == "A#1" or name == "Bb1":
    freq = 58.27
  elif name == "B1":
    freq = 61.74
  elif name == "C2":
    freq = 65.41
  elif name == "C#2" or name == "Db2":
    freq = 69.3
  elif name == "D2":
    freq = 73.42
  elif name == "D#2" or name == "Eb2":
    freq = 77.78
  elif name == "E2":
    freq = 82.41
  elif name == "F2":
    freq = 87.31
  elif name == "F#2" or name == "Gb2":
    freq = 92.5
  elif name == "G2":
    freq = 98
  elif name == "G#2" or name == "Ab2":
    freq = 103.83
  elif name == "A2":
    freq = 110
  elif name == "A#2" or name == "Bb2":
    freq = 116.54
  elif name == "B2":
    freq = 123.47
  elif name == "C3":
    freq = 130.81
  elif name == "C#3" or name == "Db3":
    freq = 138.59
  elif name == "D3":
    freq = 146.83
  elif name == "D#3" or name == "Eb3":
    freq = 155.56
  elif name == "E3":
    freq = 164.81
  elif name == "F3":
    freq = 174.61
  elif name == "F#3" or name == "Gb3":
    freq = 185
  elif name == "G3":
    freq = 196
  elif name == "G#3" or name == "Ab3":
    freq = 207.65
  elif name == "A3":
    freq = 220
  elif name == "A#3" or name == "Bb3":
    freq = 233.08
  elif name == "B3":
    freq = 246.94
  elif name == "C4":
    freq = 261.63
  elif name == "C#4" or name == "Db4":
    freq = 277.18
  elif name == "D4":
    freq = 293.66
  elif name == "D#4" or name == "Eb4":
    freq = 311.13
  elif name == "E4":
    freq = 329.63
  elif name == "F4":
    freq = 349.23
  elif name == "F#4" or name == "Gb4":
    freq = 369.99
  elif name == "G4":
    freq = 392
  elif name == "G#4" or name == "Ab4":
    freq = 415.30
  elif name == "A4":
    freq = 440
  elif name == "A#4" or name == "Bb4":
    freq = 466.16
  elif name == "B4":
    freq = 493.88
  elif name == "C5":
    freq = 523.25
  elif name == "C#5" or name == "Db5":
    freq = 554.37
  elif name == "D5":
    freq = 587.33
  elif name == "D#5" or name == "Eb5":
    freq = 622.25
  elif name == "E5":
    freq = 659.25
  elif name == "F5":
    freq = 698.46
  elif name == "F#5" or name == "Gb5":
    freq = 739.99
  elif name == "G5":
    freq = 783.99
  elif name == "G#5" or name == "Ab5":
    freq = 830.61
  elif name == "A5":
    freq = 880
  elif name == "A#5" or name == "Bb5":
    freq = 932.33
  elif name == "B5":
    freq = 987.77
  elif name == "C6":
    freq = 1046.5
  elif name == "C#6" or name == "Db3":
    freq = 1108.73
  elif name == "D6":
    freq = 1174.66
  elif name == "D#6" or name == "Eb6":
    freq = 1244.51
  elif name == "E6":
    freq = 1318.51
  elif name == "F6":
    freq = 1396.91
  elif name == "F#6" or name == "Gb6":
    freq = 1479.98
  elif name == "G6":
    freq = 1567.98
  elif name == "G#6" or name == "Ab6":
    freq = 1661.22
  elif name == "A6":
    freq = 1760
  elif name == "A#6" or name == "Bb6":
    freq = 1864.66
  elif name == "B6":
    freq = 1975.53
  elif name == "C7":
    freq = 2093
  elif name == "C#7" or name == "Db7":
    freq = 2217.46
  elif name == "D7":
    freq = 2349.32
  elif name == "D#7" or name == "Eb7":
    freq = 2489.02
  elif name == "E7":
    freq = 2637.02
  elif name == "F7":
    freq = 2793.83
  elif name == "F#7" or name == "Gb7":
    freq = 2959.96
  elif name == "G7":
    freq = 3135.96
  elif name == "G#7" or name == "Ab7":
    freq = 3322.44
  elif name == "A7":
    freq = 3520
  elif name == "A#7" or name == "Bb7":
    freq = 3729.31
  elif name == "B7":
    freq = 3951.07
  elif name == "C8":
    freq = 4186.01
  elif name == "C#8" or name == "Db8":
    freq = 4434.92
  elif name == "D8":
    freq = 4698.63
  elif name == "D#8" or name == "Eb8":
    freq = 4978.03
  elif name == "E8":
    freq = 5274.04
  elif name == "F8":
    freq = 5587.65
  elif name == "F#8" or name == "Gb8":
    freq = 5919.91
  elif name == "G8":
    freq = 6271.93
  elif name == "G#8" or name == "Ab8":
    freq = 6644.88
  elif name == "A8":
    freq = 7040
  elif name == "A#8" or name == "Bb8":
    freq = 7458.62
  elif name == "B8":
    freq = 7902.13
  else:
    raise Exception("Invalid note name")
  return freq

def majscale(note):
  notenames = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#"]
  noteindex = notenames.index(note)
  scalenotes = [notenames[noteindex], notenames[noteindex + 2], notenames[noteindex + 4], notenames[noteindex + 5], notenames[noteindex + 7], notenames[noteindex + 9], notenames[noteindex + 11]]
  return scalenotes

def chord(note, chordtype=""):
  index = notes.index(note)
  if chordtype == "m":
    notenames = [note, notes[index + 3], notes[index + 7]]
  elif chordtype == "#":
    notenames = [notes[index + 1], notes[index + 5], notes[index + 8]]
  elif chordtype == "b":
    notenames = [notes[index - 1], notes[index + 3], notes[index + 6]]
  elif chordtype == "dim":
    notenames = [note, notes[index + 3], notes[index + 6]]
  elif chordtype == "aug":
    notenames = [note, notes[index + 4], notes[index + 8]]
  elif chordtype == "sus":
    notenames = [note, notes[index + 5], notes[index + 7]]
  elif chordtype == "7":
    notenames = [note, notes[index + 4], notes[index + 7], notes[index + 10]]
  else:
    notenames = [note, notes[index + 4], notes[index + 7]]
  return notenames

def removeoctave(note):
  note = re.sub("\d+", "", note)
  return note
