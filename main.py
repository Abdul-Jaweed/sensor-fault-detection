from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == 'main':
    mongodb_client = MongoDBClient()
    print("collection name:",mongodb_client.database.list_collection_names())