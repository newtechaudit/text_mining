for i in range(1000):
    # проверяем распознано ли аудио
    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id_), headers=header)
    req = req.json()
    # если распознано — выходим из цикла
    if req['done']: break
    # если нет — выводим сообщение
    print("файл в обработке")
    # ждём 10 секунд
    time.sleep(10)

#создаем временные хранилища
all_sentenses = []
sentenses_dic = {}
all_text =''
for id,chunk in enumerate(req['response']['chunks']):
#     if id%2==1:  #актуально только для двухканального аудио

    chnk = chunk['alternatives'][0]['text'].lower()
    all_text = all_text+chnk+' '
        
print("Часть распознанного текста: ",all_text[:55])