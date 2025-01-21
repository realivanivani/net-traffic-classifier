"""
This script preprocesses a dataset of HTTP requests for use in training a machine learning model 
to detect anomalous network traffic.

**Data Preparation:**

1. **Dataset:**
   - The dataset should be located in the folder specified by the `folder_path` variable.
   - Each HTTP request should be stored in a separate `.txt` file within this folder.
   - The filenames should contain information about the data:
      - "Training" or "Test" to indicate the dataset split.
      - "normal" or "anomalous" to label the traffic type. 
      - Example filenames: 
         - normalTrafficTraining.txt
         - anomalousTrafficTest.txt

2. **`parse_http_request` function:**
   - This function (separate file) is crucial for extracting relevant features from the raw HTTP request text. 
   - It should parse the request and extract features

**Output:**

- `http_requests_all.csv`: Contains all parsed requests from all files.
- `http_requests_train.csv`: Contains parsed requests for training the model.
- `http_requests_test.csv`: Contains parsed requests for evaluating the model. 

**Before Running:**

1. **Adjust `folder_path`:** 
   - Ensure that the `folder_path` variable correctly points to the directory containing the dataset files.

"""

# Folder containing the .txt files
folder_path = 'csic_dataset/'

# List to store all parsed request data
all_requests = []

# Iterate through all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        # Determine Train_Test and Normal_Anom from the filename
        if 'Training' in filename:
            train_test = 'Training'
        elif 'Test' in filename:
            train_test = 'Test'
        else:
            train_test = 'Unknown'  # In case the filename doesn't match

        if 'normal' in filename:
            normal_anom = 'Normal'
        elif 'anomalous' in filename:
            normal_anom = 'Anomalous'
        else:
            normal_anom = 'Unknown'  # In case the filename doesn't match

        with open(os.path.join(folder_path, filename), 'r') as file:
            text = file.read()

            # Split the text into individual HTTP requests (based on 'GET' or 'POST')
            requests = re.split(r'\n(?=GET|POST)', text)
            for request in requests:
                parsed_data = parse_http_request(request)
                parsed_data['Train_Test'] = train_test
                parsed_data['Normal_Anom'] = normal_anom
                all_requests.append(parsed_data)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_requests)

# Save the DataFrame as a CSV file
df.to_csv('http_requests_all.csv', index=False)


# Now, since the assignment specified that the model should be trained only on the normalTrafficTraining.txt file, we'll split it by train and test
df_train = df[df.Train_Test == 'Training']
df_train.to_csv('http_requests_train.csv', index=False)

df_test = df[(df.Train_Test == 'Test')]
df_test.to_csv('http_requests_test.csv', index=False)

print(f"Data has been saved")
