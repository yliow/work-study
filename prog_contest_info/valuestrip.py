import os

def print_neat(array):
  k = 0;
  for i in array:
    if k % 10 == 0 and k != 0:
      print()
    k += 1
    print(k + 1, i)
    
def print_all(small, medium, large):
  print("\n================SMALL:================\n",)
  print_neat(small)
  print("\n================MEDIUM:================\n",)
  print_neat(medium)
  print("\n================LARGE:================\n",)
  print_neat(large)

def find_skool(s, small, medium, large):
    search_term = s.lower()
    found = False

    def search_list(category_name, school_list):
        nonlocal found
        for school in school_list:
            if search_term in school.lower():
                print(f"MATCH FOUND: {school} ({category_name})")
                found = True

    search_list("SMALL", small)
    search_list("MEDIUM", medium)
    search_list("LARGE", large)

    if not found:
        print(f"No schools found matching '{s}'")
        
missouri = "moskool.csv"
kansas = "ksskool.csv"

f = open(os.getcwd() + '/%s' % missouri)
g = open(os.getcwd() + '/%s' % kansas)

lines = f.readlines()
lines += g.readlines()

small = []
medium = []
large = []

for i in lines:
  i = i.split(',')

  val = None
  if not i[5].isnumeric():
    val = 0
  else:
    val = int(i[5])
  
  if val <= 500:
    small.append(i[1])
  elif 500 < val <= 1000:
    medium.append(i[1])
  else:
    large.append(i[1])
    

while True:
  print("1. print all\n2. find size of school\n3. quit")
  option = int(input("enter option:"))

  match option:
    case 1:
      print_all(small,medium,large)
    case 2:
      skool2find = input("enter a school name:")
      find_skool(skool2find, small, medium, large)
    case 3:
      break
    case _:
      print("unknown option")
