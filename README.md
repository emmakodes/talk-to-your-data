# talk-to-your-data project
This project aid you to build a talk-to-your-data chatbot using openai LLM, LangChain, and Streamlit. 
Basically:
- You clone the project
  `git clone https://github.com/emmakodes/talk-to-your-data.git`
- `cd talk-to-your-data`
- create a new virtual environment called `.venv`
  `python -m venv .venv`
- Activate the virtual environment
`.venv\Scripts\activate`
- Install the project requirements
`pip install -r requirements.txt`
- Add your document to `mydocument` directory and delete `animalsinresearch.pdf` already existing inside `mydocument` directory. `animalsinresearch.pdf` is my own document except you want to test with my own data
- Delete the files in `vector_index` directory so as to hold the vectors of your own document.
- Start the app using the following command:
`streamlit run app.py`
You will see a UI very similar to the following:
![animalinresearch1](https://github.com/emmakodes/talk-to-your-data/assets/34986076/afcfed09-a277-415a-abb6-5267603a144e)


Feel free to go into `app.py` to customize the UI to how you want.





