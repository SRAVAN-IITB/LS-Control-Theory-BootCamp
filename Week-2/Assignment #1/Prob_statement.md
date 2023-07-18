# Ball on a Plate

The filed python files contain starter environments in which you have to add your own code.

Your task is to add a PID controller to control the movement of the plate and make the ball reach the point set as input.

## Get Started

### Installing Python, PyCharm and Pygame

In case you do not have python, and a text editor installed then, we would recommend that you check out [this video](https://www.youtube.com/watch?v=8GF6O6vNXCc) so that you have a nice setup to work with for the rest of the week!

### Downloading and Running the code

Download the repo as a zip file and expand it in a convenient location.

Now open a terminal inside the directory week 2 within the expanded folder. Then type the following commands to run the code.

```bash
python main.py
```

## Resources

### PID Tuning

Refer to the last few sections of the notebook ([click here](https://colab.research.google.com/drive/1YqDG6qfuc8hW5uAKQIMwAJzptkQQ5gjZ?usp=sharing)) material for this topic, especially the python code at the end.

### PID refresher

You can go through this [PID Playlist](https://youtube.com/playlist?list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y) for a quick refresher on what PID control is and how it is used.
You don't need to watch the whole playlist, this is just to refresh a few key concepts that will be used.

### Python and pygame resources(optional)

- [pygame documentation](https://www.pygame.org/docs/) - Very useful for finding useful functions, specially [this - pygame.math.Vector2](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2)
- [Pygame tutorial](https://youtu.be/FfWpgLFMI7w) - do only what is required
- [Python tutorial](https://youtu.be/_uQrJ0TkZlc) - Feel free to skip sections since we have already covered the same concepts in CS101

## Problem Statement
We have plate resting on a pivot. Either sides of the plate are attached to actuators that can change
the angle of the plate within realistic speeds. The user is going to input a point on the plate with a
mouse click. Your task is to code a controller which can make the ball reach that point. The system
follows the ordinary differential equation:\

$$\ddot{x}=-\frac{5g}{7}\theta$$

**_Happy Coding!!_**

## Procedure

1. Find out all the variables you need to solve the PID equation and the ODE.
Make sure you keep track of the integral and error terms as they may be used across time periods.
2. Choose an appropriately small dt value. 
3. Set up constants of the PID controller in Control.py
4. Write down the equations with the help of the code given in the week 1 colab link. Make sure to use the _odeint()_ function to solve the ODE.
5. Feel free to use as many parameters across the _solve()_ function for both input and output.
6. Make sure to set up saturation limits for _theta_, _dtheta_ and _x_. Preferable the limits should be 15 degrees, 1 degree and 300 px for the three variables.
7. Tune the PID controller to make the process as ideal as possible.
8. Try to make your code run multiple PID loops in the same window one after the other. That is, if one set point value is reached another one can be input in the same window.
9. A good project submission would show that a certain set point is reached. This can be defined as the ball being in acceptable and small enough range of the set point and the velocity of the ball being close enough to 0.


## Attribution

<div>Icons made by <a href="https://www.flaticon.com/m" title="Flaticon">Flaticon</a> from <a href="https://www.pinterest.com/" title="Pinterest">Pinterest</a></div>
