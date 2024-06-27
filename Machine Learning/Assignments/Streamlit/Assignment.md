# Streamlit - Deployment Module

## Subjective Test

### 1. What is Streamlit and what are its main features?
**Streamlit** is an open-source Python library used to create and share data applications. Its main features include:
- Simple syntax for building UI components
- Reactive and interactive elements
- Easy integration with data sources and machine learning models
- Rapid prototyping and deployment

### 2. How does Streamlit differ from other web application frameworks like Flask or Django?
**Streamlit** is designed specifically for data applications with minimal code, focusing on simplicity and rapid development. In contrast:
- **Flask** is a micro-framework for building web applications with more control over the app structure.
- **Django** is a full-fledged web framework that provides a lot of built-in features for larger, more complex applications.

### 3. What are some typical use cases for Streamlit?
Typical use cases include:
- Data exploration and visualization
- Machine learning model demonstrations
- Interactive dashboards
- Prototyping data-driven applications

### 4. How do you create a simple Streamlit app?
To create a simple Streamlit app:
1. Install Streamlit: `pip install streamlit`
2. Create a Python script (e.g., `app.py`):
    ```python
    import streamlit as st
    st.title('Hello, Meta Scifor!')
    st.write('This is a simple test')
    ```
3. Run the app: `streamlit run app.py`

### 5. Can you explain the basic structure of a Streamlit script?
A basic Streamlit script consists of:
- **Imports**: Importing the Streamlit library.
- **Widgets**: Creating UI components like titles, text, buttons, etc.
- **Logic**: Implementing the logic to handle user interactions and data processing.

### 6. How do you add widgets like sliders, buttons, and text inputs to a Streamlit app?
Use the following Streamlit functions:
- **Slider**: `st.slider('Label', min_value, max_value)`
- **Button**: `st.button('Label')`
- **Text Input**: `st.text_input('Label')`

Example:
```python
age = st.slider('Select your age', 0, 100)
if st.button('Submit'):
    st.write(f'Your age is {age}')
name = st.text_input('Enter your name')
st.write(f'Hello, {name}')
```

### 7. How does Streamlit handle user interaction and state management?
Streamlit reruns the script from top to bottom whenever an interaction occurs, ensuring the UI is always up-to-date. State management can be handled using `st.session_state` to store and retrieve data across reruns.

### 8. What are some best practices for organizing and structuring a Streamlit project?
Best practices include:
- **Modularize**: Break down the code into functions and modules.
- **Reuse components**: Create reusable UI components.
- **Documentation**: Add comments and docstrings.
- **Configuration**: Use configuration files for settings and parameters.
- **Testing**: Write tests for data processing and business logic.

### 9. How would you deploy a Streamlit app locally?
To deploy a Streamlit app locally:
1. Run the app using `streamlit run app.py`.
2. Access the app at `http://localhost:2003` in a web browser.

### 10. Can you describe the steps to deploy a Streamlit app?
To deploy a Streamlit app:
1. **Local Deployment**: Use `streamlit run your_script.py`.
2. **Cloud Deployment**: Use services like Streamlit Cloud, Heroku, or AWS.
3. **Docker**: Create a Dockerfile and build a Docker image.

### 11. What is the purpose of the requirements.txt file in the context of Streamlit deployment?
The `requirements.txt` file lists all the dependencies required to run the Streamlit app. It ensures the app environment can be replicated accurately by installing the exact versions of the packages specified.
