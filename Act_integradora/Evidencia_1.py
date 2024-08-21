import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Clase que representa el almacén
class Warehouse:
    def __init__(self, width, height, num_objects, num_robots):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.robots = []
        self.initialize_objects(num_objects)
        self.initialize_robots(num_robots)

    # Inicialización de los objetos en posiciones aleatorias
    def initialize_objects(self, num_objects):
        self.objects = []
        for _ in range(num_objects):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if not self.grid[y][x]:
                    self.grid[y][x] = {'type': 'object', 'stack': 1}
                    self.objects.append((x, y))
                    break

    # Inicialización de los robots en posiciones aleatorias
    def initialize_robots(self, num_robots):
        for i in range(num_robots):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if not self.grid[y][x]:
                    robot = Robot(i, x, y, self)
                    self.robots.append(robot)
                    self.grid[y][x] = {'type': 'robot', 'robot': robot}
                    break

# Clase que representa un robot
class Robot:
    def __init__(self, id, x, y, warehouse):
        self.id = id
        self.x = x
        self.y = y
        self.warehouse = warehouse
        self.carrying = False
        self.moves = 0

    # Mover el robot en una dirección específica
    def move(self, direction):
        dx, dy = 0, 0
        if direction == 'up':
            dy = -1
        elif direction == 'down':
            dy = 1
        elif direction == 'left':
            dx = -1
        elif direction == 'right':
            dx = 1

        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < self.warehouse.width and 0 <= new_y < self.warehouse.height:
            if not self.warehouse.grid[new_y][new_x]:
                # Mover robot
                self.warehouse.grid[self.y][self.x] = None
                self.x = new_x
                self.y = new_y
                self.warehouse.grid[self.y][self.x] = {'type': 'robot', 'robot': self}
                self.moves += 1

    # Recoger un objeto si está en la celda actual
    def pick_object(self):
        if not self.carrying and self.warehouse.grid[self.y][self.x] and self.warehouse.grid[self.y][self.x]['type'] == 'object':
            self.carrying = True
            if self.warehouse.grid[self.y][self.x]['stack'] == 1:
                self.warehouse.grid[self.y][self.x] = None
            else:
                self.warehouse.grid[self.y][self.x]['stack'] -= 1

    # Soltar un objeto si está cargando uno
    def drop_object(self):
        if self.carrying:
            if self.warehouse.grid[self.y][self.x]:
                cell = self.warehouse.grid[self.y][self.x]
                if cell['type'] == 'object' and cell['stack'] < 5:
                    cell['stack'] += 1
                    self.carrying = False
            else:
                self.warehouse.grid[self.y][self.x] = {'type': 'object', 'stack': 1}
                self.carrying = False

# Clase que controla la simulación
class Simulation:
    def __init__(self, warehouse, max_steps):
        self.warehouse = warehouse
        self.max_steps = max_steps
        self.steps = 0

    # Ejecutar la simulación
    def run(self):
        while self.steps < self.max_steps:
            for robot in self.warehouse.robots:
                action = self.decide_action(robot)
                if action == 'move':
                    direction = random.choice(['up', 'down', 'left', 'right'])
                    robot.move(direction)
                elif action == 'pick':
                    robot.pick_object()
                elif action == 'drop':
                    robot.drop_object()
            self.steps += 1
            if self.check_completion():
                print(f"Completed in {self.steps} steps!")
                return

    # Decidir la acción del robot
    def decide_action(self, robot):
        if robot.carrying:
            return 'drop'
        else:
            return 'pick'

    # Verificar si la simulación ha terminado
    def check_completion(self):
        all_stacked = all([cell and cell['type'] == 'object' and cell['stack'] == 5
                           for row in self.warehouse.grid for cell in row])
        return all_stacked

# Clase que maneja la visualización de la simulación
class Visualization:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.fig, self.ax = plt.subplots()
        self.im = None

    # Dibujar el estado actual del almacén
    def draw(self):
        self.ax.clear()
        for y in range(self.warehouse.height):
            for x in range(self.warehouse.width):
                cell = self.warehouse.grid[y][x]
                if cell:
                    if cell['type'] == 'object':
                        color = 'red'
                        self.ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=True, color=color, alpha=0.5))
                        self.ax.text(x + 0.5, y + 0.5, str(cell['stack']), color='black', ha='center', va='center')
                    elif cell['type'] == 'robot':
                        color = 'blue'
                        self.ax.add_patch(patches.Circle((x + 0.5, y + 0.5), 0.3, color=color))
        self.ax.set_xlim(0, self.warehouse.width)
        self.ax.set_ylim(0, self.warehouse.height)
        self.ax.set_aspect('equal')

    # Ejecutar la visualización
    def animate(self, i):
        self.draw()
        simulation.run()

# Configuración de la simulación
warehouse = Warehouse(width=10, height=10, num_objects=20, num_robots=5)
simulation = Simulation(warehouse, max_steps=1000)

# Visualización de la simulación
visualization = Visualization(warehouse)
ani = animation.FuncAnimation(visualization.fig, visualization.animate, frames=100, interval=200)
plt.show()
