class MazeSolver:
    def __init__(self, maze_path):
        file = open(maze_path, "r")
        maze_text = file.read()
        file.close()
        self.maze = maze_text.split("\n")
        self.maze_height = len(self.maze)
        self.maze_width = len(self.maze[0])

        self.visited = []
        for i in range(len(self.maze)):
            self.visited.append([False] * len(self.maze[0]))

        self.preprocess_maze()

    def get_neighbours(self, point):
        x, y = point
        neighbours = set()
        if x < self.maze_height - 1 and self.maze[x + 1][y] == ".":
            neighbours.add((x + 1, y))
        if x > 0 and self.maze[x - 1][y] == ".":
            neighbours.add((x - 1, y))

        if y < self.maze_width - 1 and self.maze[x][y + 1] == ".":
            neighbours.add((x, y + 1))
        if y > 0 and self.maze[x][y - 1] == ".":
            neighbours.add((x, y - 1))

        return neighbours

    def update_free_cells(self, curr_point):
        x, y = curr_point
        self.visited[x][y] = True
        to_visit = self.get_neighbours(curr_point)

        for point in to_visit:
            x_p, y_p = point
            if not self.visited[x_p][y_p]:
                self.update_free_cells(point)

    def preprocess_maze(self):
        starting_point = None
        for i in range(self.maze_width):
            if self.maze[0][i] == ".":
                starting_point = (0, i)
            if self.maze[-1][i] == ".":
                starting_point = (self.maze_height - 1, i)

        for i in range(self.maze_height):
            if self.maze[i][0] == ".":
                starting_point = (i, 0)
                break
            if self.maze[i][-1] == ".":
                starting_point = (i, self.maze_width - 1)
                break

        print(starting_point)
        self.update_free_cells(starting_point)

        for i in range(self.maze_height):
            print(self.visited[i])

    def is_free(self, point):
        x, y = point
        if self.visited[x][y]:
            return True

        return False
