API Calls on the open AI is not free, each and every api calls will charges you money based on the tokens that it uses,
so alternative to that you can use models like gemini as its free for now

In order to use 
step 1: search in google gemini studio
            - Open Google AI Studio - https://aistudio.google.com 
            https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=Cloud-SS-DR-AIS-FY26-global-gsem-1713578&utm_content=text-ad&utm_term=KW_gemini%20studio&gad_source=1&gad_campaignid=23417416052&gbraid=0AAAAACn9t66AxI4P536IyKRST4Y9pxqSg&gclid=CjwKCAjwnN3OBhA8EiwAfpTYemn1nC7WdQ4BLryH7I_3WbmxVSImNVDSvf3BfjlJ-AChp4nAF7-siRoC8n0QAvD_BwE

step 2: sign in 
step 3: click on Get API Key - it will generate one and give you a tree tier one

step 4: Now in order to integrate with our python we run the SDK like this : 

            pip install -q -U google-genai

step 5: setup a folder and open in vs code and write this commends before step 4

        -python -m venev venv
        .\venv\Scripts\Activate
        pip freeze > requirements.text

        create a main.py in folder
        now paste from gemini the code mentioned in main.py