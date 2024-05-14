## Nifi To KAFKA

sptrans.sources = source1
sptrans.channels = channel1 
sptrans.sinks = sink1 

sptrans.sources.source1.type = org.apache.flume.source.kafka.KafkaSource
sptrans.sources.source1.channels = channel1
sptrans.sources.source1.batchSize = 5000
sptrans.sources.source1.batchDurationMillis = 2000
sptrans.sources.source1.kafka.bootstrap.servers = localhost:9092
sptrans.sources.source1.kafka.topics = sptrans
sptrans.sources.source1.kafka.consumer.group.id = nifi

sptrans.channels.channel1.type = memory
sptrans.channels.channel1.capacity = 100000
sptrans.channels.channel1.transactionCapacity = 100000

#Data Sink to Hdfs
sptrans.sinks.sink1.channel = channel1
sptrans.sinks.sink1.type=hdfs
sptrans.sinks.sink1.hdfs.path=/aula/sptrans
sptrans.sinks.sink1.hdfs.fileType=DataStream
sptrans.sinks.sink1.hdfs.writeformat=Text
sptrans.sinks.sink1.hdfs.batchSize=1000
sptrans.sinks.sink1.hdfs.rollSize=0
sptrans.sinks.sink1.hdfs.rollCount=100
sptrans.sinks.sink1.hdfs.rollInterval=1000
sptrans.sinks.sink1.hdfs.useLocalTimeStamp=true