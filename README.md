## Project Translation of Legal Documents : English to Gujhrati 

- My Approach to solve 

    1. I have find a hugging face model and integrate with FastAPI create an API Translation sytem via API
        - http://localhost:8000//api/translate

    2. We have also builtin API of Google translate via googletrans python module. I have also integrate this along With the FastAPI system 
        - http://localhost:8000//api/g_translate



### Hugging Face Model :
Hugging face provide  a open source model hub where so many pre-build models are available. Hugging Face also Provide Transformers module and pipeline utility to test and retrained Pre-build models.  I have try various pre-build Translation Models some of them are provide all most accurate result.I integrate a one of them with FastAPI system.   

#### Pre-Build Models I go through 

1. *[IndicTrans2](https://github.com/AI4Bharat/IndicTrans2.git)
2. Unbabel/TowerInstruct-v0.1
3. facebook/mbart-large-50-many-to-many-mmt
4. SnypzZz/Llama2-13b-Language-translate
5. facebook/nllb-200-distilled-1.3B
6. facebook/nllb-200-3.3B
7. google/madlad400-3b-mt
8. rooftopcoder/mT5_base_English_Gujrati
9. aroot/mbart-finetuned-eng-guj
10. aroot/eng-guj-wsample.43a
11. aroot/eng-guj-simcse_central_usbbu

## About Repository 
Project Translation Repository contains a folder WebAPI that is the project root folder Fast API app 
and It also contains a ipython notebook file that is my experiment hub. 

### Future Work 
If needed We can further go for the fine Tunning our model with Legal Gujrati language and terms.