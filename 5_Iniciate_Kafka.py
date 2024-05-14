## Start KAFKA

cd kafka_2.11-0.11.0.1

nohup bin/kafka-server-start.sh config/server.properties &

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sptrans

bin/kafka-topics.sh --list --zookeeper localhost:2181

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sptrans 