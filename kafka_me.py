from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(conf)

