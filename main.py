class element():
  def __init__(self, name, amu, p):
    self.name = name
    self.amu = amu
    self.p = p

# neutrons utilizes the averaged atomic mass
table = {
  "H" : element("hydrogen", 1.008, 1),
  "He" : element("helium", 4.003, 2),
  "Li" : element("lithium", 6.941, 3),
  "Be" : element("beryllium", 9.012, 4),
  "B" : element("boron", 10.811, 5),
  "C" : element("carbon", 12.011, 6),
  "N" : element("nitrogen", 14.007, 7),
  "O" : element("oxygen", 15.999, 8),
  "F" : element("fluorine", 18.998, 9),
  "Ne" : element("neon", 20.180, 10),
  "Na" : element("sodium", 22.990, 11),
  "Mg" : element("magnesium", 24.305, 12),
  "Al" : element("aluminum", 26.982, 13),
  "Si" : element("silicon", 28.086, 14),
  "P" : element("phosphorus", 30.974, 15),
  "S" : element("sulfur", 32.066, 16),
  "Cl" : element("chlorine", 35.453, 17),
  "Ar" : element("argon", 39.948, 18),
  "K" : element("potassium", 39.098, 19),
  "Ca" : element("calcium", 40.078, 20),
  "Sc" : element("scandium", 44.956, 21),
  "Ti" : element("titanium", 47.88, 22),
  "V" : element("vanadium", 50.942, 23),
  "Cr" : element("chromium", 51.996, 24),
  "Mn" : element("manganese", 54.938, 25),
  "Fe" : element("iron", 55.847, 26),
  "Co" : element("cobalt", 58.933, 27),
  "Ni" : element("nickel", 58.7, 28),
  "Cu" : element("copper", 63.55, 29),
  "Zn" : element("zinc", 65.38, 30),
  "Ga" : element("gallium", 69.72, 31),
  "Ge" : element("germanium", 72.59, 32),
  "As" : element("arsenic", 74.92, 33),
  "Se" : element("selenium", 78.96, 34),
  "Br" : element("bromine", 79.904, 35),
  "Kr" : element("krypton", 83.8, 36),
  "Rb" : element("rubidinium", 85.468, 37),
  "Sr" : element("strontium", 87.62, 38),
  "Y" : element("yttrium", 88.906, 39),
  "Zr" : element("zirconium", 91.224, 40),
  "Nb" : element("niobium", 92.906, 41),
  "Mo" : element("molybdenum", 95.95, 42),
  "Tc" : element("technetium", 98.907, 43),
  "Ru" : element("ruthenium", 101.07, 44),
  "Rh" : element("rhodium", 102.906, 45),
  "Pd" : element("palladium", 106.42, 46),
  "Ag" : element("silver", 107.868, 47),
  "Cd" : element("cadmium", 112.41, 48),
  "In" : element("indium", 114.818, 49),
  "Sn" : element("tin", 118.711, 50),
  "Sb" : element("antimony", 121.76, 51),
  "Te" : element("tellurium", 127.6, 52),
  "I" : element("iodine", 126.904, 53),
  "Xe" : element("xenon", 131.3, 54),
  "Cs" : element("cesium", 132.91, 55),
  "Ba" : element("barium", 137.33, 56),
  "La" : element("lanthanum", 138.906, 57),
  "Ce" : element("cerium", 140.12, 58),
  "Pr" : element("praseodymium", 140.908, 59),
  "Nd" : element("neodymium", 144.24, 60),
  "Pm" : element("promethium", 145, 61),
  "Sm" : element("samarium", 150.4, 62),
  "Eu" : element("europium", 151.96, 63),
  "Gd" : element("gadolinium", 157.25, 64),
  "Tb" : element("terbium", 158.925, 65),
  "Dy" : element("dysprosium", 162.5, 66),
  "Ho" : element("holmium", 164.9304, 67),
  "Er" : element("erbium", 167.26, 68),
  "Tm" : element("thulium", 168.9342, 69),
  "Yb" : element("ytterbium", 173.04, 70),
  "Lu" : element("lutetium", 174.967, 71),
  "Hf" : element("hafnium", 178.49, 72),
  "Ta" : element("tantalum", 180.947, 73),
  "W" : element("tungten", 183.85, 74),
  "Re" : element("rhenium", 186.207, 75),
  "Os" : element("osmium", 190.2, 76),
  "Ir" : element("iridium", 192.22, 77),
  "Pt" : element("platinum", 195.08, 78),
  "Au" : element("gold", 196.967, 79),
  "Hg" : element("mercury", 200.59, 80),
  "Tl" : element("thallium", 204.37, 81),
  "Pb" : element("lead", 207.2, 82),
  "Bi" : element("bismuth", 208.98, 83),
  "Po" : element("polonium", 209, 84),
  "At" : element("astatine", 210, 85),
  "Rn" : element("radon", 222, 86),
  "Fr" : element("francium", 223, 87),
  "Ra" : element("radium", 226.025, 88),
  "Ac" : element("actinium", 227.028, 89),
  "Th" : element("thorium", 232.038, 90),
  "Pa" : element("protactinium", 231.036, 91),
  "U" : element("uranium", 238.029, 92),
  "Np" : element("neptunium", 237.048, 93),
  "Pu" : element("plutonium", 244.064, 94),
  "Am" : element("americium", 243.061, 95),
  "Cm" : element("curium", 247.07, 96),
  "Bk" : element("berkelium", 247.07, 97),
  "Cf" : element("californium", 251.08, 98),
  "Es" : element("einsteinium", 254, 99),
  "Fm" : element("fermium", 257.095, 100),
  "Md" : element("mendelevium", 258.1, 101),
  "No" : element("nobelium", 259.101, 102),
  "Lr" : element("lawrencium", 262, 103),
  "Rf" : element("rutherfordium", 261, 104),
  "Db" : element("dubnium", 262, 105),
  "Sg" : element("seaborgium", 266, 106),
  "Bh" : element("bohrium", 264, 107),
  "Hs" : element("hassium", 269, 108),
  "Mt" : element("meitnerium", 278, 109),
  "Ds" : element("darmstadtium", 281, 110),
  "Rg" : element("roentgenium", 280, 111),
  "Cn" : element("copernicium", 285, 112),
  "Nh" : element("nihonium", 286, 113),
  "Fl" : element("flevorium", 289, 114),
  "Mc" : element("moscovium", 289, 115),
  "Lv" : element("livermorium", 293, 116),
  "Ts" : element("tennessine", 294, 117),
  "Og" : element("oganesson", 294, 118),
}

mode = input("mode: mole calculations(m)? ")

if mode == 'm':
  print("ctrl-c to quit.")
  print("if you are looking for the molar mass of a compound, type in the individual atoms with their count, then look for \"sum\".")
  sum = 0
  prev_mass = 0
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
      sum += (table.get(element).amu * times)
      print("name: " + table.get(element).name)
      print("amu: " + str(table.get(element).amu))
      print("protons: " + str(table.get(element).p))
      print()
      print("SUM: " + str(round(sum, 3)))
      prev_mass = round(table.get(element).amu * times, 3)

    except:
      if (element == 'c'):
        print("cleared.")
        sum = 0
        continue
      elif element == 'd':
        print("deleted previous: " + str(prev_mass))
        sum -= prev_mass
        sum = round(sum, 3)
        print("new sum: " + str(sum))
        continue
      print("unable to make the calculation, try again.")
    sum = round(sum, 3)
    print()




# print(table.get("Dy").name)