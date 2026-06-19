import os
from azure.data.tables import TableClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError

from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
TABLE_NAME='mytable'

table_client = TableClient.from_connection_string(CONNECTION_STRING, TABLE_NAME);

user_entity = {
    "PartitionKey":"Users",
    "RowKey":"user_id_234",
    "first_name":"Tom",
    "last_name":"due",
    "age":33
}

try:
    entity = table_client.upsert_entity(entity=user_entity)
except Exception as e:
    print("Error: ", e)