#! encoding: utf-8
'''
WARLOCK by Br3noAraujo
A secure and flexible password generator
'''
import random
import sys
import string
import argparse
import colorama
from typing import Optional
from random_word import RandomWords

class PasswordGenerator:
    def __init__(self):
        self.r = RandomWords()
        # Using string constants for better security
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.num = string.digits
        self.symbols = string.punctuation
        self.all = self.lower + self.upper + self.num + self.symbols
        
        self.banner = f"""
     {colorama.Fore.LIGHTBLUE_EX}__/\__
. _  {colorama.Fore.WHITE}\\\\{colorama.Fore.YELLOW}''{colorama.Fore.WHITE}//{colorama.Fore.LIGHTBLUE_EX}
-{colorama.Fore.YELLOW}( ){colorama.Fore.LIGHTBLUE_EX}-/_{colorama.Fore.WHITE}||{colorama.Fore.LIGHTBLUE_EX}_\\
 .'. \_{colorama.Fore.YELLOW}(){colorama.Fore.LIGHTBLUE_EX}_/ {colorama.Fore.BLUE}WARLOCK
  |   | . \\
  |   | .  \\
 .'. ,\_____'.
"""

    def generate_password(self, length: int = 12) -> Optional[str]:
        """
        Generates a random password with the specified length
        
        Args:
            length: Desired password length
            
        Returns:
            str: Generated password or None if length is invalid
        """
        try:
            if length <= 0:
                raise ValueError("Password length must be positive")
                
            # Ensuring password has at least one of each type
            password = [
                random.choice(self.lower),
                random.choice(self.upper),
                random.choice(self.num),
                random.choice(self.symbols)
            ]
            
            # Completing the rest of the password
            remaining_length = length - len(password)
            if remaining_length > 0:
                password.extend(random.sample(self.all, remaining_length))
            
            # Shuffling the final password
            random.shuffle(password)
            return "".join(password)
            
        except ValueError as e:
            print(f"\n{colorama.Fore.RED}Error: {str(e)}{colorama.Fore.WHITE}")
            return None

    def generate_leet(self) -> Optional[tuple[str, str]]:
        """
        Generates a password in leet speak style
        
        Returns:
            tuple[str, str]: Tuple containing (original_word, leet_password) or None if error
        """
        try:
            word = self.r.get_random_word()
            if not word:
                raise ValueError("Could not generate a random word")
                
            leet_map = {
                'a': '4', 'e': '3', 'i': '1', 'o': '0'
            }
            
            # Convert word to leet, keeping first letter uppercase
            leetpass = word[0].upper()
            leetpass += ''.join(leet_map.get(c.lower(), c) for c in word[1:])
            
            # Add # at the beginning
            leetpass = f"#{leetpass}"
            
            return (word, leetpass)
            
        except Exception as e:
            print(f"\n{colorama.Fore.RED}Error generating leet password: {str(e)}{colorama.Fore.WHITE}")
            return None

    def print_password(self, password: str | tuple[str, str], is_leet: bool = False) -> None:
        """Prints the generated password with the banner"""
        if is_leet and isinstance(password, tuple):
            original_word, leet_pass = password
            print(f'{self.banner}')
            print(f'📝 Original Word: {colorama.Fore.GREEN}{original_word}{colorama.Fore.WHITE}')
            print(f'🔐 Leet Password: {colorama.Fore.YELLOW}{leet_pass}{colorama.Fore.WHITE}\n')
        else:
            print(f'{self.banner}🔐PASSWORD🧙 ==> {colorama.Fore.YELLOW}{password}{colorama.Fore.WHITE}\n')

def main():
    parser = argparse.ArgumentParser(description='WARLOCK - Secure Password Generator')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('length', nargs='?', type=int, default=12,
                      help='Password length (default: 12)')
    group.add_argument('--leet', action='store_true',
                      help='Generate leet-style password (easier to memorize)')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    if args.leet:
        password = generator.generate_leet()
        if password:
            generator.print_password(password, is_leet=True)
    else:
        password = generator.generate_password(args.length)
        if password:
            generator.print_password(password)
            
    if not password:
        parser.print_help()

if __name__ == "__main__":
    main()
