function setup() {
  createCanvas(640, 480);
}

function myTranslate(x, y, tx, ty) {
  return [x + tx, y + ty];
}

function myRotation(x, y, angle) {
  angle = radians(angle);
  let newX = x * cos(angle) - y * sin(angle);
  let newY = x * sin(angle) + y * cos(angle);
  return [newX, newY];
}

function myRotationPiv(x, y, xr, yr, angle) {
  angle = radians(angle); 
  let newX = xr + (x - xr) * cos(angle) - (y - yr) * sin(angle);
  let newY = yr + (x - xr) * sin(angle) + (y - yr) * cos(angle);
  return [newX, newY];
}

function myScaling(x, y, sx, sy) {
  x = x * sx;
  y = y * sy;
  return [x, y];
}

function myScalingFxP(x, y, sx, sy, xfp, yfp) {
  x = x * sx + xfp * (1 - sx);
  y = y * sy + yfp * (1 - sy);
  return [x, y];
}

function myReflection(x, y, axis) {
  x = -x;
  y = -y;
  return [x, y];
}

function myShearX(x, y, shx) {
  return [x + shx * y, y];
}

function myShearY(x, y, shy) {
  return [x, y + shy * x];
}

function draw() {
  background(102);
  
  // Cambiar el origen al centro de la ventana
  translate(width / 2, height / 2);
  
  // Triángulo blanco en el centro rotado
  fill(255);
  polygon(0, 0, 50, 3, myRotation, 45);
  
  // Otras posibles transformaciones (descomentarlas para probarlas)
  // polygon(0, 0, 100, 5, myTranslate, 50, 50);
  // polygon(0, 0, 100, 4, myRotation, 45);
  // polygon(0, 0, 100, 4, myRotationPiv, 90, 100, 100);
  // polygon(-150, 0, 100, 4, myScaling, 1.5, 1.5);
  polygon(0, 0, 100, 4, myReflection);
  // polygon(0, 0, 100, 4, myShearX, 0.5);
  // polygon(0, 0, 100, 4, myShearY, 0.5);
  
  // Dibujar una cuadrícula de 4 cuadros
  stroke(255);
  line(-width / 2, 0, width / 2, 0);
  line(0, -height / 2, 0, height / 2);
}

function polygon(x, y, radius, npoints, transform, ...params) {
  let angle = TWO_PI / npoints;
  beginShape();
  for (let a = 0; a < TWO_PI; a += angle) {
    let sx = x + cos(a) * radius;
    let sy = y + sin(a) * radius;
    if (transform != null) {
      [sx, sy] = transform(sx, sy, ...params);
    }
    vertex(sx, sy);
  }
  endShape(CLOSE);
}
