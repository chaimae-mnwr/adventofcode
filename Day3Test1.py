class Day03:
    """Day 03 task processor"""

    def __init__(self, in_arr):
        self.in_arr = in_arr
        self.line_len = len(in_arr[0])
        self.nb_lines = len(in_arr)

    def get_task1(self, slope_x, slope_y):
        encountered_trees = 0
        position = 0
        index = 0
        while index < self.nb_lines:
            line = self.in_arr[index]
        #for line in self.in_arr[index]:
            if line[position % self.line_len] == "#":
                encountered_trees += 1
            position += slope_x
            index += slope_y

        return encountered_trees

    def get_task2(self, slopes):
        encountered_trees = 1
        for slope in slopes:
            slope_x, slope_y = slope
            encountered_trees *= self.get_task1(slope_x, slope_y)

        return encountered_trees


def main():
    """ Run the daily tasks """
    with open("/home/menouar/Documents/dir5/puzzle3.txt", "r") as in_file:
        in_arr = [line.strip() for line in in_file.readlines()]

    day03 = Day03(in_arr)
    sol_a = day03.get_task1(3, 1)
    print(f"Task 1: {sol_a}")
    sol_b = day03.get_task2([[1, 1], [3,1], [5, 1], [7, 1], [1, 2]])
    print(f"Task 2: {sol_b}")
    return sol_a, sol_b

if __name__ == "__main__":
    sol_a, sol_b = main()
