import pygame
import numpy as np
import Control as c

# initialising the window. You can ignore this part.

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 40)

# setting plate parameters

centerX = 400
centerY = 400
plateT = 60

r = 0.1 # the radius of the ball

# loading in images and transforming them to required sixes and angles. You can ignore this part.

plate = pygame.image.load("plate.png")
plate = pygame.transform.rotate(plate, -45)
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (40, 40))
pivot = pygame.image.load("plain-triangle.png")

# game control variable. This variable determines if the came continues to run. You can ignore this part.

run = True


# A function used to rotate an image about its center. You can ignore this part.
def blit_rot_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)

# Initialize game parameters
theta = 0   # Angle of the plate with the horizontal (measured positive counterclockwise)
phi = 0     # Angle of rotation of the ball about its own axis
x = 0       # Distance of the center of the ball from the pivot
X, Y = 400, 400 # Initialize X and Y variables

# PID controller constants
Kp = 0.1   # Proportional gain
Ki = 0.01   # Integral gain
Kd = 0.05   # Derivative gain

# PID controller variables
int = 0
prev_error = 0

# Function to calculate PID control output
def ctrl_Output(error, dt):         #   Calculated and controlled output
    global int, prev_error

    # Proportional term
    P = Kp * error

    # Integral term
    int += error * dt
    I = Ki * int

    # Derivative term
    der = (error - prev_error) / dt
    D = Kd * der

    # Calculate control output
    control_output = P + I + D

    # Update previous error
    prev_error = error

    return control_output

# Game loop
while run:

    # checking for mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                X, Y = event.pos  # gets the x and y coordinates of the mouse left click
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                X, Y = event.pos  # gets the x and y coordinates of the mouse left click and moving.

    # Calculate error (difference between current ball position and setpoint)
    error = x - X + 400

    # Calculate control output using PID controller
    dt = 0.01  # Time step
    control_output = ctrl_Output(error, dt)

    # Update plate angle
    dtheta = control_output

    # Constants for the angular velocity saturation
    max_dtheta = 1  # degree per time step
    # Apply saturation limits
    if abs(dtheta) > max_dtheta:
        dtheta = np.sign(dtheta) * max_dtheta
    theta += dtheta

    # Update ball position
    dx = c.solve(theta)
    x += dx

    # make sure the ball rotates
    dphi = dx / r
    phi += dphi

    # setting the background colour of the screen
    screen.fill((235, 62, 74))

    # displaying the images on the screen within appropriate physical parameters,
    # for example, it is ensured that the ball is always on the plate.

    blit_rot_center(screen, plate, (centerX - 364, centerY - 364), theta)
    blit_rot_center(screen, ball, (centerX - 20 + x * np.cos(np.radians(theta)) - plateT * np.sin(np.radians(theta)),
                                   centerY - 20 - plateT * np.cos(np.radians(theta)) - x * np.sin(np.radians(theta))),
                    -phi)
    screen.blit(pivot, (centerX - 32, centerY - 32 + plateT))

    pygame.display.update()

#   -Sravan K Suresh {22B3936}

