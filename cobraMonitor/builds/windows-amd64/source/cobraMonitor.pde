import processing.serial.*;

PFont f;         // Declare PFont variable
PImage img;      // Declare Image variable

Serial myPort;   // Create object from Serial class
String val;      // Data received from the serial port
String[] parsed_values; // Array to store parsed values

int firstRow;
int rowGap;
int firstColumn;
int columnGap;

int lf = 10;

void setup() {
  f = createFont("Noto Serif", 16, true); // Create Font
  img = loadImage("cobra-logo-white.png"); //Load image
  size(1000, 800);
  
  rectMode(CENTER);

  String[] portList = Serial.list();
  if (portList.length > 0) {
    String portName = portList[0];
    myPort = new Serial(this, portName, 115200);
  }
}

void draw() {
  background(50, 50, 50);             // Set background to white
  textFont(f, 30);                  // Specify font to be used

  if (myPort != null && myPort.available() > 0) {               // If data is available,
    val = myPort.readStringUntil(lf); // read String and store it in val
    parsed_values = loadData(val);
    //delay(150); //If something is wrong, try setting up a delay
    //time, gps, accele_x, accele_y, accele_z, gyro_x, gyro_y, gyro_z, module_temp, temperature, pressure, humidity
  } else {
    parsed_values = new String[12];
    for (int i = 0; i < 12; i++) {
      parsed_values[i] = "0";
    }
    background(50,50,50);
    textFont(f, 35);  
    fill(255,0,0);
    textAlign(CENTER);
    text("Check connection to arduino.", width/2,height/2);
  }
  
  
  //LOGO
  fill(255, 255, 255);   // Specify font color
  textAlign(LEFT);
  text("Cobra Monitor 0.1", 60, 40);   // Display Text
  image(img, 0, 0, img.width/6, img.height/6);

  //TIME
  textAlign(RIGHT);
  text(time_is(), width - 20, 40);

  // GPS
  textAlign(LEFT);
  text("GPS coord: " + parsed_values[1], 40, 90);

  //TEMPERATURE
  textAlign(LEFT);
  firstRow = 90;
  rowGap = 40;
  text("Temperature: " + parsed_values[9] + "ºC", width - 370, firstRow);
  text("Pressure: "+ parsed_values[10] + "kPa", width - 370, firstRow+rowGap);
  text("Humidity: "+ parsed_values[11], width - 370, firstRow+rowGap*2);
  textFont(f, 20);
  text("M. temperature: "+ parsed_values[8] + "ºC", width - 370, firstRow+rowGap*3);

  //GYROSCOPE
  textAlign(LEFT);
  textFont(f, 30);
  firstRow = 170;
  rowGap = 20;
  firstColumn = 50;
  columnGap = 150;
  
  // TESTING VALUES
  parsed_values[5] = "45";
  parsed_values[6] = "45";
  parsed_values[7] = "45";
  
  text("X axis: "+parsed_values[5], firstColumn, firstRow);
  text("Y axis: "+parsed_values[6], firstColumn+columnGap, firstRow);
  text("Z axis: "+parsed_values[7], firstColumn+columnGap*2, firstRow);
  
  float x_axis = radians(float(parsed_values[5]));
  float y_axis = radians(float(parsed_values[6]));
  float z_axis = radians(float(parsed_values[7]));
  
  translate(firstColumn+60, firstRow+60);
  rotate(x_axis);
  rect(0, 0, 20, 60);
  
  rotate(-x_axis); // resetting rotate angle so other too blocks are in the same row
  translate(150, 0);
  rotate(y_axis);
  rect(0, 0, 20, 60);

  rotate(-y_axis);
  translate(150, 0);
  rotate(z_axis);
  circle(0, 0, 50);

  //ACCELEROMETER
  firstRow = 210;
  columnGap = 100;
  //text("Accelero:", 140, 170);
  //text("X axis: "+parsed_values[2], firstColumn + columnGap, firstRow);
  //text("Y axis: "+parsed_values[3], firstColumn + columnGap, firstRow+rowGap);
  //text("Z axis: "+parsed_values[4], firstColumn + columnGap, firstRow+rowGap*2);
}

String time_is() {
  // ADD FEATURE TO ADD 0 BEFORE NUMBERS SMALLER THAN 10
  String d = nf(day(), 2);
  String month = nf(month(), 2);
  String y = str(year());

  String s = nf(second(), 2);  // Values from 0 - 59
  String m = nf(minute(), 2);  // Values from 0 - 59
  String h = nf(hour(), 2);    // Values from 0 - 23

  String time = d + "/" + month + "/" + y + "    " + h + ":" + m + ":" + s;
  return time;
}

String[] loadData(String values) {
  if (values != null && values.split(",").length == 12) {
    String[] parsed_val = values.split(",");
    return parsed_val;
  } else {
    String[] parsed_val = new String[12];
    for (int i = 0; i < 12; i++) {
      parsed_val[i] = "0";
    }
    return parsed_val;
  }
}
