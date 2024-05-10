import json
<<<<<<< HEAD
from kafka import KafkaConsumer # type: ignore
=======
<<<<<<< HEAD
from kafka import KafkaConsumer # type: ignore
=======

from kafka import KafkaConsumer


>>>>>>> 4e1b3a02e38843ddb007754d6e5bfad7e768a1c6
>>>>>>> 7f2b63ad653ad7ce92b9efa68309b58d5a9ce1df
from .config import KAFKA_BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    'order_topic',
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
<<<<<<< HEAD
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
=======
<<<<<<< HEAD
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
=======
    value_deserializer=lambda v: json.loads(v).decode('utf-8')
)
>>>>>>> 4e1b3a02e38843ddb007754d6e5bfad7e768a1c6
>>>>>>> 7f2b63ad653ad7ce92b9efa68309b58d5a9ce1df
