def delete_function(string):
    delete = string
    with open("devicelist.txt", "r") as fp:
        lines = fp.readlines()

    with open("devicelist.txt", "w") as fp:
        for line in lines:
            if line.strip("\n") != delete:
                fp.write(line)
        print("The device has been deleted")














