
#%% Hugging Face MBART Model implementation  
# from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
# model = MBartForConditionalGeneration.from_pretrained("aroot/eng-guj-simcse_central_ssblu")
# tokenizer = MBart50TokenizerFast.from_pretrained("aroot/eng-guj-simcse_central_ssblu")
# tokenizer.src_lang = "en_IN"

# def translate_en_to_gu(article_en : str):
#     try:
#         encoded_en = tokenizer(article_en, return_tensors="pt")
#         generated_tokens = model.generate(
#             **encoded_en,
#             forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"])
        
#         text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
#         print(text)
#         return text
#     except Exception as e :
#         print(e)
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
def translate_en_to_gu(article_en : str):
    try:
        model_name = "rooftopcoder/mT5_base_English_Gujrati" # Example model for English to German translation
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        input_ids = tokenizer(article_en, return_tensors="pt").input_ids
        translation_ids = model.generate(input_ids)
        translation = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
        return translation
    except Exception as e :
        print(e)
    





    
#%%   Google Trans Implementation
from googletrans import Translator

def g_translate_en_to_gu(article_en:str):
    translator = Translator()
    try :
        translation = translator.translate(article_en, dest='gu')
        # translation = translator.translate(text, dest='gu')
        
        return translation.text
    except Exception as  e:
        print(e)
        

