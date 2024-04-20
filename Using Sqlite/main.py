'''
# new things ---> 
(''' '''---> make format )
'''

# import database 
import sqlite3
conn=sqlite3.connect('youtub_db')
cursor=conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS videos(id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             time TEXT NOT NULL) ''')               
# functions 
def list_all_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)" ,(name,time))
    conn.commit()
def update_video(videoId,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE Id=?",(new_name,new_time,videoId))
    conn.commit()
    
def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE Id =?",(videoId,))
    conn.commit()
    

def main():
    while True:
        print("\n Youtube manager app with DB ")
        print("1. List of all videos: ")
        print("2. Add videos :")
        print("3. Update the video: ")
        print("4: Delete the video: ")
        print("5. Exit from the App: ")
        choice=input("Enter your choice: ")
        # This part of the code is the main logic of the program. It presents a menu to the user with
        # different options for managing videos in the database. Here's a breakdown of what each part
        # does:
        if choice== '1':
            list_all_video()
        elif choice== '2':
            name=input("Enter the video: ")
            time=input("Enter the video time: ")
            add_video(name, time)
            
        elif choice=='3':
            videoId=input("Enter the video ID: ")
            name=input("Enter the name: ")
            time=input("Enter the time: ")
            update_video(videoId,name,time)      
        elif choice== '4':
            videoId=input("Enter the video Id")
            delete_video(videoId)  
        elif choice == '5':
            break
        else:
            print("Enter the correct choices ")
# conn.close()   
                
if __name__=="__main__":
    main()