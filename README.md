# Matuidi
The Paper Search Assistant
Built using Rasa


### nlu model: 
    train nlu:
        rasa train nlu
    test nlu:
        rasa shell nlu

### dialogue/core model:
    start custom action server:
        rasa run actions
    train core in new terminal:
        rasa train --out models --fixed-model-name rasa_models

### run chatbot:
    rasa shell

### run interative training:
    start custom action server:
        rasa run actions
    start interactive training in new terminal:
        rasa interactive

### integrate with telegram:
    start custom action server:
        rasa run actions
    start ngrok in new terminal:
        ./ngrok http 5005
        change webhook_url in credentials.yml
    connect to telegram in new terminal:
        rasa run --port 5005 --credentials credentials.yml --endpoints endpoints.yml

### run using rasa x:
    start custom action server:
        rasa run actions
    start ngrok in new terminal:
        ./ngrok http 5002
    export RASA_X_HOSTNAME=https://{number you get after running ngrok}.ngrok.io; rasa x
