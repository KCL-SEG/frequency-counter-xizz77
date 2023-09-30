"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if str(item) in frequencies.keys():
            frequencies[str(item)] = frequencies[str(item)] + 1
        else:
            frequencies[str(item)] = 1
            
    return frequencies
