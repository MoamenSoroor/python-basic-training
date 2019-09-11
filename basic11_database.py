import sqlite3

def main():
    print("main function")
    
if __name__=="__main__": main()

def connect_to_db():
    db = sqlite3.connect("mydatabase.db")
    
