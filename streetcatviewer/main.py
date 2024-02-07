import os
from streetcatviewer import database

def main():
    print("Here are all feeders: ")
    for feeder in database.get_cams():
        print(feeder['nickname'])


if __name__ == "__main__":
    main()