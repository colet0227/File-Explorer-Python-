# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668
from pathlib import Path, os
from os import remove
from enum import Enum


def list_contents(dtry):
    """List the contents."""
    p = Path(dtry)
    try:
        sorted_p = sorted(p.iterdir(), key=os.path.isdir)
        for o in sorted_p:
            print(o)
    except:
        print("Can't be found")


def recursive(dtry):
    """List everything recursively."""
    p = Path(dtry)
    try:
        sorted_p = sorted(p.iterdir(), key=os.path.isdir)
        for o in sorted_p:
            print(o)
            if o.is_dir():
                recursive(o)
    except:
        print("Can't be found")


def files_only(dtry):
    """List only files."""
    p = Path(dtry)
    try:
        for obj in p.iterdir():
            if obj.is_file():
                print(obj)
    except:
        print("Can't be found")


def files_recursive(dtry):
    """List files recursively."""
    p = Path(dtry)
    try:
        sorted_p = sorted(p.iterdir(), key=os.path.isdir)
        for obj in sorted_p:
            if obj.is_file():
                print(obj)
            if obj.is_dir():
                recursive(obj)
    except:
        print("Can't be found")


def specific_file(dtry, nme):
    """Output only a specific file name."""
    p = Path(dtry)
    try:
        sorted_p = sorted(p.iterdir(), key=os.path.isdir)
        for obj in sorted_p:
            if nme in str(obj):
                print(obj)
    except:
        print("Can't be found")


def specific_recursion(dtry, nme):
    """Outputs a name recursively."""
    p = Path(dtry)
    try:
        sorted_p = sorted(p.iterdir(), key=os.path.isdir)
        for obj in sorted_p:
            if nme in str(obj):
                print(obj)
            if obj.is_dir():
                specific_recursion(obj, nme)
    except:
        print("Can't be found")
        text = input()
        p = Path(text[2:])


def create_file(dtry, name):
    """Create a file."""
    p = Path(dtry)
    p = p / name

    if not p.exists():
        p.touch()
    
    print(p)


def delete_file(file):
    """Delete a file."""
    p = Path(file)
    while not p.is_file():
        print('ERROR')
        file = input()
        p = Path(file[2:])
    while '.dsu' not in file:
        print('ERROR')
        file = input()
        p = Path(file[2:])
    name = str(p)
    remove(p)
    print(name + ' DELETED')


def read_contents(file):
    """Read the contents of a file."""
    empty = True
    p = Path(file)

    while empty == True:
        while not p.is_file():
            print('Not a valid file')
            file = input('Select a different file')
            p = Path(file[2:])
        while '.dsu' not in file:
            print('ERROR')
            file = input()
            p = Path(file[2:])
        
        f = p.open()
        contents = f.readlines()
        if len(contents) == 0:
            print('EMPTY')
            file = input()
            p = Path(file[2:])
        else:
            for line in contents:
                print(line, end='')
            empty = False
        f.close()


def listing(contents):
    """List the contents based on the letter"""
    if ' -r' in contents[1]:
        if ' -f' in contents[1]:
            files_recursive(contents[0][2:])
        elif ' -s' in contents[1]:
            specific_recursion(contents[0][2:], extra)
        elif ' -e' in contents[1]:
            specific_recursion(contents[0][2:], extra)
        else:
            recursive(contents[0][2:])
    
    elif ' -f' in contents[1]:
        files_only(contents[0][2:])
    
    elif ' -s' in contents[1]:
        specific_file(contents[0][2:], extra)
    
    elif ' -e' in contents[1]:
        specific_file(contents[0][2:], extra)
    
    else:
        list_contents(contents[0][2:])


def split(text):
    """Split the text into a list"""
    extra = ''
    if text.find(' -r') >= 0:
        contents = text.split(' -r')

        if text.find(' -s') >= 0:
            extra = contents[1][4:]
        
        if text.find(' -e') >= 0:
            extra = '.' + contents[1][4:]
        
        contents[1] += ' -r'
    
    elif text.find(' -f') >= 0:
        contents = text.split(' -f')
        contents[1] += ' -f'
    
    elif text.find(' -s') >= 0:
        contents = text.split(' -s')
        extra = contents[1][1:]
        contents[1] += ' -s'
    
    elif text.find(' -e') >= 0:
        contents = text.split(' -e')
        extra = '.' + contents[1][1:]
        contents[1] += ' -e'
    
    else:
        contents = [text]
        contents.append(text)
    
    return contents, extra


if __name__ == "__main__":
    # [COMMAND] [INPUT] [[-]OPTION] [INPUT]
    text = input()
    command = text[:1]

    while text[:1] != 'Q':
        # Listing option
        if text[:1] == 'L':
            contents, extra = split(text)
            
            # Different options with the L command
            listing(contents)
        
        elif text[:1] == 'C':
            # Create a dsu file
            while ' -n' not in text:
                print('ERROR')
                text = input()
            contents = text.split(' -n')
            extra = contents[1][1:] + '.dsu'
            create_file(contents[0][2:], extra)
        
        elif text[:1] == 'D':
            # Delete a dsu file
            delete_file(text[2:])
        
        elif text[:1] == 'R':
            # Read the contents
            read_contents(text[2:])
        
        else:
            # Print if the input is not Q, L, C, D, or R
            print('Not a valid feature.')
        
        text = input()
    
    # Quit the program
    quit()

