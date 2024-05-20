# Text-Summarization

1. [Saving model to local location ](#Saving-model-to-local-location )
2. [Loading model from local location](#Loading-model-from-local-location)
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
