//D1:blue, D2:orange, D3:red
int leds[3]  = {D1, D2, D3};

int led(String data){
    //set all pins to LOW when called
    for(int i = 0; i < arraySize(leds); i++){
        digitalWrite(leds[i], LOW);
    }
    
    //set the corresponding led to HIGH
    if(data == "red")
        digitalWrite(leds[2], HIGH);
    else if(data == "orange")
        digitalWrite(leds[1], HIGH);
    else if(data == "blue")
        digitalWrite(leds[0], HIGH);
    else
        return 1;
    
    return 0;
}

void setup() {
    //recognise the led web function
    Particle.function("led", led);
    
    //set all pins to output
    for(int i = 0; i < arraySize(leds); i++){
        pinMode(leds[i], OUTPUT);
    }
}

void loop() {
    //none
}
