import os #import the OS module to interact with OS

def directory_list(): 
    #defining a function
    while True: 
        #while loop allows the user to keep searching until they exit instead of having to restart the program each time
        directory = input("Please enter the directory you wish to go to or type '''exit''' to quit: ") 
        #user inputs the path they want to go to
        if directory.lower() == "exit": 
            #if user wants to exit, they type exit, .lower() ensures that whatever they type becomes lowercase
            print("Exiting...Goodbye!")
            break 
            #breaks the loop
        if os.path.exists(directory) and os.path.isdir(directory): 
            #checks to see if the directory exists and if it is a directory
            os.chdir(directory) 
            #changes to that directory
            print("Directory changed to: ", os.getcwd()) 
            #prints the current working directory
            view_files = os.listdir() 
            #variable to list and view the files in the directory
            if view_files:
                print(f"Here are the files in this directory:  {view_files}") 
                #prints a list of the files in the directory if there are any else it will print the following:
            else:
                print("No files found! ")
            file_size = sum(os.path.getsize(file) for file in view_files if os.path.isfile(file)) 
            #adds the sum of view_files files and checks if they are files, .getsize returns the file or directory in bytes           
            if file_size >= 1024: 
                #if greater than 1024 bytes, converts to Kilobytes
                print(f"The total file size = {file_size/1024:.2f} KBs.") 
                # prints the file size in KB as a floating number
            else:
                print(f"The total file size = {file_size} bytes.")
        else: 
            #if directory not found, prints this
            print("Directory does not exist, try again.") 
directory_list() #runs the function
