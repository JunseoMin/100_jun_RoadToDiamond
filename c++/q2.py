import random

def main():
  correct = False
  randN = random.randint(1,100)
  trial = 0

  print("generated num: ", randN)

  while not correct:
    print("guess the num between 1~100")
    trial += 1
    inN = int(input())

    if inN == randN:
      correct = True
      print("answer is: ", randN)
      print("Cong! you tried {} times".format(trial))
    
    if inN < randN:
      print("low")
    
    if inN > randN:
      print("high")

if __name__ == "__main__":
  try:
    main()
  except:
    print("error!")