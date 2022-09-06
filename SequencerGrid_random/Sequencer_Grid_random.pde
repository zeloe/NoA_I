/**
 * Array Objects. 
 * 
 * Demonstrates the syntax for creating an array of custom objects. 
 */
import oscP5.*;
import netP5.*;
int unit = 50;
int count;
int redamount = 0;
int greenamount = 0;
int blueamount = 255;
int index = 0;
Module[] mods;
OscP5 oscP5;
PImage img;
String path = "black.png";
void setup() {
  size(500, 500);
  noStroke();
  int wideCount = width / unit;
  int highCount = height / unit;
  count = wideCount * highCount;
  oscP5 = new OscP5(this,8001);
  mods = new Module[count];
  int index = 0;
  for (int y = 0; y < highCount; y++) {
    for (int x = 0; x < wideCount; x++) {
      mods[index++] = new Module(x*unit, y*unit, unit/2, unit/2, random(0.05, 0.8), unit);
      img = loadImage(path);
    }
  }
}

void oscEvent(OscMessage theOscMessage){
  
  if(theOscMessage.checkAddrPattern("/path") == true)
  {
    path = theOscMessage.get(0).stringValue();
    img = loadImage(path);
  }
  if(theOscMessage.checkAddrPattern("/red") == true)
  {
    redamount = theOscMessage.get(0).intValue();
    index    = theOscMessage.get(1).intValue();
    greenamount = 0;
    blueamount = 0;
    img = loadImage(path);
  }
  if(theOscMessage.checkAddrPattern("/reset") == true)
  {
    redamount = 0;
    greenamount = 0;
    blueamount = 255;
    img = loadImage("black.png");
  }
}
void draw() {
  background(0);
  clear();
    image(img, 0, 0);
   for (Module mod : mods) {
    mod.display();
   }
    mods[index].colorit(redamount,blueamount,greenamount);
    
}
