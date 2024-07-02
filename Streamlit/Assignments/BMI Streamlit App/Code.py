# bmi_calculator_top_image_feet.py
import streamlit as st

def calculate_bmi(height, weight):
    """Calculate BMI based on height (in feet) and weight (in kg)."""
    height_meters = height * 0.3048  # Convert feet to meters
    bmi = weight / (height_meters ** 2)
    return bmi

def main():
    st.title('BMI Calculator')

    # Display image with caption
    st.markdown('<h2 style="text-align: center;">Body Mass Index (BMI) Image</h2>', unsafe_allow_html=True)
    bmi_image_path = r"C:\Users\gchar\streamlit_app\streamlit_app\image.jpg"
    st.image(bmi_image_path, caption='BMI Image', use_column_width=True, output_format='JPEG')

    # Input fields
    height = st.slider('Select your height (in feet)', min_value=3.28, max_value=8.2, step=0.1)
    weight = st.slider('Select your weight (in kg)', min_value=10.0, max_value=300.0, step=0.1)

    # Calculate BMI
    if st.button('Calculate BMI'):
        bmi = calculate_bmi(height, weight)
        st.write(f'### Your BMI: {bmi:.2f}')

        # BMI Categories
        st.write('### BMI Categories:')
        st.write('- Underweight: BMI < 18.5')
        st.write('- Normal weight: 18.5 <= BMI < 25')
        st.write('- Overweight: 25 <= BMI < 30')
        st.write('- Obesity: BMI >= 30')

if __name__ == '__main__':
    main()
