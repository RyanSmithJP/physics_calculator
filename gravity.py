def calculate_gravity(entry_mass, entry_radius, precision, label_result):
    try:
        mass = float(entry_mass.get())
        radius = float(entry_radius.get())
        grav_constant = 6.674*(10**-11)
        result = (grav_constant*mass)/(radius**2)
        label_result.config(text=f'Acceleration due to gravity = {result:.{precision.get()}f} m/s^2')
    except ValueError:
        label_result.config(text='Please enter valid parameters')
