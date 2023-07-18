import numpy as np
from scipy.integrate import odeint

g = 9.8

# The following function gives the ordinary differential
# equation that our plant follows. Do not meddle with this.
def f(x, t, theta):
    return (x[1], (-5 * g / 7) * np.radians(theta))

def solve(theta):

    # Define the initial conditions
    x0 = 0.0
    v0 = 0.0
    initial_state = [x0, v0]

    # Define the time points for integration
    t = np.linspace(0, 1, 100)  # Adjust the time range and step size as needed

    # Call odeint to solve the ODE
    solution = odeint(f, initial_state, t, args=(theta,))

    # Extract the change in x from the solution
    dx = solution[-1, 0] - x0

    return dx
