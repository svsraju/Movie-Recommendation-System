# Content Based Movie-Recommendation-System
![image](https://user-images.githubusercontent.com/46058709/83594408-be664300-a524-11ea-9e06-1372b97e2ca5.png)

### Table of Contents
1. [Installations](#libraries)
2. [Project Motivation](#motivation)
3. [File Structure](#structure)
4. [Project Components](#project_componenets)
5. [Building the project](#Building)
6. [Plot Demos](#demo1)
7. [Classification Demo](#demo2)
8. [Licensing, Authors, and Acknowledgements](#licensing)


## 1. Installations <a name="libraries"></a>
We are not using any complex alogorithms for the application.so you need not include any installation.

## 2.Project Motivation<a name="motivation"></a>

I was wanted to build a recommender system, as it was one of the main applications of machine learning. I dont wanted to start with complex algorithms, but I have explored the content based recommender systems. These systems work with data that user provides. It should be clear that with out the user provided data, content based systems cannot recommend any data.

My main aim was to deploy the system as a app, where people can use the same and check the movies that they might want to watch based on the ratings they give.

## 3. File Structure <a name="structure"></a>

```
- templates
| - base.html
| - home.html  # main page of web app
| - recommend.html  # classification result page of web app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md
```
[Figure 8](https://www.figure-eight.com/) helps companies transform their data by providing human annotators and machine learning to annotate data at all scales.
The data we use for the project was downloaded from [Figure 8](https://www.figure-eight.com/dataset/combined-disaster-response-data/).
### data
#### disaster_messages.csv :
"disaster_messages.csv" dataset contains messages that were sent during disaster events and build a classifier to identify messages or events in need of attention or relief.

![image](https://user-images.githubusercontent.com/46058709/78414949-5a86d300-75e4-11ea-9ea1-eb937c696e9b.png)


#### disaster_categories.csv  :
"disaster_categories.csv" dataset contains these categories.Each message is tagged with a the categories it belongs to. We have 36 categories in total



![image](https://user-images.githubusercontent.com/46058709/78414981-86a25400-75e4-11ea-9314-18dc21d6adcd.png)

#### 4. Project Components<a name="project_componenets"></a>
There are three components that I have used to complete  this project.

Notebooks
ETL Pipeline Prep.ipynb - jupyter notebook for data exploration and cleaning
ML Pipeline Preparation - jupyter notebook for model selection and evaluation

##### 4.1 ETL Pipeline

File _data/process_data.py_ contains data cleaning pipeline that:

- Loads the `messages` and `categories` dataset
- Merges the two datasets
- Cleans the data
- Stores it in a **SQLite database**

##### 4.2 ML Pipeline

File _models/train_classifier.py_ contains machine learning pipeline that:

- Loads data from the **SQLite database**
- Splits the data into training and testing sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs result on the test set
- Exports the final model as a pickle file

#### 4.3 Flask Web App
File _app/template/_ has files that contain a html files which are used for the web application

- Frontend was designed using **Bootstrap**
- Backend was designed using **Flask** and visualizations were done with help of **plotly**


### 5. Building the project<a name="Building"></a>

`process_data.py` and `train_classifier.py` are built in a such a way that if someone in the future comes with a revised or new dataset of messages, they will be able to easily create a new model just by running the code. 

These Python scripts can be run with additional arguments specifying the files used for the data and model.

##### 5.1 Running ETL pipeline

To run ETL pipeline that cleans data and stores in database python:

`data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db `

Here first argument is the python file, which needs both messages and categories datasets. The final argument is the database.

##### 5.2 Running ML pipeline

To run ML pipeline that trains classifier and saves python:

`models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

Here First argument to be passed is the python file, next would be be database where cleaned data is stored and final argument is the name of the pickle file 

##### 5.3 Running the Web App

Run the following command in the app's directory to run your web app:
`python run.py`

After that Go to http://0.0.0.0:3001/ or http://localhost:3001/



#### 6. Plot Demos <a name="demo1"></a>
![Plot demos](https://github.com/sousablde/Disaster-Response-Pipeline/blob/master/Images/plots_demo.gif)

##### 7. Classification Demo <a name="demo2"></a>
![Classification demos](https://github.com/sousablde/Disaster-Response-Pipeline/blob/master/Images/classification_demo.gif)



## 9. Licensing, Authors, Acknowledgements<a name="licensing"></a>
I am greatly to Udacity and Figure8 for their efforts in bringing this project.I would like to also thank ![Beatriz Sousa](https://github.com/sousablde) for open sourcing her work

