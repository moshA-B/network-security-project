import csv

def log_reader(file):
    try:
        with open(file,"r") as f:
            reader=csv.reader(f)
            all_list=[row for row in reader]
    except FileNotFoundError:
        print("file not found")
        return None
    return all_list


