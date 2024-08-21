import random
import argparse
import moderngl
import numpy as np
from PIL import Image

# Genera los puntos para un rayo desde el centro de la imagen en una dirección dada
def generate_ray_points(center_x, center_y, length, angle):
    x2 = int(center_x + length * np.cos(angle))
    y2 = int(center_y + length * np.sin(angle))
    return center_x, center_y, x2, y2

# Dibuja una línea usando el algoritmo de Bresenham, que es simple y eficiente
def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

# Dibuja un patrón artístico complejo usando espirales y rayos
def draw_complex_pattern(ctx, prog, nLines, color_flag):
    fbo = ctx.simple_framebuffer((1024, 1024))  # Usamos un lienzo más grande para mejor resolución
    fbo.use()
    fbo.clear(0.0, 0.0, 0.0, 1.0)  # Fondo negro

    center_x, center_y = 512, 512  # El punto central desde donde dibujamos los rayos

    for i in range(nLines):
        # Decide el color de la línea
        color = (random.random(), random.random(), random.random()) if color_flag else (1.0, 1.0, 1.0)
        angle = random.uniform(0, 2 * np.pi)  # Ángulo aleatorio para la dirección del rayo
        length = random.uniform(100, 512)  # Longitud del rayo entre 100 y 512 píxeles
        x1, y1, x2, y2 = generate_ray_points(center_x, center_y, length, angle)
        
        points = bresenham_line(x1, y1, x2, y2)
        vertices = []
        
        for (x, y) in points:
            # Normalizamos las coordenadas para que estén en el rango [-1, 1], que es lo que OpenGL espera
            vertices.extend([x / 512 - 1, y / 512 - 1])
            vertices.extend(color)

        vertices = np.array(vertices, dtype='f4')

        # Creamos el buffer de vértices y lo dibujamos
        vbo = ctx.buffer(vertices.tobytes())
        vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')
        vao.render(moderngl.LINES)

    # Convertimos el framebuffer en una imagen y la mostramos
    Image.frombytes('RGB', fbo.size, fbo.read(), 'raw', 'RGB', 0, -1).show()

# Función principal para manejar los argumentos y ejecutar el dibujo
def main():
    parser = argparse.ArgumentParser(description="Genera arte con patrones complejos usando ModernGL")
    parser.add_argument('--nLines', type=int, required=True, help="Número de líneas a dibujar")
    parser.add_argument('--color', action='store_true', help="Dibujar líneas con colores aleatorios")
    args = parser.parse_args()

    ctx = moderngl.create_standalone_context()
    prog = ctx.program(
        vertex_shader='''
            #version 330

            in vec2 in_vert;
            in vec3 in_color;

            out vec3 v_color;

            void main() {
                v_color = in_color;
                gl_Position = vec4(in_vert, 0.0, 1.0);
            }
        ''',
        fragment_shader='''
            #version 330

            in vec3 v_color;

            out vec4 f_color;

            void main() {
                f_color = vec4(v_color, 1.0);
            }
        ''',
    )

    draw_complex_pattern(ctx, prog, args.nLines, args.color)

if __name__ == "__main__":
    main()
