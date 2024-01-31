from fastapi import FastAPI, HTTPException, Query
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

article_en = 'Good Evening Guys. I like your approach to solve this. '
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer.src_lang = "en_IN"

def translate_en_to_gu(article_en : str):
    try:
        encoded_en = tokenizer(article_en, return_tensors="pt")
        generated_tokens = model.generate(
            **encoded_en,
            forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"])
        
        text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        print(text)
        return text
    except Exception as e :
        print(e)
    




app = FastAPI()

@app.post("/api/translate")
def translator_api(article:str):
    try: 
        article_gu = translate_en_to_gu(article)
        return {"article_gu":article_gu}
    except Exception as e: 
        raise HTTPException(e)