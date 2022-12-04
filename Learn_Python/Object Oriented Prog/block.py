print('Object Oriented Programming.')
print()

class Block:
    """
    Description - Write a class Block that creates a block (Duh..)
    Requirements - The constructor should take an array as an argument,
    this will contain 3 integers of the form [width, length, height]
    from which the Block should be created.
    """
    def __init__(self, array):

        self.width = array[0]
        self.length = array[1]
        self.height = array[2]

    def get_width(self):

        # This function returns the block's width.
        return self.width

    def get_length(self):

        # This function returns the block's length.
        return self.length

    def get_height(self):

        # This function returns the block's height.
        return self.height

    def get_volume(self):

        # This function returns the block's volume.
        return self.width * self.length * self.height

    def get_surface_area(self):

        # This function returns the block's surface area.
        return (self.width * self.height + self.height * self.length
                + self.width * self.length) * 2

b = Block([2, 4, 6])
print(f'The block b has {b.get_width()} of width, {b.get_length()} of length,'
      f' {b.get_height()} of height,\n'
      f'{b.get_volume()} of volume and {b.get_surface_area()} or surface area.')
# Outputs - The block b has 2 of width, 4 of length, 6 of height,
# 48 of volume and 88 or surface area.
