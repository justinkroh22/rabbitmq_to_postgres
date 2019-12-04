#!/usr/bin/env python
import pika
import sys
import psycopg2



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_leads', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

all_lead_types = sys.argv[1:]
if not all_lead_types:
    sys.stderr.write("Usage: %s [leads] [high_priority] [other]\n" % sys.argv[0])
    sys.exit(1)

for lead_type in all_lead_types:
    channel.queue_bind(
        exchange='direct_leads', queue=queue_name, routing_key=lead_type)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):

    string_body = str(body)

    stripped_message = string_body[2:]

    stripped_message2 = stripped_message[:-1]

    #print(stripped_message2)


    f = open("otherleads.txt", "a")
    f.write(stripped_message2)
    f.close()


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()