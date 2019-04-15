int moisture = 0;
int pin = A2;

void setup() {
    //serial for debugging
    Serial.begin(9600); //9600 baud rate
    Serial.println("DHT11 test!");
    
    pinMode(pin, INPUT);
}

void loop() {
    //publish every 30 seconds
    delay(500);
    
    //data
    moisture = analogRead(pin);
    
    //send data moisture to webhook event "Data"
    Particle.publish("Data", String(moisture), PRIVATE);
    
    //also output to serial for debugging
    Serial.print("Moisture: ");
    Serial.println(moisture);
}
