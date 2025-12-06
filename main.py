import json 

FILENAME = "youtube.txt" 



def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open(FILENAME, 'w') as f:
        json.dump(videos, f)



# Case 1
def list_all_videos(videos): 
    print("\n")
    print("-"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} Duration {video['time']}")   
    print("-"*70)

    
# Case 2
def add_video(videos):
    video_name = input("Enter Video name: ")
    video_time = input("Enter Video time: ")
    videos.append({'name': video_name, 'time':video_time})
    save_data_helper(videos)


# Case 3
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video you want to update"))
    if 1<= index <=len(videos):
        new_video_name = input("Enter new Video name: ")
        new_video_time = input("Enter new Video time: ")
        videos[index-1]={'name':new_video_name,'time': new_video_time}
        save_data_helper(videos)
    else:
        print("\n Invalid index selected!")

# Case 4
def delete_video(videos):
    index = int(input("Enter the video you want to Delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("\n Invalid index selected")


# Case 5
def exit_app(Greating):
    pass



def main():
    videos = load_data()
    while True:
        
        print("\n Youtube Manager | Choose an Option")
        print("\n 1. List all Videos")
        print("\n 2. Add a Youtube Videos")
        print("\n 3. Update youtube Video Videos")
        print("\n 4. delete a YT  Videos")
        print("\n 5. Exit the app")
        choice = input("\n Enter Your Choice: ")

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
                print("\n Invalied Choice!!")


if __name__== "__main__":
    main()
    
   
