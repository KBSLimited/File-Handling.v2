import os

def list_directory_contents(path):
    """List the contents of the given directory path."""
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        
        if contents:
            # Print each item in the contents list
            for item in contents:
                print(item)
        else:
            print(f"The directory '{path}' is empty.")
            
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    """Prompt user for directory path and list its contents."""
    directory_path = input("Enter the directory path: ").strip()
    
    if directory_path:
        # Call the function to list directory contents
        list_directory_contents(directory_path)
    else:
        print("Error: No directory path provided.")

if __name__ == "__main__":
    main()