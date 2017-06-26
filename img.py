try:
  from random import randint,randint,shuffle,seed
except ImportError as e:
  print(e)
try:
  from sys import exit,argv
except ImportError as e:
  print(e)
try:
  import argparse
except ImportError as e:
  print(e)

def Banner():
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  hh = randint(0,40)
  print('_'*hh+' '+'_'*hh)
  print('\n')


if __name__ == '__main__':
  Banner()
  parse = argparse.ArgumentParser(description='Images effects by Elllender :)',prog='main.py')
  parse.add_argument('-p','--path',help="Image path.")
  parse.add_argument('-s','--save',help="Save image in path")
  parse.add_argument('-g','--grad',help="Effect.")
  parse.add_argument('-n','--nois',help="Effect.")
  parse.add_argument('-u','--usage',help="Example : python3 img.py -p image.png -s new_image.png -n")
  args = parse.parse_args()
  if args.path:
    path = str(args.path)
    if args.save:
      path_save = str(args.save)
    else:
      print('[-] Please set output path. -h --help')
  else:
    print('[-] Please set path witch image. -h --help')


if args.grad:
  import effect2
  effect2.effect2(path,path_save)
if args.nois:
  import effect
  effect.effect(path,path_save)

