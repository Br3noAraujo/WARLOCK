#! encoding: utf-8
'''
WARLOCK by Br3noAraujo
'''
import random, sys, colorama

from random_word import RandomWords

r = RandomWords()


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
symbols = '@#!$&' # + 'çÇ'

# for more security
#import string
#lower = string.ascii_lowercase
#upper = string.ascii_uppercase
#num = string.digits
#symbols = string.punctuation


banner = f"""
     {colorama.Fore.LIGHTBLUE_EX}__/\__
. _  {colorama.Fore.WHITE}\\\\{colorama.Fore.YELLOW}''{colorama.Fore.WHITE}//{colorama.Fore.LIGHTBLUE_EX}
-{colorama.Fore.YELLOW}( ){colorama.Fore.LIGHTBLUE_EX}-/_{colorama.Fore.WHITE}||{colorama.Fore.LIGHTBLUE_EX}_\\
 .'. \_{colorama.Fore.YELLOW}(){colorama.Fore.LIGHTBLUE_EX}_/ {colorama.Fore.BLUE}WARLOCK
  |   | . \\
  |   | .  \\
 .'. ,\_____'.
"""


all = lower + upper + num + symbols

def gen_pass(length):
    try:
        temp = random.sample(all, length)
        password = "".join(temp)
        print (f'{banner}🔐PASSWORD🧙 ==> {colorama.Fore.YELLOW}{password}{colorama.Fore.WHITE}\n\n')
    except ValueError:
        print (f"\n\n{banner}{colorama.Fore.LIGHTCYAN_EX}\n\nThis password is very strong for me. Sorry! Try one less password!\n\n{colorama.Fore.WHITE}")
        

def gen_leet():
    leetpass = r.get_random_word()
    leetpass = leetpass.replace('a', '4')
    leetpass = leetpass.replace('e', '3')
    leetpass = leetpass.replace('i', '1')
    leetpass = leetpass.replace('o', '0')
    
    print (f'{banner}🔐PASSWORD🧙 ==> {colorama.Fore.YELLOW}{leetpass}{colorama.Fore.WHITE}\n\n')
    
def main():
    
    if len(sys.argv) <= 1:
        gen_pass(length=12)
    
    try:
        if sys.argv[1] == "--leet":
            gen_leet()
            exit()
            
    except:
        exit()
    try:   
        length = int(sys.argv[1])
        gen_pass(length)
    except ValueError:
        print (f"\n\n{banner}{colorama.Fore.LIGHTCYAN_EX}\n\nUSAGE: python warlock.py <length: max 67, default 12.> OR python warlock.py --leet\npython warlock -h to show this message\n\n--leet: Less secure but easier to decorate\n\n{colorama.Fore.WHITE}")

if __name__ == "__main__":
    main()