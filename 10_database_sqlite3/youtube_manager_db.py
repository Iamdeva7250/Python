import sqlite3

conn = sqlite3.connect('youtube_video.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found.")
    else:
        print("\n************ Video List *************")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Time: {row[2]}")
            print("\n************ Video List *************")

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("✅ Video added successfully!")

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("✅ Video updated successfully!")

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("🗑️ Video deleted successfully!")

def main():
    while True:
        print("\n📺 Youtube Manager App with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == "3":
            try:
                video_id = int(input("Enter the video ID: "))
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_videos(video_id, name, time)
            except ValueError:
                print("❌ Invalid ID, must be a number.")
        elif choice == "4":
            try:
                video_id = int(input("Enter the video ID to delete: "))
                delete_videos(video_id)
            except ValueError:
                print("❌ Invalid ID, must be a number.")
        elif choice in ("5", "q", "quit", "exit"):
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

    conn.close()

if __name__ == "__main__":
    main()
