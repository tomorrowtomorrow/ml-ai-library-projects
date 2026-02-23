## Disease calculator using baye theorm and etc...

**Bayes Disease Probability Simulator**

---

## Overview

This project simulates disease testing in a population to illustrate **Bayes’ Theorem** in action.

* It calculates **theoretical** probability of being sick given a positive test: (P(Disease | Positive))
* It simulates a population and **computes an empirical probability** to compare with theory
* The project demonstrates the role of **prevalence, sensitivity, and specificity** in real-world diagnostics

---

## Features

* Input parameters:

  * Population size
  * Disease prevalence
  * Test sensitivity
  * Test specificity
* Simulates each individual’s disease status and test result
* Calculates:

  * Theoretical probability using Bayes’ formula
  * Empirical probability from simulation
* Handles edge cases (like no positive tests) safely

---

## Key Concepts Illustrated

* **Sensitivity:** Probability test is positive given disease
* **Specificity:** Probability test is negative given no disease
* **Prevalence:** Proportion of the population that is diseased
* **False positives / False negatives**
* **Bayes’ Theorem:** Updating probability based on test results

---

## Installation

No external packages are needed — only Python standard library (`random`).

```bash
# Clone repository (optional)
git clone https://github.com/sahandkhodayi/bayes-disease-simulator.git
cd bayes-disease-simulator

# Run the script
python simulate_bayes.py
```

---

## Usage Example

```python
from simulate_bayes import simulate_bayes

# Parameters
population = 10000
prevalence = 0.01       # 1% disease prevalence
sensitivity = 0.95      # 95% chance test catches sick people
specificity = 0.90      # 90% chance test correctly clears healthy people

# Run simulation
theory, empirical = simulate_bayes(population, prevalence, sensitivity, specificity)

print(f"Theoretical P(Disease|Positive): {theory:.4f}")
print(f"Empirical P(Disease|Positive): {empirical:.4f}")
```

---

## How it Works

1. **Simulate Population**

   * For each person, randomly assign disease status based on prevalence
2. **Simulate Test**

   * Sick → test positive with probability = sensitivity
   * Healthy → test positive with probability = 1 − specificity
3. **Count Results**

   * Track total positives and true positives
4. **Compute Probabilities**

   * Empirical: true positives / total positives
   * Theoretical: Bayes formula

---

## Example Output

```
Theoretical P(Disease|Positive): 0.0867
Empirical P(Disease|Positive): 0.0872
```

* With large populations, empirical results approximate theory
* Shows how low prevalence can lead to many false positives even with a good test

---

## Notes

* Can easily extend:

  * Multiple diseases
  * Interactive user input
  * Visualization of results
  * Sensitivity-specificity tradeoff analysis
* Great practice for **probability, conditional probability, and Bayes theorem**
* Foundational for ML concepts like **Naive Bayes classifier**

---

## Author

* sahdn khodayi / GitHub handle
* Learning AI/ML from scratch
---