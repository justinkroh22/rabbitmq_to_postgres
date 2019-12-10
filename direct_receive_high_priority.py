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
    #print(f'{string_body}')
    stripped_message = string_body[2:]

    stripped_message2 = stripped_message[:-1]

    #print(stripped_message2)

    test_list = stripped_message2.split(',')
    
    #print(test_list)

    try:
        dbconnection = psycopg2.connect(user = "postgres",
                                  password = "password",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "leadsdb")

        cursor = dbconnection.cursor()

        postgres_insert_query = """ INSERT INTO high_priority (registration_dttm, id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title, comments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (test_list[0], test_list[1], test_list[2], test_list[3], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10], test_list[11], test_list[12])
        cursor.execute(postgres_insert_query, record_to_insert)

        dbconnection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into high_priority table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into high_priority table", error)


    finally:
    #closing database connection.
        if(dbconnection):
            cursor.close()
            dbconnection.close()
            print("PostgreSQL connection is closed")



channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()



