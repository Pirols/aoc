from pathlib import Path


class Cuboid:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max, state):
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max
        self.state = state


    def get_volume(self):
        return (self.x_max - self.x_min + 1) * \
               (self.y_max - self.y_min + 1) * \
               (self.z_max - self.z_min + 1)


    def get_intersection(self, other):
        # compute intersection
        ## x
        if (self.x_max < other.x_min) or (self.x_min > other.x_max):
            return None
        res_x_min = max(self.x_min, other.x_min)
        res_x_max = min(self.x_max, other.x_max)
        ## y
        if (self.y_max < other.y_min) or (self.y_min > other.y_max):
            return None
        res_y_min = max(self.y_min, other.y_min)
        res_y_max = min(self.y_max, other.y_max)
        ## z
        if (self.z_max < other.z_min) or (self.z_min > other.z_max):
            return None
        res_z_min = max(self.z_min, other.z_min)
        res_z_max = min(self.z_max, other.z_max)

        # which state is the intersection
        if self.state == other.state:
            ## if the current cuboid is the same sign of an already existing theirs' intersections influence should be discarded
            state = -self.state
        elif self.state == 1:
            ## if the current cuboid is on and the other is off, than its intersection must be turned on to balance off
            state = 1
        else:
            ## viceversa the intersection with a previously present on-cuboid must be balanced
            state = -1

        return Cuboid(res_x_min, res_x_max, res_y_min, res_y_max, res_z_min, res_z_max, state)


if __name__ == "__main__":
    data_path = Path('22_data.txt')
    cuboids = list()

    with open(data_path, mode='r') as f:
        for line in f:
            state, zone = line.split()

            # should the cube be turned on or off
            state = 1 if state == 'on' else -1

            # define cube zones
            x, y, z = zone.split(',')
            x_min, x_max = [int(val) for val in x.split('=')[1].split('..')]
            y_min, y_max = [int(val) for val in y.split('=')[1].split('..')]
            z_min, z_max = [int(val) for val in z.split('=')[1].split('..')]

            # generate the new cuboid
            new_cuboid = Cuboid(x_min, x_max, y_min, y_max, z_min, z_max, state)

            # compute all intersections (even with other intersections)
            to_append = list()
            for cuboid in cuboids:
                intersection = new_cuboid.get_intersection(cuboid)
                if intersection is not None:
                    to_append.append(intersection)

            cuboids.extend(to_append)

            if state == 1:
                cuboids.append(new_cuboid)

    # part a and b
    tot_a = 0
    tot_b = 0

    for cuboid in cuboids:
        volume = cuboid.get_volume() * cuboid.state
        tot_b += volume
        # disregard cuboid outside the 100x100x100 cuboid around (0, 0, 0)
        if -50 <= cuboid.x_min <= cuboid.x_max <= 50 and \
           -50 <= cuboid.y_min <= cuboid.y_max <= 50 and \
           -50 <= cuboid.z_min <= cuboid.z_max <= 50:
            tot_a += volume

    print(f"Number of on cubes (100x100x100 cuboid): {tot_a}")
    print(f"Number of on cubes: {tot_b}")
