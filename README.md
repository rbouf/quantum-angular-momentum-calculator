# Quantum Angular Momentum Calculator

A Python tool for computing Wigner 3-j and 6-j symbols used in quantum mechanics, atomic physics, and nuclear physics.

## 🎯 Physical Significance

### Wigner 3-j Symbol
The Wigner 3-j symbol represents the probability amplitude for coupling three angular momenta in quantum systems. It's directly related to Clebsch-Gordan coefficients and appears in:
- Matrix elements of spherical tensor operators
- Atomic transition selection rules
- Angular momentum addition in quantum mechanics

### Wigner 6-j Symbol  
The Wigner 6-j symbol describes transformations between different coupling schemes of three angular momenta, essential for:
- Recoupling coefficients in nuclear physics
- Transformation between LS and jj coupling schemes
- Shell model calculations

## ✨ Features

- **3-j Symbol Calculation**: Compute coupling coefficients for three angular momenta
- **6-j Symbol Calculation**: Calculate recoupling transformations
- **Fraction Support**: Handle half-integer quantum numbers (1/2, 3/2, etc.)
- **Interactive CLI**: User-friendly command-line interface
- **High Precision**: Accurate computation using SymPy's robust algorithms

## 🚀 Quick Start

```bash
# Install dependencies
pip install sympy numpy

# Run the calculator
python wigner_calculator.py
