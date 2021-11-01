import random
import codecs
import json

with codecs.open("basetxt_config.json", "r", "utf-8") as cfg:
  config = json.loads(cfg.read())

splitBy = config["splitBy"]
seperator = config["seperator"]

with codecs.open("unicode.txt", "r", "utf-8") as f:
  words = f.readlines()

#print(len(words))

words = [i.replace("\n", "") for i in words]
#print(words, len(words))

def splitBin(f):
  binStr = ""
  for i in f:
    binStr += bin(i).split("0b")[1].zfill(8)
  binStr = [int('0b' + binStr[i:i+splitBy], 2) for i in range(0, len(binStr), splitBy)]
  return binStr

def unsplit(f):
  binStr = ""
  for i in f:
    binStr += bin(i).split("0b")[1].zfill(splitBy)
  binStr = [int('0b' + binStr[i:i+8], 2) for i in range(0, len(binStr), 8)]
  return binStr

def wordEncode(bytes):
  splitbytes = splitBin(bytes)
  return seperator.join([words[i] for i in splitbytes])

def wordDecode(str):
  if seperator != "":
    strl = str.split(seperator)
  else:
    strl = [i for i in str]
  unsplitbytes = unsplit([words.index(i) for i in strl])
  return bytes(unsplitbytes)

def encode(s):
  str = s
  if len(str) % 3 != 0:
    print("Adding padding")
  if splitBy > 8:
    padding = 2
  else:
    padding = 1
  if type(str) == bytes:
    str += b"\x00" * padding
  else:
    str += "\x00" * padding

  if type(str) == bytes:
    encoded = wordEncode(str)
  else:
    encoded = wordEncode(str.encode("utf-8"))
  #Decoding doesnt require the padding character
  if encoded.split()[-1] == "A":
    return encoded[0:-1]
  else:
    return encoded

def decode(s):
  return wordDecode(s).decode("utf-8").replace("\x00", "")

def decodeFile(s):
  return wordDecode(s)[0:padding*-1]

#encodeTest = encode("Hey")
#decodeTest = decode(encodeTest)

#print("Encoded:", encodeTest)
#print("Decoded:", decodeTest)
