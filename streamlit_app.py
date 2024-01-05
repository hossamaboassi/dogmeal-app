# Import necessary libraries
import streamlit as st
from pydantic import BaseModel
from typing import List
import openai

# Define the BaseModel class for data validation
class MealSuggestions(BaseModel):
    suggestions: List[str]

# Streamlit code to create the UI
def main():
    # Set up the title and description of the web app
    st.title("Healthy Dog Meal Generator")
    st.write("Generate concise meal suggestions for your dog based on breed, age, weight, and conditions.")

    # Input section: User inputs for dog details
    breed = st.text_input("Dog Breed", "")
    age = st.slider("Dog Age (in years)", min_value=1, max_value=15, value=3)
    weight = st.slider("Dog Weight (in kg)", min_value=1, max_value=100, value=10)
    conditions = st.text_area("Special Conditions (if any)", "")

    # Button to trigger the meal suggestions generation
    if st.button("Generate Meal Suggestions"):
        # Create a prompt based on user inputs
        prompt = f"Generate healthy meal suggestions for a {age}-year-old {breed} dog weighing {weight}kg with the following conditions: {conditions}"

        # Replace with your OpenAI API key
        openai_api_key = "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"
        openai.api_key = openai_api_key

        # Replace with your OpenAI model
        openai_model = "text-davinci-003"

        # Call the structured_generator function with the user input
        result = structured_generator(openai_model, prompt, MealSuggestions)

        # Display the generated meal suggestions
        if result.suggestions:
            st.subheader("Generated Meal Suggestions")
            for i, suggestion in enumerate(result.suggestions[:3]):
                st.write(f"**Meal {i + 1}:** {suggestion}")

# Function to interact with OpenAI API
def structured_generator(openai_model, prompt, custom_model):
    result = openai.Completion.create(
        engine=openai_model,
        prompt=prompt,
        max_tokens=150,
        n=3,  # Generate three suggestions
        stop=None,
        temperature=0.6,
    )
    return custom_model.parse_obj({"suggestions": [choice['text'] for choice in result['choices']]})

# Protect the script to run only when it's the main module
if __name__ == "__main__":
    main()
