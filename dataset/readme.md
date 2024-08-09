
# Dataset for CSIC 2010 HTTP Request Classification

This directory contains the CSIC 2010 dataset, which is used for parsing, analyzing, and classifying HTTP requests as part of a network traffic classification project. The aim is to distinguish between normal (legitimate) and malicious (anomalous) HTTP requests.

## Dataset Description

Dataset Description: The HTTP dataset CSIC 2010 contains the generated traffic targeted to an e- Commerce web application developed at our department. In this web application, users can buy items using a shopping cart and register by providing some personal information. As it is a web application in Spanish, the data set contains some Latin characters.
The dataset is generated automatically and contains 36,000 normal requests and more than 25,000 anomalous requests. The HTTP requests are labeled as normal or anomalous and the dataset includes attacks such as SQL injection, buffer overflow, information gathering, files disclosure, CRLF injection, XSS, server side include, parameter tampering and so on. This dataset has been successfully used for web detection in previous works [4, 5, 6, 7, 8, 9].

The traffic is generated following the next steps:

First, real data are collected for all the parameters of the web application. All the data (names, surnames, addresses, etc.) are extracted from real databases. These values are stored in two databases: one for the normal values and other for the anomalous ones. Additionally, all the public available pages of the web application are listed.
Next, normal and anomalous requests are generated for every web page. In the case that normal requests have parameters, the parameter values are filled out with data taken from the normal database randomly. The process is analogous for anomalous requests, where the values of the parameters are taken from the anomalous database.

Three types of anomalous requests were considered:

1) Static attacks try to request hidden (or non-existent) resources. These requests include obsolete files, session ID in URL rewrite, configuration files, default files, etc.

2) Dynamic attacks modify valid request arguments: SQL injection, CRLF injection, cross-site scripting, buffer overflows, etc.

3) Unintentional illegal requests. These requests do not have malicious intention, however they do not follow the normal behavior of the web application and do not have the same structure as normal parameter values (for example, a telephone number composed of letters).
   

## Contents

- **csic_dataset.zip**: This zip file contains the raw dataset used for training and evaluating HTTP request classifiers. Extracting this file will yield three text files:
  - **normalTrafficTraining.txt**: Contains HTTP requests representing normal traffic used for training classifiers.
  - **normalTrafficTest.txt**: Contains HTTP requests representing normal traffic used for testing classifiers.
  - **anomalousTrafficTest.txt**: Contains HTTP requests representing malicious or anomalous traffic used for testing classifiers.

## Data Source

The dataset can be downloaded from the [official website](http://www.isi.csic.es/dataset/) (Update: seems the link is not active anymore. Here is a working reference: https://web.archive.org/web/20130924222653/http://iec.csic.es/dataset) .

## Dataset Format

Each file contains multiple rows, each representing an HTTP request with the following structures (few examples):

```
GET http://localhost:8080/tienda1/publico/anadir.jsp?id=3&nombre=Vino+Rioja&precio=100&cantidad=55&B1=A%F1adir+al+carrito HTTP/1.1
User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)
Pragma: no-cache
Cache-control: no-cache
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Encoding: x-gzip, x-deflate, gzip, deflate
Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5
Accept-Language: en
Host: localhost:8080
Cookie: JSESSIONID=81761ACA043B0E6014CA42A4BCD06AB5
Connection: close

POST http://localhost:8080/tienda1/publico/anadir.jsp HTTP/1.1
User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)
Pragma: no-cache
Cache-control: no-cache
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Encoding: x-gzip, x-deflate, gzip, deflate
Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5
Accept-Language: en
Host: localhost:8080
Cookie: JSESSIONID=933185092E0B668B90676E0A2B0767AF
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 68

id=3&nombre=Vino+Rioja&precio=100&cantidad=55&B1=A%F1adir+al+carrito
```

## Usage

To utilize this dataset for training and evaluating a classifier, follow these steps:

1. **Extract** the `csic_dataset.zip` file to access the individual `.txt` files.
2. **Parse** the HTTP requests by processing the lines in each file to extract meaningful features for classification.
3. **Preprocess** the data, which may involve tokenizing requests, handling URL parameters, and encoding categorical features.
4. **Train** your classifier using `normalTrafficTraining.txt` as the training set.
5. **Evaluate** the classifier's performance on both `normalTrafficTest.txt` and `anomalousTrafficTest.txt`.

## Notes

- The data must be preprocessed and feature-engineered before being fed into machine learning models.
- Consider both supervised and unsupervised learning approaches, depending on your analysis goals.

## Licensing and Citation

Please ensure you comply with any licensing terms provided by the dataset source. If using the data for research or publication, cite the original dataset appropriately.
