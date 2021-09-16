folder_path = input().split("\\")
filename, extension = folder_path[len(folder_path) - 1].split(".")
print(f"File name: {filename}\nFile extension: {extension}")