import os, re, sys

global execNum
execNum = 0

def validFile(filename):
  return (not(filename.startswith(".")) and (os.path.splitext(filename)[1] in suppExt) and not((filename == __file__.replace(".\\", ""))) or os.path.isdir(filename))

def removeSubstr(filepath):
  match = re.search(pattern, filepath)
  if match:
    print("Removing substr on file:", filepath)
    global execNum
    execNum += 1
    os.rename(filepath, filepath[match.end():])


def browsing(path):
  for file in os.listdir(path):
    if validFile(file):
      if os.path.isdir(file):
        os.chdir(file)
        browsing(os.getcwd())
        os.chdir("..")
      else:
        removeSubstr(file)
    else:
      continue


def main():
  # Getting things ready
  global suppExt
  suppExt = []
  global pattern
  pattern = ""

  folder = input("Root folder: ")
  extensions = input('Supported extensions (Ex.: ".mp3, .jpg"): ').split(",")
  for extension in extensions:
    suppExt.append(extension)
  pattern = input('Substring to remove: ("NN " -  2 digit number followed by a space): ').replace("N", "\d").replace("S", "\A")
  pattern = re.compile(pattern)
  os.chdir(folder)
  browsing(os.getcwd())
  if execNum:
    print("%d file(s) were found and renamed" % execNum)
  else:
    print("No eligible file was found")


if __name__ == '__main__':
  main()