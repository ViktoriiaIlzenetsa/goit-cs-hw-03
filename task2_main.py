from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017/"

client = MongoClient(uri, server_api = ServerApi('1'))
db = client.cats

def read_all():
    count = 0
    result = db.cats.find({})
    for cat in result:
        print(cat)
        count += 1
    if count == 0:
        print("Database is empty")

def read_by_name():
    name = input("Enter name:")
    result = db.cats.find_one({"name": name})
    if result:
        print(result)
    else:
       print(f"Cat with name {name} not found") 


def create():
    name = input("Enter name:")
    age = input("Enter age:")
    features = input("Enter features separated by commas:")
    features_list = [el.strip() for el in features.split(",")]
    result = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features_list,
        }
    )
    print(f"Cat with name {name} saved with id {result.inserted_id}")

def update_age_by_name():
    name = input("Enter name:")
    result = db.cats.find_one({"name": name})
    if result:
        age = input("Enter new age:")
        db.cats.update_one({"name": name}, {"$set": {"age": age}})
        print(f"Age for {name} updated")
    else:
        print(f"Cat with name {name} not found")

def add_feature_by_name():
    name = input("Enter name:")
    result = db.cats.find_one({"name": name})
    if result:
        feature = input("Enter new feature:")
        db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
        print(f"Feature {feature} added")
    else:
        print(f"Cat with name {name} not found")

def delete_by_name():
    name = input("Enter name:")
    result = db.cats.find_one({"name": name})
    if result:
        db.cats.delete_one({"name": name})
        print(f"Record with name {name} deleted")
    else:
        print(f"Cat with name {name} not found")

def delete_all():
    db.cats.delete_many({})
    print(f"Deleted all records from the collection")

if __name__ == "__main__":
    print("""Welcome to the assistant bot!
    Available commands:
        ° help
        ° create
        ° read_all
        ° read_one    # read one by name
        ° update_age  # update age by name
        ° add_feature # add feature by name
        ° delete_one  # delete one by name
        ° delete_all
        ° exit""")
    try:
        while True:
            command = input("Enter a command: ").strip()
            if command == "exit":
                print("Good bye!")
                break
            elif command == "help":
                print("""Available commands:
        ° help
        ° create
        ° read_all
        ° read_one    # read one by name
        ° update_age  # update age by name
        ° add_feature # add feature by name
        ° delete_one  # delete one by name
        ° delete_all
        ° exit""")
            elif command == "read_all":
                read_all()
            elif command == "create":
                create()
            elif command == "read_one":
                read_by_name()
            elif command == "update_age":
                update_age_by_name()
            elif command == "add_feature":
                add_feature_by_name()
            elif command == "delete_one":
                delete_by_name()
            elif command == "delete_all":
                delete_all()
            else:
                print("Unknown action")
    except:
        print("Database connection failed")