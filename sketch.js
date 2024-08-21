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
  
  function myScaling(x, y) {
    return [x, y];
  }
  
  function myScalingFxP(x, y) {
    return [x, y];
  }
  
  function myReflection(x, y) {
    return [x, y];
  }
  
  function myShearX(x, y) {
    return [x, y];
  }
  
  function myShearY(x, y) {
    return [x, y];
  }
  
  function draw() {
    background(102);
    fill(255);
    polygon(0, 0, 100, 4, null);
    fill(1);
    //polygon(0, 0, 100, 5, myTranslate, 50, 50);
    //polygon(0, 0, 100, 4, myRotation, 45);
    polygon(0, 0, 100, 4, myRotationPiv, 90, 100, 100);
  }
  
  function polygon(x, y, radius, npoints, transform, ...params) {
    let angle = TWO_PI / npoints;
    console.log(params);
    beginShape();
    for (let a = 0; a < TWO_PI; a += angle) {
      let sx = x + cos(a) * radius;
      let sy = y + sin(a) * radius;
      if (transform != null) {
        [sx, sy] = transform(sx, sy, ...params);
      }
      sx = sx + width / 2;
      sy = -sy + height / 2;
      vertex(sx, sy);
    }
    endShape(CLOSE);
  }