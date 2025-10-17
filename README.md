# To-Do App

This is a simple to-do backend application built with FastAPI and a frontend using Streamlit.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Backend

To run the FastAPI backend, use:
```bash
uvicorn main:app --reload
```

## Running the Frontend

To run the Streamlit frontend, create a new file `app.py` with the following content:
```python
import streamlit as st
import requests

st.title('To-Do App')

# Add your Streamlit frontend code here
```
Then run:
```bash
streamlit run app.py
```
