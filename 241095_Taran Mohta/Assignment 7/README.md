
# Deutsch–Jozsa Algorithm - Implementation

This is the  implementation of the **Deutsch–Jozsa algorithm**. The Deutsch–Jozsa algorithm is one of the first examples showing an exponential separation between quantum and classical computing for a specific problem.

---

## Problem Statement

Given a Boolean function \( f: \{0,1\}^n \rightarrow \{0,1\} \), promised to be either:

- **Constant**: same output (0 or 1) for all inputs  
- **Balanced**: returns 0 for exactly half the inputs, and 1 for the other half

The task is to determine whether \( f \) is constant or balanced.

- **Classical computing**: May require up to \( 2^{n-1} + 1 \) evaluations  
- **Quantum computing (Deutsch–Jozsa)**: Requires only **1 query** to the oracle

---

## Circuit Overview

The Deutsch–Jozsa algorithm uses \( n+1 \) qubits:

- \( n \) qubits in the input register, initialized to \( |0\rangle^{\otimes n} \)
- 1 target qubit initialized to \( |1\rangle \)

The quantum circuit structure is as follows:



      ┌───┐              ┌───────┐      ┌────────────┐      ┌───────┐      ┌───┐
|0⟩───┤ H ├──────────────┤       ├──────┤    U_f      ├──────┤ H ⊗ n ├──────┤ M ├───
      └───┘              │       │      │             │      └───────┘      └─┬─┘
                         │       │      │             │                      │
      ┌───┐              │  n+1  │      │             │                      ▼
|0⟩───┤ H ├──────────────┤  qubit├──────┤   Oracle    ├────────────────────── M
      └───┘              │       │      │             │
                         │       │      │             │
      ┌───┐              │       │      └─────────────┘
|1⟩───┤ X ├───┤ H ├──────┘
      └───┘

---

## What the Algorithm Does

1. **Initialize** the qubits:  
   \( |0\rangle^{\otimes n} \otimes |1\rangle \)

2. **Apply Hadamard gates** to all qubits

3. **Apply oracle unitary** \( U_f \) such that:  
   \[
   U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle
   \]

4. **Apply Hadamard** again to the first \( n \) qubits

5. **Measure** the first \( n \) qubits

---

## Interpretation of Output

The measurement histogram from the simulator tells us the nature of the function:

- **Only `000...0` occurs**: The function is **constant**
- **Any other result**: The function is **balanced**



