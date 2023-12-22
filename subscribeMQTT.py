
import paho.mqtt.client as mqtt

# Définir le broker
broker_address = "broker.hivemq.com"

# Définir le sujet (topic) auquel s'abonner
topic = "snir/bts/2023/msg"

# Fonction appelée lorsqu'un message est reçu
def on_message(client, userdata, msg):
    print(f"Message reçu sur le sujet {msg.topic}: {msg.payload.decode()}")

# Configurer le client MQTT
client = mqtt.Client()
client.on_message = on_message

# Se connecter au broker
client.connect(broker_address)
client.subscribe(topic)

# Boucle pour écouter les messages
client.loop_forever()
