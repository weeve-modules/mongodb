"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""
from pymongo import MongoClient
from os import getenv
from logging import getLogger

log = getLogger("module")

# connect to MongoDB
client = MongoClient(getenv('MONGO_URI'))
collection = client[str(getenv('DATABASE_NAME'))][str(getenv('COLLECTION_NAME'))]

def module_main(received_data: any) -> str:
    """
    Send data to MongoDB.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        if type(received_data) == list:
            # MongoDB accepts only single JSON data
            for data in received_data:
                collection.insert_one(data)
        else:
            collection.insert_one(received_data)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
