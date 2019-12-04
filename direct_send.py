#!/usr/bin/env python
import pika
import sys
import csv

f = open('userdata2.csv')
csv_f = csv.reader(f)




connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_leads', exchange_type='direct')

for row in csv_f:
  registration_dttm = str(row[0])
  id = str(row[1])
  first_name = str(row[2])
  last_name = str(row[3])
  email = str(row[4])
  gender = str(row[5])
  ip_address = str(row[6])
  cc = str(row[7])
  country = str(row[8])
  birthdate = str(row[9])
  salary = str(row[10])
  title = str(row[11])
  comments = str(row[12])

  if country == 'United States':
    lead_type = 'leads'

  if country != 'United States' and cc != '':
  	lead_type = 'high_priority'

  if country != 'United States' and cc == '':
  	lead_type = 'other'





  message = registration_dttm + ',' + id + ',' + first_name + ',' + last_name + ',' + email + ',' + gender + ',' + ip_address + ',' + cc + ',' + country + ',' + birthdate + ',' + salary + ',' + title + ',' + comments

  channel.basic_publish(
      exchange='direct_leads', routing_key=lead_type, body=message)
  
  print(" [x] Sent %r:%r" % (lead_type, message))


connection.close()