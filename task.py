from transformers import T5Tokenizer , T5orConditionalGeneration 
from models import TranslationModel

tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=512)
translator = T5orConditionalGeneration.from_pretrained("t5-small")
## store_translation 
## Translation request and save it to the db 
def store_translation(t):
    model = TanslationModel(text =t.text , base_lang = t.base-lang , final_lang = t.final_lang)
    model.save()
    return model.id

## run_translation 
## Run a pretrained deep learning model 
def run_translation(t_id:int):
   model = TranslationModel.get_by_id(t_id)
   prefex = f"tranlate {model.base_lang} to {model.final_lang}: {model.text}"
   input_ids = tokenizer(prefex, return_tensors = "pt").input_ids
   
   outputs = translator.generate(input_ids, max_new_tockens=512)
   translation  = tokenizer.decode(outputs[0], skip_special_tokens=True)
   model.translation = translation
   model.save() 


##find_translation
##retrieve a translation from db 
