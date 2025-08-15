
"""
Complex Number Operations & Visualization
----------------------------------------
This script:
  • Accepts two complex numbers from the user (e.g., 2+3j, -1-4j).
  • Computes addition, subtraction, multiplication, and division.
  • Draws separate complex-plane diagrams for each operation.
"""

import argparse
import cmath
import math
import sys
import matplotlib.pyplot as plt

def arrow(ax, z, label):
    ax.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1)
    ax.text(z.real, z.imag, f" {label}")

def setup_axes(ax, title):
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title(title)

def autoscale(ax, points, margin=0.2):
    xs = [p.real for p in points] + [0]
    ys = [p.imag for p in points] + [0]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    dx = xmax - xmin or 1.0
    dy = ymax - ymin or 1.0
    pad_x = dx * margin
    pad_y = dy * margin
    ax.set_xlim(xmin - pad_x, xmax + pad_x)
    ax.set_ylim(ymin - pad_y, ymax + pad_y)

def plot_addition(z1, z2, result):
    fig, ax = plt.subplots()
    setup_axes(ax, 'Addition: z1 + z2')
    arrow(ax, z1, 'z1')
    arrow(ax, z2, 'z2')
    ax.quiver(z1.real, z1.imag, z2.real, z2.imag, angles='xy', scale_units='xy', scale=1, alpha=0.6)
    arrow(ax, result, 'z1+z2')
    autoscale(ax, [z1, z2, result])
    plt.show()

def plot_subtraction(z1, z2, result):
    fig, ax = plt.subplots()
    setup_axes(ax, 'Subtraction: z1 - z2 (add -z2)')
    arrow(ax, z1, 'z1')
    arrow(ax, z2, 'z2')
    minus_z2 = -z2
    arrow(ax, minus_z2, '-z2')
    ax.quiver(z1.real, z1.imag, minus_z2.real, minus_z2.imag, angles='xy', scale_units='xy', scale=1, alpha=0.6)
    arrow(ax, result, 'z1 - z2')
    autoscale(ax, [z1, z2, minus_z2, result])
    plt.show()

def plot_multiplication(z1, z2, result):
    fig, ax = plt.subplots()
    setup_axes(ax, 'Multiplication: z1 * z2')
    arrow(ax, z1, 'z1')
    arrow(ax, z2, 'z2')
    arrow(ax, result, 'z1*z2')
    r2 = abs(z2)
    theta2 = cmath.phase(z2)
    ax.text(0.02, 0.98, f'|z2| = {r2:.3g}\narg(z2) = {math.degrees(theta2):.1f}°', transform=ax.transAxes,
            va='top', ha='left', bbox=dict(boxstyle='round', alpha=0.1))
    autoscale(ax, [z1, z2, result])
    plt.show()

def plot_division(z1, z2, result):
    fig, ax = plt.subplots()
    setup_axes(ax, 'Division: z1 / z2')
    arrow(ax, z1, 'z1')
    arrow(ax, z2, 'z2')
    if result is None:
        ax.text(0.5, 0.5, 'Division undefined (z2 = 0)', transform=ax.transAxes, ha='center')
    else:
        arrow(ax, result, 'z1/z2')
        r2 = abs(z2)
        theta2 = cmath.phase(z2)
        ax.text(0.02, 0.98, f'1/|z2| = {1/r2:.3g}\n-arg(z2) = {-math.degrees(theta2):.1f}°',
                transform=ax.transAxes, va='top', ha='left', bbox=dict(boxstyle='round', alpha=0.1))
    autoscale(ax, [z1, z2] + ([] if result is None else [result]))
    plt.show()

def compute(z1, z2):
    add_ = z1 + z2
    sub_ = z1 - z2
    mul_ = z1 * z2
    div_ = None if z2 == 0 else z1 / z2
    return add_, sub_, mul_, div_

def parse_complex(prompt):
    s = input(prompt).strip()
    try:
        return complex(s)
    except Exception:
        print("Invalid complex number. Example: 2+3j")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true', help='Run demo with preset values')
    args = parser.parse_args()
    if args.demo:
        z1, z2 = complex(2, 3), complex(1, -2)
    else:
        z1 = parse_complex('Enter first complex number: ')
        z2 = parse_complex('Enter second complex number: ')
    add_, sub_, mul_, div_ = compute(z1, z2)
    print(f"Addition: {add_}")
    print(f"Subtraction: {sub_}")
    print(f"Multiplication: {mul_}")
    print("Division: " + ("undefined" if div_ is None else str(div_)))
    plot_addition(z1, z2, add_)
    plot_subtraction(z1, z2, sub_)
    plot_multiplication(z1, z2, mul_)
    plot_division(z1, z2, div_)

if __name__ == '__main__':
    main()
