#!/usr/bin/env python
# coding: utf-8

# In[2]:


from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers = ['ip-172-31-81-238.ec2.internal:9092'], api_version =(0,10,1))
    for i in range(50):
        message = "message {}".format(str(datetime.now().time()))
        producer.send('log record',json.dumps(message).encode('utf-8'))
        sleep(2)
        print('Message sent', i)

