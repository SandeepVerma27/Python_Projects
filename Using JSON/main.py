# error handling  (try catch)

# file=open('youtupe.txt','w')
# try:
#     file.write('python project')
# finally:
#     file.close()

# or (with write for the intraction with file)
# with open('youtub.txx','w') as file:
#     file.write('it automatic close the file')

# New Keyowrds in this projects
'''
{
    1. (try catch ---> for error handling try accept finally )
    2. (with---> open file sort syntax not need to close file after use)
    3. (match---> for matching the any type of data use instead of if else)
    4. (case _:---> use inside the match like default input handle)
    5. (main():--> wrap all method inside the main and like entry point of the program)
    6. (__name__--> call dander  give the name of the function)
    7. (JSON --> import json )
    8. (load(file)--> it json method that load the data from the file and convert the json)
    9. (json.dump('kya likhna','kaha linkhna')--->write the content or anything in the file)
    10. (enumrable()--> it give indexing on iterable values)
    11. (del)--> del keyword delete from the list.
   
   
   
    
}
'''
# import json 
import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)  
    except FileNotFoundError:
        return ["failed to upload "]
    finally:
        pass
    

# helper method 
def save_data_helper(videos):
    try:
       with open('youtube.txt','w') as file:
        json.dump(videos,file)
    except:
       print("Some error occur on saving time....")
    
        
    
# method list of all video 
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    
   
    for index, video in enumerate(videos, start=1):
        print(f"{index}. video name is = '{video['name']}  ', and duration is: = '{video['time']}' ")
  
        
    print("\n")
    print("*" * 70)


# add video 
def add_video(videos):
    name=input("Enter video name :")
    time=input("Enter video time: ")
    videos.append({"name":name, "time": time})
    save_data_helper(videos)

# update video 
def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the number to update "))
    if 1 <= index <= len(videos):
        name=input("Enter the new video name ")
        time=input("Enter the time of he video ")
        videos[index-1]={'name':name , 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected ")

# delete video 
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video index to delete "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print( "delete successful")
    else:
        print("Invalid video index ")
    
   

print(list_all_videos)
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager: | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit the loop")
        choice=input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice ")
if __name__=="__main__":
    main()
    
    
   

            
        
    