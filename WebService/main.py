from fastapi import FastAPI, HTTPException, Query
from translation import translate_en_to_gu,g_translate_en_to_gu
from _model import Article
app = FastAPI()

@app.post("/api/translate")
def translator_api(article:Article):
    try: 
        article_gu = translate_en_to_gu(article.article )
        return {"article_gu":article_gu}
    except Exception as e: 
        raise HTTPException(e)

@app.post("/api/g_translate")
def translator_api(article:Article):
    try: 
        article_gu = g_translate_en_to_gu(article.article)
        
        return {"article_gu":article_gu}
    except Exception as e: 
        raise HTTPException(e)