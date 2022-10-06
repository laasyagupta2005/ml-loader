import requests 

def get_data(train_data_url, test_data_url = None):
    print("Fetching train_data...")
    train_req = requests.get(train_data_url)
    csv_file = open("data/train_data.csv", "wb")
    csv_file.write(train_req.content)
    csv_file.close()
    print("done.")

    if test_data_url != None:
        print("Fetching test_data...")
        test_req = requests.get(test_data_url)
        csv_file = open("data/test_data.csv", "wb")
        csv_file.write(test_req.content)
        csv_file.close()
        print("done.")



if __name__ == "__main__":
    train_data_url = input() 
    test_data_url = None                        # input()
    get_data(train_data_url, test_data_url)