class WireManager:
    def __init__(self, wire_paths=None):
        self.wire_paths = load_data() if wire_paths is None else wire_paths
        self.num_of_wires = len(self.wire_paths)
        self.line_segments = tuple([] for _ in range(self.num_of_wires))
        self.coords_of_intersection = []
        self.direction = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }

    def find_closest_intersection(self):
        corner_coords = tuple([] for _ in range(self.num_of_wires))

        def process_direction(dir_code):
            d, value = dir_code[0], int(dir_code[1:])
            return (x * value for x in self.direction[d])

        def calculate_manhattan_distance(x, y):
            return abs(x) + abs(y)

        # creating the coordinates of wire corners
        for i, wire in enumerate(self.wire_paths):
            corner_coords[i].append((0, 0))
            for dir_code in wire.split(','):
                x, y = process_direction(dir_code)
                next_x, next_y = corner_coords[i][-1]
                next_x += x
                next_y += y
                corner_coords[i].append((next_x, next_y))

        # creating line segments from corners
        for i in range(len(corner_coords)):
            LineSegment.id = 0
            for j in range(len(corner_coords[i]) - 1):
                self.line_segments[i].append(LineSegment(corner_coords[i][j], corner_coords[i][j + 1]))
            
        coords_of_intersection = []
        
        for line_1 in self.line_segments[0]:
            for line_2 in self.line_segments[1]:
                x, y = line_1.check_for_intersection(line_2)
                if (x, y) != (0, 0):
                    self.coords_of_intersection.append((x, y, line_1, line_2))

        # {intersection point : manhattan distance} pairs
        result = {p : calculate_manhattan_distance(*p[:2]) for p in self.coords_of_intersection}

        print(f'Distance to closest intersection: {min(result.values())}')


    def minimum_steps(self):
        def backtrack_wire(p, wire):
            if p == 0:
                return self.line_segments[wire][p].length
            else:
                return self.line_segments[wire][p].length + backtrack_wire(p - 1, wire)

        def partial_segment(p):
            x, y, wire_1, wire_2 = p
            prev_seg_1 = self.line_segments[0][wire_1.id - 1]
            prev_seg_2 = self.line_segments[1][wire_2.id - 1]
            part_sum_1 = abs(x - prev_seg_1.p2[0]) + abs(y - prev_seg_1.p2[1])
            part_sum_2 = abs(x - prev_seg_2.p2[0]) + abs(y - prev_seg_2.p2[1])
            return part_sum_1 + part_sum_2

        combined_steps = []

        for p in self.coords_of_intersection:
            x, y, wire_1, wire_2 = p
            line_index = wire_1.id
            steps_1 = backtrack_wire(line_index - 1, 0)
            line_index = wire_2.id
            steps_2 = backtrack_wire(line_index - 1, 1)
            remaining_sum = partial_segment(p)
            combined_steps.append(steps_1 + steps_2 + remaining_sum)

        print(f'Minimum steps: {min(combined_steps)}')



class LineSegment:
    id = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.length = self.get_segment_length()
        self.id = LineSegment.id
        LineSegment.id += 1

    def get_segment_length(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        return abs(y1 - y2) if x1 == x2 else abs(x1 - x2)

    def check_for_intersection(self, other):
        p1, p2 = self.p1, self.p2
        p3, p4 = other.p1, other.p2
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4

        # if denominator equals 0, the lines are parallel
        if (denominator := ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))) == 0:
            return 0, 0

        u_a = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
        u_b = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator

        if u_a >= 0 and u_a <= 1 and u_b >= 0 and u_b <= 1:
            x = x1 + (u_a * (x2 - x1))
            y = y1 + (u_a * (y2 - y1))
            return x, y

        return 0, 0


def load_data():
    with open('day_3/input.txt') as data:
        return data.readlines()


if __name__ == '__main__':
    wm = WireManager()
    wm.find_closest_intersection()
    wm.minimum_steps()