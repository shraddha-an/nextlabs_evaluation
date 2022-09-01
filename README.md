Solutions to the Evaluation Rounds of NextLabs

## Part 1 - Regex Problem
1. Regex Solution: The notebook **regex_problem.ipynb**, in this repo, contains the solution to the first question. 
Alternately, please find the link to the colab notebook below.
  
[Link to Colab Notebook](https://colab.research.google.com/drive/16lmPURbM-VCWAnyb3kzFHl8Oi1s317fn?usp=sharing)

### How to Run
1) Run it on Colab.

## Part 2 - Customer Check-in Prediction
#### **1. EDA**: 
The notebook **EDA_Customer_Checkin_Prediction.ipynb** (branch: main) in this repo, contains the data analysis.
    Alternately, please find the link to the colab notebook below.
    
[Link to Colab Notebook](https://colab.research.google.com/drive/1-U8myjUyY9mj66vZlHjKLkWf6pcU4ngi?usp=sharing)
 

#### **2. Prediction Model**:
The notebook **EDA_Customer_Checkin_Prediction.ipynb** (branch: main) in this repo, contains the Ml and neural network models 
  to predict whether a customer will check-in to the hotel or not.
    Alternately, please find the link to the colab notebook below.
    
  [Link to Colab Notebook](https://colab.research.google.com/drive/1wpTq5k42k6fY3cR8enqxVqrB9nfOcJ6_?usp=sharing)
  
    
  ### How to Run
  1) Running on Colab: Please make sure to restart runtime after installing the packages (at the top) in the notebooks.
  

#### **3. Deploying the Model**: 
I've used the [Streamlit library](https://docs.streamlit.io/library/get-started) to deploy my neural net classifier and have it make predictions on the input the user enters in a web page. I would recommend running the notebooks in Colab itself; and deploy the model on your local machines. Detailed instructions will be below.

  **Instructions:**

  1) Clone this repository; [link](https://github.com/shraddha-an/nextlabs_evaluation), on your local machines.
  2) Make sure you are in the project directory; for simplicity I've kept all files/scripts under a single folder.
  3) Create a new environment. I recommend using conda.
  4) Install the packages listed in requirements.txt
  5) Perform a small test to ensure scikit-learn with the version 1.0.2 has been installed. 
      Otherwise an error will be thrown at deployment, as my pickled feature transformer uses scikit-learn==1.0.2
  6) Likewise, make sure the streamlit library has been installed. I've used conda again for installing packages, but here's the [official installation guide](https://docs.streamlit.io/library/get-started/installation) from Streamlit for reference.
  7) My **deployed_script.py** requires the saved tf.keras nn model, the pickled sklearn preprocessor, and other Python lists also pickled. Before deploying, please check to see that these files are present, and, under the same directory as the deploy_script.py file.
  8) To deploy, please type

  ```
  streamlit run deploy_script.py
  ```
  9) You should see a web page like so, which asks for the features to be input. Once you've inputted the features, pressing on Predict will generate the prediction.
  
<img width="1440" alt="Screenshot 2022-09-01 at 18 46 02" src="https://user-images.githubusercontent.com/62532888/187923268-ab40ff13-056c-49d1-90a5-ba1b7b547161.png">
