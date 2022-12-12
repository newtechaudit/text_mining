# параметры запроса
key = 'ваш API - key yc’

# путь к файлу в бакете YC
filelink = 'https://storage.yandexcloud.net/bucket0011/test_audio.mp3' 
   
body ={
    "config": {
        "specification": {
            "languageCode": "ru-RU"
            , "audioEncoding": "MP3"
        }
    },
    "audio": {
        "uri": filelink
    }
}

header = {'Authorization': 'Api-Key {}'.format(key)}
POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"

# структура POST - запроса согласно инструкции API
req = requests.post(POST, headers=header, json=body)

#Получаем ответ от сервера, из которого забирам ID задачи на обработку аудиозаписи.
data = req.json()
id_ = data['id']  
print(id_)