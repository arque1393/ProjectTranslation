from fastapi import FastAPI, HTTPException
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("SnypzZz/Llama2-13b-Language-translate")
tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang="en_XX")


def translate_en_to_gu(article_en : str = ""):
    try:
        model_inputs = tokenizer(article_en, return_tensors="pt")
        generated_tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"]
        )
        
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