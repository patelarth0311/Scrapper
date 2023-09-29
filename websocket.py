import asyncio
import websockets
from confluent_kafka import Consumer, KafkaError
consumer_config = {
   'bootstrap.servers': 'localhost:9092',
    'group.id': 'nba-group',
    'auto.offset.reset': 'earliest'  # You can choose 'earliest' or 'latest' based on your needs
}
consumer = Consumer(consumer_config)
consumer.subscribe(['nba'])

async def fetch_kafka_data(websocket):

    running = True

    while running:
        msg = consumer.poll(1.0)  # Adjust the timeout as needed
        
    
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition')
                running = False
            else:
                print('Error: {}'.format(msg.error()))
        else:
            message_value = msg.value()
            print('Received message: {}'.format(message_value))
            await websocket.send(message_value.decode('utf-8'))
            
        # Process the message as needed
    consumer.close()


async def kafka_data_sender(websocket):
        # Fetch Kafka data and process it (replace this with your Kafka consumer logic)
        await fetch_kafka_data(websocket)  # Implement this function
    



async def main():
    async with websockets.serve(kafka_data_sender, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())