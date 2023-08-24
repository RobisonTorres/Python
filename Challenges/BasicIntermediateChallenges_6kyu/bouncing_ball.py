print('From Code Wars.')
print()

'''
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:

    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
'''

def bouncing_ball(h, bounce, window):

    # This function determines how many times the ball will pass in front of the window.
    if h > 0 and 0 < bounce < 1 and window < h:
        result = 1
        while h > window:
            h = h * bounce
            if h > window:
                result += 2
        return result
    return -1

print(bouncing_ball(30, 0.75, 1.5))  # Outputs - 21 times.
