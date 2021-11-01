import basetxt

action = input("Encode/decode/encodefile/decode? (e/d/ef/df)")

if action == "e":
  s = input("String to encode:\n")
  print(basetxt.encode(s))
  print("---------------------")
if action == "d":
  s = input("String to decode:\n")
  print(basetxt.decode(s))
  print("---------------------")
if action == "ef":
  s = input("Enter string to decode to file:\n")
  f = open(s, "rb").read()
  print(basetxt.encode(f))
  print("---------------------")
if action == "df":
  s = input("String to decode:\n")
  fn = "decoded.bin"
  decoded = basetxt.decodeFile(s)
  with open(fn, "wb") as fw:
    fw.write(decoded)
