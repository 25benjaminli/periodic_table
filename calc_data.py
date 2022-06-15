
def calc():
  import main
  print("ctrl-c to quit.")
  print("if you are looking for the molar mass of a compound, type in the individual atoms with their count, then look for \"sum\".")
  sum = 0
  prev_mass = 0
  compound = ""
  prev_element = ""
  while(True):
    thing = input("symbol, (c - clear), (d - delete prev) then count: ")
    what = ""
    counter = 0
    for i in range(len(thing)):
      if thing[counter].isnumeric():
        what += thing[counter:len(thing)]
        break
      counter += 1
    if len(what) == 0:
      times = 1
    else:
      times = int(what)
    
    element = thing[0:counter]
    
    try:
      if (element == 'c' or element == 'd'):
        int("hi") # break into except stupidly
      print("you want to multiply your element, " + element + ", by " + str(times) + " times, correct?")
      sum += (main.table.get(element).amu * times)
      compound += (str(element) + str(times)) if times > 1 else (str(element))
      print("name: " + main.table.get(element).name)
      print("amu: " + str(main.table.get(element).amu))
      print("protons: " + str(main.table.get(element).p))
      print("valence electrons: " + str(main.table.get(element).valence))
      print()
      print("SUM: " + str(round(sum, 3)))
      print("Current compound: " + compound)
      prev_mass = round(main.table.get(element).amu * times, 3)
  
    except:
      if (element == 'c'):
        print("cleared.")
        sum = 0
        compound = ""
        continue
      elif element == 'd':
        print("deleted previous: " + str(prev_mass))
        sum -= prev_mass
        sum = round(sum, 3)
        print("new sum: " + str(sum))
        compound = compound[0:len(compound)-len(prev_element)] if prev_element != "" else ""
        continue
      print("unable to make the calculation, try again.")
    sum = round(sum, 3)
    prev_element = element
    print()