import snowflake.connector
import os
import snowflake.connector
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

con = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    authenticator="EXTERNALBROWSER"
)

df = con.cursor().execute("select top 10 * from lake.simple.clinician_daily").fetch_pandas_all()

print(df)
