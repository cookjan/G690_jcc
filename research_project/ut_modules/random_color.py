#random color generator from https://www.askpython.com/python/examples/generate-random-colors
import random
 
        def random_color_generator():
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                return (r, g, b)
 
        random_color = random_color_generator()