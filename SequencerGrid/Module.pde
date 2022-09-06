class Module {
  int xOffset;
  int yOffset;
  float x, y;
  int unit;
  int xDirection = 1;
  int yDirection = 1;
  float speed; 
  int red;
  int blue;
  int green;
  // Contructor
  Module(int xOffsetTemp, int yOffsetTemp, int xTemp, int yTemp, float speedTemp, int tempUnit) {
    xOffset = xOffsetTemp;
    yOffset = yOffsetTemp;
    x = xTemp;
    y = yTemp;
    speed = speedTemp;
    unit = tempUnit;
  }
  
  // Custom method for updating the variables
  void colorit(int red, int green, int blue) {
    fill(red,green,blue);
    ellipse(yOffset + y, xOffset + x, 6, 6);
  }
  // Custom method for drawing the object
  void display() {
    fill(0,255,0);
    ellipse(yOffset + y, xOffset + x, 6, 6);
  }
}
