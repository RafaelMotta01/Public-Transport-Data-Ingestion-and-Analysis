#Criar external table com o location apontando para o pasta que o flume esta salvando os arquivos
#Creating External Table with location, pointing to the Flume folder where the files are being stored.

create external table sptrans (
hora string, 
linha string, 
origem string, 
destino string,
x string,
y string)
row format delimited fields terminated by ';'
LOCATION '/project/sptrans';