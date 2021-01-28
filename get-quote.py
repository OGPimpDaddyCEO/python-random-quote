import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 15
  rnd = random.randint(0,last)

  counter = 0
  
  while counter < 5:
    print(quotes[(rnd*counter)%last])
    counter += 1

if __name__== "__main__":
  primary()
