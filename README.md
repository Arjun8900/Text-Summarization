# Text-Summarization

## Index
1. [Description](#Description)
2. [Saving model to local location ](#Saving-model-to-local-location )
3. [Loading model from local location](#Loading-model-from-local-location)
4. [Demo](#demo)

## Description: 
- In this repo, I'm using `Langchain` + `Hugging-Face` model. Models are downloaded from Hugging-Face, which are used for used for summarization of text.
- This repo can be used offline as well. The <i><b>Tokenizer</b></i> and <i><b>Model</b></i> will be downloaded very first time, from next time onwards, this code will use the downloaded model offline.<br>
<u><b>NOTE</b></u>: Uncomment the Line 17-18 and Line 21-22 for first time, as it'll download the model in respective folder location.

## Saving model to local location 
- Tokenizer will saved to Tokenizer folder. 
- Model will saved to Model folder. 
- I've only pushed empty folders of Tokenizer and Model, as the models are of huge size.




```python
tokenizer_local_location = f"/Users/arjunsingh.kanwal/Documents/CODE/Python/Text-Summarization/Tokenizer/{model_name}"
model_local_location = f"/Users/arjunsingh.kanwal/Documents/CODE/Python/Text-Summarization/Model/{model_name}"


# SAVE TOKENIZER
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(tokenizer_local_location)

# SAVE MODEL
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.save_pretrained(model_local_location)

```

## Loading model from local location
```python
# LOAD TOKENIZER && MODEL
tokenizer = AutoTokenizer.from_pretrained(tokenizer_local_location)
model = AutoModelForSeq2SeqLM.from_pretrained(model_local_location)
```
## Demo: 
