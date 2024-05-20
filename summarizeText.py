import warnings
warnings.filterwarnings("ignore")

# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

model_name = "Falconsai/text_summarization"
# model_name = "t5-base-finetuned-wikiSQL"

tokenizer_local_location = f"/Users/arjunsingh.kanwal/Documents/CODE/Python/Text-Summarization/Tokenizer/{model_name}"
model_local_location = f"/Users/arjunsingh.kanwal/Documents/CODE/Python/Text-Summarization/Model/{model_name}"

# SAVE TOKENIZER | Uncomment this for first time.
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# tokenizer.save_pretrained(tokenizer_local_location)

# SAVE MODEL | Uncomment this for first time.
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# model.save_pretrained(model_local_location)


# LOAD TOKENIZER && MODEL
tokenizer = AutoTokenizer.from_pretrained(tokenizer_local_location)
model = AutoModelForSeq2SeqLM.from_pretrained(model_local_location)


pipe = pipeline("summarization", model=model, tokenizer=tokenizer, max_length=100)
local_llm = HuggingFacePipeline(pipeline=pipe)


prompt = PromptTemplate(
    input_variables=["longText"],
    template="Summarize text : {longText}"
)
hub_chain = LLMChain(prompt=prompt, llm=local_llm, verbose=True)

while True:

    print("Please enter the text:", end =" ")
    user_input = str(input())
    if (user_input == ''): 
        break

    print(hub_chain.run(user_input))
    print()