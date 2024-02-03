from fastapi import FastAPI, HTTPException, Query
from translation import translate_en_to_gu,g_translate_en_to_gu
from _model import Article
app = FastAPI()
@app.get('/')
def base():
    return {"message":"This Site can Handle Two Post request via API. Visit '/docs' for documentation"}

@app.post("/api/translate", tags=['Hugging Face Model'])
def translator_api(article:Article):
    try: 
        article_gu = translate_en_to_gu(article.article )
        return {"article_gu":article_gu}
    except Exception as e: 
        raise HTTPException(e)

@app.post("/api/g_translate", tags=['Google Translator API'])
def google_translator_api(article:Article):
    try: 
        article_gu = g_translate_en_to_gu(article.article)
        
        return {"article_gu":article_gu}
    except Exception as e: 
        raise HTTPException(e)