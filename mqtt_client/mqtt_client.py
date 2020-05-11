import paho.mqtt.client as mqtt

#JSON notation
sensorValues= """[{"id":"sensor1","time":1589068267000,"v1":10,"v2":11},{"id":"sensor2","time":1589068267000,"v1":12,"v2":13}]"""

broker_address="localhost" 
client = mqtt.Client("sensor_client")
client.connect(broker_address,port=1883)
client.publish("sensor",sensorValues)