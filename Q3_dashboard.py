
import sympy as sp

# Question 3: Polynomial Calculus

# Define the variable and function
t = sp.Symbol("t")
f = t**3 - 6*t**2 + 9*t + 2

print("QUESTION 3: POLYNOMIAL CALCULUS")
print("=" * 45)

# Display the function
print("\nGiven function:")
sp.pprint(sp.Eq(sp.Function("f")(t), f))

# (a) Factorisation
print("\n(a) Factorisation:")
print(sp.factor(f))

# (b) Solve f(t) = 0
print("\n(b) Solutions of f(t) = 0:")
roots = sp.solve(sp.Eq(f, 0), t)
for root in roots:
    sp.pprint(root)

print("\nNumerical roots:")
print(sp.nroots(f))

# Solve f(t) = 2
print("\nSolutions of f(t) = 2:")
solutions = sp.solve(sp.Eq(f, 2), t)
for solution in solutions:
    sp.pprint(solution)

# (c) First derivative
first_derivative = sp.diff(f, t)
print("\n(c) First derivative f'(t):")
sp.pprint(first_derivative)

# Second derivative
second_derivative = sp.diff(f, t, 2)
print("\nSecond derivative f''(t):")
sp.pprint(second_derivative)

# (d) Indefinite integral
indefinite_integral = sp.integrate(f, t)
print("\n(d) Indefinite integral:")
sp.pprint(indefinite_integral)
print("Remember to add the constant of integration C.")

# (e) Definite integral from 0 to 2
definite_integral = sp.integrate(f, (t, 0, 2))
print("\n(e) Definite integral from 0 to 2:")
sp.pprint(definite_integral)

print("=" * 45)
