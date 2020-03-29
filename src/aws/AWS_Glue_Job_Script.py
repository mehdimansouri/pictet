import sys
from awsglue.transforms import Join
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

engagement      = glueContext.create_dynamic_frame.from_catalog(database = "db_nbateamscase", table_name = "engagement", transformation_ctx = "engagement")
cost            = glueContext.create_dynamic_frame.from_catalog(database = "db_nbateamscase", table_name = "cost", transformation_ctx = "cost")
profitability   = glueContext.create_dynamic_frame.from_catalog(database = "db_nbateamscase", table_name = "profitability", transformation_ctx = "profitability")
winning         = glueContext.create_dynamic_frame.from_catalog(database = "db_nbateamscase", table_name = "winning", transformation_ctx = "winning")

final_df = Join.apply(engagement,Join.apply(cost, Join.apply(profitability,winning, keys1=['team'], keys2=['team']), keys1=['team'], keys2=['team']), keys1=['team'], keys2=['team'])

datasink4 = glueContext.write_dynamic_frame.from_options(frame = final_df, connection_type = "s3", connection_options = {"path": "s3://nbateamscasestudy-processeds3bucket-175ai4ptchxnd"}, format = "parquet", transformation_ctx = "datasink4")
