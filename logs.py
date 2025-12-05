with open("logs.txt", "r") as file:
    lines = file.readlines()
    
error_lines = [line for line in lines if line.startswith("ERROR:")]
    
with open("errors.txt", "w") as f:
    f.writelines(error_lines)
    
print("Total lines:", len(lines))
print("Error lines:", len(error_lines))