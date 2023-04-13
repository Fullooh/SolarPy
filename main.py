import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Global Variables
planet_index = 0

G = 6.6743e-11  # Gravitational constant

# Masses of the planets
masses = np.array([5.9736e24, 3.285e23, 4.867e24, 6.39e23, 1.898e27, 5.683e23, 1.024e26])

def diff_equation(time, year, x0, y0, z0, vx0, vy0, vz0): 
    global planet_index
    res_nu = G * masses[planet_index]

    #Using newtons law to calculate the differential equations
    res_de = np.linalg.norm(year[0:3] - year[3:6])**3
    res = res_nu * (year[0:3] - year[3:6]) / res_de

    return np.concatenate((year[6:], res, res))

def planet_positions(time, year):
    # Define initial positions and velocities of the planets in the solar system AS OF MAR 27 2023
    # These values are obtained from NASA JPL Horizons database
            #Earth                   #Mercury               #Venus                  #Mars                   #Jupiter                #Saturn                 #Uranus             #Neptune
    x0 = [-1.498226235729210E+08, 3.052257456324214E+07, -1.330021660009238E+07, -1.513434351485086E+08, 6.947391319707890E+08, 1.251866707341551E+09, 1.961389286280390E+09, 4.454293272212478E+09]

    y0 = [-1.503580923124005E+07, 3.456894206024369E+07, 1.068202700844620E+08, 1.948936753757561E+08, 2.529997810530325E+08, -7.640101209446666E+08, 2.189619063131434E+09, -4.002477530644583E+08]

    z0 = [3.324549480270687E+04, -5.726974053762667E+04, 2.190211684669994E+06, 7.798201734118089E+06, -1.659284005223630E+07, -3.655848396303177E+07, -1.727787864315689E+07, -9.441119096068434E+07]

    vx0 = [2.511611611529636E+00, -4.550982057359742E+01, -3.491972064068707E+01, -1.828562586901633E+01, -4.618548138888609E+00, 4.491284929932218E+00, -5.122758501853182E+00, 4.504691155921977E-01]

    vy0 = [-2.977221101505069E+01, 3.498096897842066E+01, -4.098870492121980E+00, -1.272665158468572E+01, 1.289235803454705E+01, 8.227861841784886E+00, 4.226602151072220E+00, 5.445690801647118E+00]

    vz0 = [6.753248526170097E-04, 7.034611062366697E+00, 1.959130417760081E+00, 1.822527202873925E-01, 4.986538865547541E-02, -3.224172128450702E-01, 8.221306170775344E-02, -1.225341114632514E-01]

    #Number of planets
    n = len(masses)

    # Define time range in seconds (1 Earth years)
    t_span = np.linspace(0, 1*365*24*60*60, num = 10)

    #Calling the initial positions and velocities on the planets
    init_y0 = x0 + y0 + z0 + vx0 + vy0 + vz0

    print(t_span, y0)

    # Solve differential equations for the time range
    sol = solve_ivp(diff_equation, [t_span[0], t_span[-1]], y0= init_y0, t_eval=t_span, args = (x0, y0, z0, vx0, vy0, vz0,))  
  

    # Plot planet positions as a function of time
    fig, axs = plt.subplots(8, 1, figsize=(8, 10), sharex=True)

    #Convert the axs list to a numpy array
    axs = np.array(axs)

    #Plotting in into the matplotlib graph
    for i, ax in enumerate(axs.flat):
        ax.plot(sol.t / (365*24*60*60), sol.y[i], label='Planet {}'.format(i+1))
        ax.set_ylabel('Position')
        ax.legend()

    axs[-1].set_xlabel('Time (years)')
    plt.show()
planet_positions(1,1)



