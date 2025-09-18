# mongodb+srv://youtubepi:Deva@7250@cluster0.ablykes.mongodb.net/

# import pymongo

from pymongo import MongoClient
from bson import ObjectId

# ✅ Use proper MongoDB URI (replace with your real user/pass)
client = MongoClient("mongodb+srv://youtubepi:Deva7250@cluster0.ablykes.mongodb.net/")
db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("✅ Video added successfully!")

def list_videos():
    videos = list(video_collection.find())
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )
        if result.modified_count:
            print("✅ Video updated successfully!")
        else:
            print("❌ No video found with that ID.")
    except Exception:
        print("❌ Invalid video ID format.")

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("🗑️ Video deleted successfully!")
        else:
            print("❌ No video found with that ID.")
    except Exception:
        print("❌ Invalid video ID format.")

def main():
    while True:
        print("\n📺 Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
