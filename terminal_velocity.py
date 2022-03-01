from math import sqrt,tanh

# Formula solve F=1/2*c*Rho*A*v^2
# F= force, c= drag coefficient, rho = fluid density, v = velocity
# https://en.wikipedia.org/wiki/Free_fall#Uniform_gravitational_field_with_air_resistance

# def function to determine velocity at time t for at given C_d
def v(t, C_d=0.1):
	m   = 100 # mass [kg]
	g   = 9.82 # gravitational constant DK
	rho = 1.29 # fluid density
	A   = 20 # area

	v_inf = sqrt((2 * m * g)/(rho * C_d * A)) # terminal velocity
	vt = v_inf*tanh(g*t/v_inf) # velocity at time t

	return vt

# Function testing
print(v(t=2, C_d=0.01))
print(v(t=2))
