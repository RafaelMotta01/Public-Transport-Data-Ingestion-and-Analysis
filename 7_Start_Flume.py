##Start Flume Agent

sptrans.conf

cd apache-flume-1.7.0-bin

conf/

vi sptrans.conf 

cd ..

bin/flume-ng agent --conf ./conf --conf-file ./conf/sptrans.conf --name sptrans -Dflume.root.logger=INFO,console