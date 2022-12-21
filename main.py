from random import randint
from typing import Set, Any
from fastapi import FastAPI
from kafka import TopicPartition

import uvicorn
import aiokafka
import asyncio
import json
import logging

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer


from config import settings
from logger import logger
from src.common.types import ProducerMessage, ProducerResponse


# instantiate the API
app = FastAPI()

# global variables
loop = asyncio.get_event_loop()
group_id = f"{settings.KAFKA_CONSUMER_GROUP_PREFIX}-{randint(0, 10000)}"
consumer_task = None
consumer = None
aioproducer = None


@app.on_event("startup")
async def startup_event():
    logger.info("Initializing API ...")
    await initialize()
    await consume()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down API")
    consumer_task.cancel()
    await aioproducer.stop()
    await consumer.stop()


@app.get("/")
async def root():
    return {"owner": "Victor Gomez", "email": "victor.g@datyra.com"}


@app.post("/producer/{topicname}")
async def kafka_produce(msg: ProducerMessage, topicname: str):

    await aioproducer.send(topicname, json.dumps(msg.dict()).encode("ascii"))
    response = ProducerResponse(name=msg.name, lastname=msg.lastname, topic=topicname)

    return response


async def initialize():
    loop = asyncio.get_event_loop()
    global consumer
    global aioproducer
    group_id = f"{settings.KAFKA_CONSUMER_GROUP_PREFIX}-{randint(0, 10000)}"

    logger.debug(
        f"Initializing KafkaConsumer for topic {settings.KAFKA_TOPIC}, group_id {group_id}"
        f" and using bootstrap servers {settings.KAFKA_BOOTSTRAP_SERVERS}"
    )

    consumer = aiokafka.AIOKafkaConsumer(
        settings.KAFKA_TOPIC,
        loop=loop,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=group_id,
    )

    # get cluster layout and join group KAFKA_CONSUMER_GROUP
    await consumer.start()

    logger.debug(
        f"Initializing KafkaProducer using bootstrap servers {settings.KAFKA_BOOTSTRAP_SERVERS}"
    )

    aioproducer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
    )
    # get cluster layout and initial topic/partition leadership information
    await aioproducer.start()


async def consume():
    global consumer_task
    consumer_task = asyncio.create_task(send_consumer_message(consumer))


async def send_consumer_message(consumer):
    try:
        # consume messages
        async for msg in consumer:
            # x = json.loads(msg.value)
            logger.info(f"Consumed msg: {msg}")

    finally:
        # will leave consumer group; perform autocommit if enabled
        logger.warning("Stopping consumer")
        await consumer.stop()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
