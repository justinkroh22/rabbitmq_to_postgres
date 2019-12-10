S3 to RabbitMQ to Postgres:

How to use:

Launch the three direct_recieve python files in your shell by doing the following in seperate terminals.

python direct_receive_leads.py leads
python direct_receive_high_priority.py high_priority
python direct_receive_other.py other

Then in another terminal run the following:

python direct_send.py


This will then insert messages into the postgres database tables or txt file which is in csv format.



The recievers will be actively listening for messages on the channel, to send more just run

python direct_send.py again

