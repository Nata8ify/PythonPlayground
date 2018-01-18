

def Main():
    with open("w.txt", "r+") as file:
        file.write("Hello, World!")
        file.write("\nสวัสดี, โลก!")
        print("++ \n"+file.read())
        file.close()

    file = open("r.txt", "r")
    # print(file.read()) # read all
    for line in file:
        if(line.__contains__("---")):
            file.close()
            break
        print(":: "+line)

if __name__ == "__main__" :
    Main()