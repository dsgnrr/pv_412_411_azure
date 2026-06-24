import os
from dotenv import load_dotenv
from uuid import uuid4

from azure.cosmos import CosmosClient, PartitionKey, exceptions
import random

address = [
    {"country":"Ukraine", "city":'Odesa', "street":'prospekt Shevchenko, 71'},
    {"country":"Ukraine", "city":'Kyiv', "street":'Franka, 34/3'},
    {"country":"Ukraine", "city":'Mykolaiv', "street":'prospekt Nebesnoi Sotni , 34'},
    {"country":"Ukraine", "city":'Lviv', "street":'Shevchenko, 24'},
    {"country":"Ukraine", "city":'Vinnytsya', "street":'Zaliznychna, 55'},
]

order_status = ['paid','delivered','pending']

class Order:
    id:str
    userId: str
    product: str
    price: float
    status: str
    
    def __init__(self, product, price, status, **kwargs):
        self.id = str(uuid4())
        self.userId = f"user_{random.randint(100000, 999999)}"
        self.product = product
        self.price = price
        self.status = status
        
        for k,v in kwargs.items():
            setattr(self, k, v)


def generate_orders(items_count=5):
    orders = []
    for i in range(items_count):
        orders.append(
            Order(f'product-{random.randint(100,999)}',
                  random.randint(1, 100000),
                  status=order_status[random.randint(0, len(order_status)-1)],
                  **address[random.randint(0, len(address)-1)]
                  ).__dict__
        )
        
    return orders


load_dotenv()

ENDPOINT = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")

client = CosmosClient(ENDPOINT, COSMOS_KEY)

database_name = 'OurDB2'
try:
    database = client.create_database_if_not_exists(id=database_name)
except exceptions.CosmosHttpResponseError as e:
    print("Error execution:", e)

container_name = 'Orders'

partition_key = PartitionKey("/userId")

try:
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=partition_key,
        offer_throughput=1000
    )
except exceptions.CosmosHttpResponseError as e:
    print("Error execution:", e)
    
# # INSERT DATA
# try:
#     orders = generate_orders(10)
#     for item in orders:
#         container.upsert_item(body=item)
    
# except exceptions.CosmosHttpResponseError as e:
#     print("Error execution:", e)

# READ DATA
try:
    response = container.read_all_items()
    for idx, item in enumerate(response, 1):
        print(f"DATA[{idx}]:",item, '\n')
except exceptions.CosmosHttpResponseError as e:
    print("Error execution:", e)

target_id = '7144969e-bdb5-40d4-8dd6-ed7b0eaca7dd'
target_part_key = 'user_945488'

try:
    response = container.read_item(item=target_id, partition_key=target_part_key)
    print("Get unique:", response)
except exceptions.CosmosHttpResponseError as e:
    print("Error execution:", e)
    
query = "SELECT * FROM c WHERE c.userId = @userId"
params = [{"name":"@userId", "value":"user_482263"}]

items = container.query_items(query=query, parameters=params, enable_cross_partition_query=False)

for item in items:
    print("Get by query:", item)
    


