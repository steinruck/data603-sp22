#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, MapType, DoubleType, TimestampType
from pyspark.sql.functions import from_json, col

# for visualization purposes
get_ipython().system('pip install plotly kaleido')
import plotly.express as px
import plotly.graph_objs as go

# create spark session
spark = SparkSession.builder.appName('ISS').getOrCreate()

# read stream for ISS location
stream = (spark.readStream
                      .format('socket')
                      .option('host', 'localhost')
                      .option('port', 22223)
                      .load()
          )

# define JSON schema
schema = (StructType([
                    StructField('iss_position', MapType(StringType(), StringType(), False), False),
                    StructField('timestamp', TimestampType(), False),
                    StructField('message', StringType(), False)
                    ])
            )

# parse JSON object - split location into lat and long
stream_parsed = (stream
       .select(from_json(col('value'), schema).alias('data'))
       .select('data.*')
       .withColumn('latitude', col('iss_position').getItem('latitude'))
       .withColumn('longitude', col('iss_position').getItem('longitude'))
      )

# create single table using only timestamp and lat/long sub columns
stream_parsed.createOrReplaceTempView('iss')
df = spark.sql('select timestamp, latitude, longitude from iss')

# send each batch to json file
writer = (df
          .writeStream
          .outputMode('append')
          .format('json')
          .option("checkpointLocation", "checkpoint/")
          .option("path", "output/")
          .trigger(processingTime='10 seconds')
          .start()
          .awaitTermination(timeout=3600)
         )

# merge all JSON as CSV file
spark.read.json("output/*.json").coalesce(1).write.format("csv").option('header', 'True').save("iss_stream")

# for some reason it deletes the schema so redo
schema = (StructType([
                    StructField('latitude', DoubleType(), False),
                    StructField('longitude', DoubleType(), False),
                    StructField('timestamp', TimestampType(), False),
                    ])
            )

# create dataframe using schema from saved csv - could use in memory but I wanted a hard copy
df = spark.read.option("header", True).schema(schema).csv("iss_stream/*.csv")

# convert to pandas
pdf = df.toPandas()

# create plot over world map using plotly express
# won't render in Docker so just output as .png instead
fig = px.scatter_geo(pdf,lat='latitude',lon='longitude', hover_name="timestamp", projection="fahey")
fig.update_layout(title = 'ISS Location for 1 Hour', title_x=0.5, height=1000, width=1000)
(fig.update_geos(coastlinecolor='olive', 
                 framecolor="grey", 
                 framewidth=3, 
                 lakecolor="blue", 
                 showcountries=True, 
                 showocean=True, 
                 oceancolor="skyblue", 
                 showrivers=True, 
                 rivercolor="royalblue", 
                 showland=True, 
                 landcolor="ivory", 
                 lonaxis = dict(
                                showgrid = True,
                                gridcolor = 'rgb(102, 102, 102)',
                                gridwidth = 0.5
                                 ),
                lataxis = dict(
                                showgrid = True,
                                gridcolor = 'rgb(102, 102, 102)',
                                gridwidth = 0.5)))

fig.write_image("iss_60min.png")
fig.write_html("iss_60min.html")

