#!/bin/python3

import struct
import random
import argparse
import notes
import instruments

def main():
  ts = args.time_signature.split("/")
  verboseinfo("key: " + args.key)
  verboseinfo("time signature: " + args.time_signature)
  verboseinfo("tempo: " + str(args.tempo) + "bpm")
  verboseinfo("number of bars: " + str(args.length))
  verboseinfo("samplerate: " + str(args.samplerate))
  songprogression = genchords(args.key, args.length)
  songmelody = [];
  for barnum in range(0, args.length):
    for i in range(0, int(ts[0])):
      songmelody.append(genmelody(songprogression[barnum]))
  wavdata = instruments.gensong(args.length, args.samplerate, args.tempo, args.instrument, args.volume, ts, songprogression, songmelody)
  wavheader(args.file, len(wavdata) * 2, args.samplerate, 16)
  outfile = open(args.file, "ab")
  for sample in wavdata:
    outfile.write(struct.pack("@h", sample))
  outfile.close()

def verboseinfo(msg):
  if args.verbose == True:
    print(msg)

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
  while (True):
    progressionline = progressions[int(random.random() * len(progressions))]
    progression = progressionline.split(":")[0]
    emotion = progressionline.split(":")[1]
    emotion = emotion.split()
    emotions = [int(emotion[0]) - int(emotion[1]), int(emotion[2]) - int(emotion[3])]
    if emotions[0] < args.happiness + args.match_percent * 2 and emotions[0] > args.happiness - args.match_percent * 2 and emotions[1] < args.calmness + args.match_percent * 2 and emotions[1] > args.calmness - args.match_percent * 2:
      verboseinfo("chord progression: " + progression)
      progression = progression.split()
      chords = []
      for barnum in range(0, bars):
        chords.append(notes.romanchord(progression[barnum % len(progression)], key))
      return chords

def genmelody(chord):
  return notes.removeoctave(chord[int(random.random() * len(chord))]) + str(4 + int(random.random() * 2))

argparser = argparse.ArgumentParser(description = "Generate some music")
argparser.add_argument("file", type=str, help="File to write to")
argparser.add_argument("-H", "--happiness", type=int, action="store", default=0, help="The happiness of your song, from -100 to 100")
argparser.add_argument("-c", "--calmness", type=int, action="store", default=0, help="The calmness of your song, from -100 to 100")
argparser.add_argument("-m", "--match-percent", type=int, action="store", default=100, help="The match percent tolerence, don't set too low!")
argparser.add_argument("-v", "--verbose", default=False, action="store_true", help="Print extra information")
argparser.add_argument("-s", "--samplerate", default=48000, type=int, action="store", help="The number of samples per second in the output file")
argparser.add_argument("-V", "--volume", default=100, type=int, action="store", help="The volume of your song (setting this too high causes distortion)")
argparser.add_argument("-t", "--tempo", default=120, type=int, action="store", help="The tempo (in beats per minute) for your song")
argparser.add_argument("-l", "--length", default=32, type=int, action="store", help="The number of bars for your song")
argparser.add_argument("-i", "--instrument", type=str, action="store", default="piano", help="The instrument used in your song")
argparser.add_argument("-T", "--time-signature", type=str, action="store", default=gentimesig(), help="The time signature for your song (e.g. '4/4')")
argparser.add_argument("-k", "--key", type=str, action="store", default=genkey(), help="The key for your song")
args = argparser.parse_args()

main()