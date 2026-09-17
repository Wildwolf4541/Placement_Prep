import json
import time
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    
def list_all_videos(videos):
    print("\n")
    print("-"*70)
    for index,value in enumerate(videos,start=1):
        print(f"{index}. {value['name']} -> {value['time']}")
    print("-"*70)
    time.sleep(2)

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index= int(input("Enter the video number to update: "))

    if 1<=index<=len(videos):
        name=input("Enter new name: ")
        time=input("Enter new time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
        list_all_videos(videos)
    else:
        print("Invalid number")

def delete_video(videos):
    list_all_videos(videos)
    index= int(input("Enter the video number to update: "))
    
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        list_all_videos(videos)
    else:
        print("Invalid number")

def main():
    videos= load_data()
    while True:
        print("\n Welcome to Youtube Manager | Choose an Option ")
        print("1. List all Youtube videos.")
        print("2. Add a Youtube video.")
        print("3. Update an existing Youtube video.")
        print("4. Delete a Youtube video.")
        print("5. Exit the manager.")
        choice= input("Enter Your Choice: ")

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
                print("Invalid Choice")

if __name__=="__main__":
    main()