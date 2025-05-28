# WARLOCK

![WARLOCK Banner](https://i.imgur.com/hRkCY2x.png)

A secure and flexible password generator written in Python.

## Features

- Generate strong random passwords with customizable length
- Create memorable leet-style passwords
- Colorful terminal interface
- Multiple character types (lowercase, uppercase, numbers, symbols)
- Easy to use command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/warlock.git

# Navigate to the project directory
cd warlock

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Generate a default password (12 characters)
python warlock.py

# Generate a password with specific length
python warlock.py 16

# Generate a leet-style password
python warlock.py --leet

# Show help
python warlock.py -h
```

## Password Types

### Random Password
- Contains at least one of each:
  - Lowercase letter
  - Uppercase letter
  - Number
  - Special symbol
- Fully customizable length
- Randomly shuffled

### Leet Password
- Based on random English words
- First letter capitalized
- Common letter substitutions (a→4, e→3, i→1, o→0)
- Starts with # symbol
- Format: #Word (e.g., #P4ssw0rd)

## Requirements

- Python 3.6+
- colorama
- random-word

## License

MIT License

## Author

Br3noAraujo 
