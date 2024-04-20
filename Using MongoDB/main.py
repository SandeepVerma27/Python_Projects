# import pymongo
# or 
from pymongo import MongoClient
from bson import ObjectId
# client=pymongo.MongoClient("mongodb+srv://7458vermaravi:sandeepMongo116@cluster0.pufde8n.mongodb.net/youtubemanager")
# not a good practice to use like this us id and password
# or 
client=MongoClient("mongodb+srv://7458vermaravi:sandeepMongo116@cluster0.pufde8n.mongodb.net/")
db=client["youtubemanager"]
video_collection=db["video"]
print(video_collection)

def list_video():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']} and time:{video['time']}")
def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})
    
def update_video(video_id,name,time):
    video_collection.update_one({"_id": ObjectId(video_id)},{"$set":{"name":name,"time":time}})
def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id) })
    
def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all video: ")
        print("2. Add new video with time: ")
        print("3. Update video: ")
        print("4. Delete video: ")
        print("5. Exit Video: ")
        choice=input("Enter your choice: ")
        if choice== "1":
            list_video()
        elif choice== "2":
            name=(input("Enter the video: "))
            time=(input("Enter the time: "))
            add_video(name,time)
        elif choice=="3":
            video_id=(input("Enter the video id: "))
            name=(input("Enter the updated video: "))
            time=(input("Enter the updated time: "))
            update_video(video_id,name,time)
        elif choice=="4":
            video_id=(input("Enter the video_id: "))
            delete_video(video_id)
        elif choice=="5":
            break
        else:
            print("Invalid input: ")
               

if __name__ == "__main__":
    main()
   
    


