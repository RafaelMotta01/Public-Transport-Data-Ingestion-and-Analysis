#Analyses with Spark

sudo cp /usr/lib/hive/conf/hive-site.xml /usr/lib/spark/conf/

from pyspark.sql import HiveContext
from pyspark import SparkContext
import pyspark.sql.functions as F
from pyspark.sql.functions import count, col 

h = HiveContext(sc)
df = h.sql("select * From project.sptrans")

dfMax = df.groupBy("linha").agg(F.max(df.x).alias('maxX'))

dfMin = df.groupBy("linha").agg(F.min(df.x).alias('minX'))

dfJoin = dfMax.join(dfMin,(dfMax.linha == dfMin.linha)).select(dfMax.linha,dfMax.maxX, dfMin.minX)

dfJoin.where(dfJoin.maxX == dfJoin.minX).show()

dfJoin.select((dfJoin.maxX + dfJoin.minX),dfJoin.linha).show()