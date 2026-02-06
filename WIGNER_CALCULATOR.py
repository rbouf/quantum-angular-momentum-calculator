#!/usr/bin/env python3
"""
WIGNER SYMBOLS CALCULATOR
=========================
Quantum Angular Momentum Coefficients Computation

A Python tool for calculating Wigner 3-j and 6-j symbols used in quantum
mechanics, atomic physics, and nuclear physics for angular momentum coupling.
"""

from sympy.physics.wigner import wigner_3j, wigner_6j
from fractions import Fraction

def convert_fraction_to_numeric(value):
    """
    Convert Fraction to appropriate numeric type.
    
    Parameters:
    -----------
    value : Fraction
        Input fraction from user
        
    Returns:
    --------
    int or float
        Integer if denominator is 1, otherwise float
    """
    return int(value) if value.denominator == 1 else float(value)

def calculate_3j_symbol(j1, j2, j3, m1, m2, m3):
    """
    Calculate Wigner 3-j symbol.
    
    Parameters:
    -----------
    j1, j2, j3 : Fraction
        Angular momentum quantum numbers
    m1, m2, m3 : Fraction
        Magnetic quantum numbers
        
    Returns:
    --------
    float
        Value of the Wigner 3-j symbol
    """
    args = [convert_fraction_to_numeric(x) for x in [j1, j2, j3, m1, m2, m3]]
    return wigner_3j(*args)

def calculate_6j_symbol(j1, j2, j3, j4, j5, j6):
    """
    Calculate Wigner 6-j symbol.
    
    Parameters:
    -----------
    j1...j6 : Fraction
        Angular momentum quantum numbers
        
    Returns:
    --------
    float
        Value of the Wigner 6-j symbol
    """
    args = [convert_fraction_to_numeric(x) for x in [j1, j2, j3, j4, j5, j6]]
    return wigner_6j(*args)

def validate_selection(selection):
    """
    Validate user selection input.
    
    Parameters:
    -----------
    selection : str
        User input for symbol type
        
    Returns:
    --------
    bool
        True if selection is valid, False otherwise
    """
    return selection in ['3', '6']

def get_fraction_input(prompt):
    """
    Safely get fraction input from user.
    
    Parameters:
    -----------
    prompt : str
        Input prompt message
        
    Returns:
    --------
    Fraction
        User input converted to Fraction
    """
    while True:
        try:
            value = input(prompt)
            if '/' in value:
                num, den = value.split('/')
                return Fraction(int(num), int(den))
            else:
                return Fraction(int(value), 1)
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (e.g., 1/2) or integer.")

def main():
    """
    Main interactive program for calculating Wigner symbols.
    """
    print("="*60)
    print("WIGNER SYMBOLS CALCULATOR")
    print("="*60)
    print("Calculate quantum angular momentum coupling coefficients")
    print()
    
    # Get user selection
    while True:
        selection = input("Select symbol type (3-j or 6-j). Enter 3 or 6: ").strip()
        if validate_selection(selection):
            break
        print("Invalid selection. Please enter '3' for 3-j symbol or '6' for 6-j symbol.")
    
    # Calculate based on selection
    if selection == '3':
        print("\n" + "-"*40)
        print("WIGNER 3-j SYMBOL CALCULATION")
        print("-"*40)
        print("Enter angular momentum (j) and magnetic (m) quantum numbers")
        print()
        
        # Get input for 3-j symbol
        j1 = get_fraction_input("Enter j1: ")
        j2 = get_fraction_input("Enter j2: ")
        j3 = get_fraction_input("Enter j3: ")
        m1 = get_fraction_input("Enter m1: ")
        m2 = get_fraction_input("Enter m2: ")
        m3 = get_fraction_input("Enter m3: ")
        
        # Calculate and display result
        result = calculate_3j_symbol(j1, j2, j3, m1, m2, m3)
        print("\n" + "="*40)
        print("RESULT:")
        print(f"Wigner 3-j symbol {{ {j1} {j2} {j3} }}")
        print(f"                     {{ {m1} {m2} {m3} }}")
        print(f"Value: {result:.8f}")
        print("="*40)
        
    else:  # selection == '6'
        print("\n" + "-"*40)
        print("WIGNER 6-j SYMBOL CALCULATION")
        print("-"*40)
        print("Enter angular momentum quantum numbers")
        print()
        
        # Get input for 6-j symbol
        j1 = get_fraction_input("Enter j1: ")
        j2 = get_fraction_input("Enter j2: ")
        j3 = get_fraction_input("Enter j3: ")
        j4 = get_fraction_input("Enter j4: ")
        j5 = get_fraction_input("Enter j5: ")
        j6 = get_fraction_input("Enter j6: ")
        
        # Calculate and display result
        result = calculate_6j_symbol(j1, j2, j3, j4, j5, j6)
        print("\n" + "="*40)
        print("RESULT:")
        print(f"Wigner 6-j symbol {{ {j1} {j2} {j3} }}")
        print(f"                   {{ {j4} {j5} {j6} }}")
        print(f"Value: {result:.8f}")
        print("="*40)

if __name__ == "__main__":
    main()