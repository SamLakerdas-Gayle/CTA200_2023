import numpy as np

def iterate_complex(max_itr):
    x_lin = np.linspace(-2,2,500)
    y_lin = np.linspace(-2,2,500)
    x, y = np.meshgrid(x_lin,y_lin)

    # Complex plane
    comp_pln = x + y*1j
    # True if values diverge and false if values don't
    div = np.full_like(x, False, dtype=bool)
    # Iteration number at divergence.
    itr = np.full_like(x, -1)
    # Current value of z for each point
    z = np.zeros_like(x)

    # Iterate the z values
    for i in range(max_itr):
        z[div] = 0
        z=z**2+comp_pln
        div[abs(z) > 2] = True
        # This line ensures that the iteration value is only updated when z diverges.
        itr[(itr < 0) & div] = i+1
    return div, itr