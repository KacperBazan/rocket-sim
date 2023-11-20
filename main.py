# Rocket properties
dry_mass = 80.28  # kg
wet_mass = 30.39  # kg
burn_time = 5.65  # s
mdot = wet_mass / burn_time  # kg/s

# Engine properties
chamber_k = 1.1926  # unitless
chamber_M = 0.023889  # kg/mol
chamber_R = 8.31446261815324 / chamber_M  # J/(kg*K)
chamber_temp = 3016.32  # K
chamber_pressure = 3447378.64  # Pa
throat_area = 0.00246362965667312  # m^2
exit_area = 0 # m^2 (initialized later)
exit_pressure = 0 # Pa (initialized later)

# Kinematic properties
height = 0  # m
velocity = 0  # m/s
acceleration = 0  # m/s^2
thrust = 0  # N (initialized later)
t = 0  # s

# Environment properties
sea_level = 620  # m (elevation of FAR launch site)
g = 9.80665 # m/s^2
dt = 0.01  # s


def ambient_pressure(height):
    # Calculate the ambient pressure (Pa) at a given height (https://en.wikipedia.org/wiki/Atmospheric_pressure)

    p0 = 101325  # Sea level standard atmospheric pressure, Pa
    T0 = 288.15  # Sea level standard temperature, K
    L = 0.00876  # Temperature lapse rate, K/m
    g = 9.80665  # Gravitational acceleration, m/s^2
    M = 0.02896968  # Molar mass of dry air, kg/mol
    R0 = 8.31446261815324  # Universal gas constant, J/(mol*K)

    return p0 * (1 - (L * height) / T0) ** ((g * M) / (R0 * L))


def exit_velocity(exit_pressure):
    # Calculate the exit velocity (m/s) given the exit pressure and engine properties

    k = chamber_k  # unitless
    R = chamber_R  # J/(kg*K)
    T = chamber_temp  # K
    p1 = chamber_pressure  # Pa

    return (
        (2 * k / (k - 1)) * R * T * (1 - (exit_pressure / p1) ** ((k - 1) / k)) ** 0.5
    )


def exit_area(exit_pressure):
    # Calculate the exit area (m^2) given the exit pressure and engine properties

    k = chamber_k  # unitless
    p1 = chamber_pressure  # Pa
    At = throat_area  # m^2

    return (
        ((k + 1) / 2) ** (1 / (k - 1))
        * (exit_pressure / p1) ** (1 / k)
        * (((k + 1) / (k - 1)) * (1 - (exit_pressure / p1) ** ((k - 1) / k))) ** 0.5
        * (1 / At)
    ) ** -1


def initialize_rocket():
    # Initialize the rocket properties

    







def simulate_rocket(
    dry_mass,
    wet_mass,
    burn_time,
    exhaust_velocity,
    exit_pressure,
    height,
    ambient_pressure,
    exit_area,
):
    # Calculate the initial mass of the rocket
    initial_mass = dry_mass + wet_mass

    # Initialize variables to track the rocket's state
    current_mass = initial_mass
    current_height = 0
    current_time = 0

    # Iterate over the burn time
    while current_time < burn_time:
        # Calculate the current thrust force
        current_thrust = (
            exhaust_velocity * exit_area * (exit_pressure - ambient_pressure)
        )

        # Calculate the current acceleration
        current_acceleration = current_thrust / current_mass

        # Update the current height and velocity using the equations of motion
        current_height += current_velocity * dt + 0.5 * current_acceleration * dt**2
        current_velocity += current_acceleration * dt

        # Update the current mass based on the propellant consumption rate
        propellant_consumption_rate = wet_mass / burn_time
        current_mass = initial_mass - propellant_consumption_rate * current_time

        # Update the current time
        current_time += dt

    # Calculate the apogee based on the final height
    apogee = current_height

    # Return the calculated apogee
    return apogee

    # Simulate the rocket and calculate the apogee based on the given exit pressure
    # Your simulation code goes here
    # Return the calculated apogee


def find_optimal_exit_pressure():
    # Define the range of exit pressures to test
    exit_pressure_range = [100, 200, 300, 400, 500]

    # Initialize variables to track the maximum apogee and the corresponding exit pressure
    max_apogee = 0
    optimal_exit_pressure = 0

    # Iterate over the exit pressure range
    for exit_pressure in exit_pressure_range:
        # Simulate the rocket for the current exit pressure
        apogee = simulate_rocket(exit_pressure)

        # Check if the current apogee is greater than the maximum apogee found so far
        if apogee > max_apogee:
            # Update the maximum apogee and the corresponding exit pressure
            max_apogee = apogee
            optimal_exit_pressure = exit_pressure

    # Return the optimal exit pressure
    return optimal_exit_pressure


# Run the solver
optimal_exit_pressure = find_optimal_exit_pressure()
print("Optimal Exit Pressure:", optimal_exit_pressure)
