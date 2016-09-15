#!/usr/bin/python3

defs = {}
depth = 0
maxDepth = 20

def execute(line):
  global depth
  depth += 1
  if depth > maxDepth:
    return ""
  result = ""
  for c in line:
    if c in defs:
      if c == defs[c]:
        result += c
      else:
        result += execute(defs[c])
    else: 
      result += c
  return result

def parse(line):
  if ':' in line:
    parts = line.split(":")
    defs[parts[0]] = parts[1] 
  else:
    print(execute(line))

if __name__ == '__main__':
  import sys
  f = open(sys.argv[1])

  for line in f:
    parse(line.rstrip())
  #print(defs)
