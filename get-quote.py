import random

def primary():
  

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) -1
  rnd = random.randint(0,last)
  
  
  #q1 = quotes.rstrip([rnd], "\n")
  
  #print(q1)
  print(quotes[rnd]), print(quotes[rnd + 1])

if __name__== "__main__":
  primary()
