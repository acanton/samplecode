//Arduino Server Code
//Alex Canton
//Provided template by arduino libraries

#include <Ethernet.h> //load the Ethernet Library
#include <EthernetUdp.h> //oad the Udp Library
#include <SPI.h> //load the SPI Library

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xFE, 0xEE}; //assign the mac address
IPAddress ip(10, 1, 15, 247); //assign the IP address of the arduino 
unsigned int localPort = 5000; //port assignment for server communication
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
String dataReq; //string used to store data
int packetSize; //size of the packet
EthenetUDP Udp; /defining the Udp object

void setup() {

Serial.begin(9600); //switch on the serial port
Ethernet.begin(mac, ip); //initialize the ethernet connection
Udp.begin(localPort); //Udp initialization
delay(1500);
}

void loop() {
   packetSize = Udp.parsePacket(); //Read theh packetSize
  
  if(packetSize>0){ //Check to see if a request is present
  
  Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE); //Reading the data request on the Udp
  String dataReq(packetBuffer); //Convert packetBuffer array to string datReq
  
  if (dataReq =="Red") { //See if Red was requested
  
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());  //Initialize Packet send
    Udp.print("Prompted for Red"); //Send string back to client
    Udp.endPacket(); //Packet has been sent
  }
   if (dataReq =="Green") { //See if Green was requested
  
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());  //Initialize Packet send
    Udp.print("Prompted Green"); //Send string back to client
    Udp.endPacket(); //Packet has been sent
   }
    if (dataReq =="Blue") { //See if Red was requested
  
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());  //Initialize Packet send
    Udp.print("Prompted for Blue"); //Send string back to client
    Udp.endPacket(); //Packet has been sent
    }
  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);
}

