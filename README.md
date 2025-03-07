# Для чего этот скрипт

Этот скрипт предназначен для автоматической проверки почты на наличие новых писем с ответами на вопросы с маркетплейса Ozon и отправки ответов на них через (не публичное) API. <br>
Скрипт предназначен для работы в паре с репозиторием (но можно использовать и отдельно) [Ozon-QuestionsSeller-EmailSender](https://github.com/EstebanQW/Ozon-QuestionsSeller-EmailSender) (сначала формируются письма с вопросами, отправляются на почту сотрудника (или проект для обработки вопросов), который их обрабатывает. Затем данный скрипт проверяет почту и отправляет ответы по API. Скрипт создавался, чтобы ослеживать среднее время ответа, количество обработанных вопросов)

______

## Начало работы

* [Какое письмо будет обрабатывать скрипт](#какое-письмо-будет-обрабатывать-скрипт)  
* [Создание функции](#создание-функции)  
* [Создание бакета с Cookie](#создание-бакета-с-cookie)  
* [Настройка триггера](#настройка-триггера)  
* [Запуск скрипта](#запуск-скрипта)  
* [Как работает скрипт](#как-работает-скрипт)  
* [Обработка ошибок](#обработка-ошибок)  
* [Важные замечания](#важные-замечания)  

## Какое письмо будет обрабатывать скрипт

В заголовке письма после "Re:" должен стоять id вопроса Ozon<br>
В теле письма первая строка должна содержать `[Ответить]_____` - если отвечаем на вопрос (или `[Отклонить]_____` -  если пропускаем вопрос и ничего не отвечаем на него)<br>
![image](https://github.com/user-attachments/assets/462827ce-f94b-4923-82b6-cfe9db10fbcb)



## Создание функции

1. Необходимо создать функцию python на [Yandex Cloud Functions](https://console.yandex.cloud/folders) <br>
2. Заменить содержимое файла `index.py` в вашей функции на содержимое файла `index.py` из данного репозитория<br>
3. Создать в функции 4 файла - `API_send_answer.py`,`login.py`,`mail_checker_ozon.py` и`requirements.txt`, вставить в них содержимое файлов `API_send_answer.py`,`login.py`,`mail_checker_ozon.py` и`requirements.txt` из данного репозитория.<br>
5. Перед запуском скрипта необходимо настроить параметры в файле `login.py`:<br>
`company_id`: Уникальный идентификатор компании на Ozon. Его можно найти в URL страницы компании на Ozon. Например, для URL https://www.ozon.ru/seller/ooo-mebelnaya-fabrika-volzhanka-1234/products/?miniapp=seller_1234 идентификатор компании — 1234.<br>
`imap_server`: Сервер для подключения к почте (например, imap.mail.ru).<br>
`imap_username`: Почта, которую необходимо проверять на входящие письма.<br>
`imap_password`: Пароль от почты для сторонних приложений.<br>
`trusted_mail`: Почта, с которой будут поступать письма. Важно соблюдать регистр символов.<br>
`bucket_name`: Название бакета в Yandex Object Storage.<br>
`file_name`: Название файла с куки в бакете.<br>
`AWS_ACCESS_KEY_ID`: Key ID для доступа к бакету.<br>
`AWS_SECRET_ACCESS_KEY`: Key для доступа к бакету.<br>
`region`: Регион бакета (обычно "ru-central1").
6. В настройках функции установить таймаут 60 секунд и сохранить изменения<br>
![image](https://github.com/user-attachments/assets/7b72ff96-543e-4886-9ad9-751239dee50f) 
7. Сделать функцию публичной переключив тумблер в обзоре функции<br>
![image](https://github.com/user-attachments/assets/251ebed7-2ee7-4a82-87cb-db9e51597b18)


## Создание бакета с Cookie 

Бакет создается, чтобы не обновлять куки в каждом скрипте, а обновлять только содержимое файла в бакете или производить обновление куки внутри одного из скриптов (добавляете в один из скрипотов актуальное куки, в этом же скрипте добавляете функцию обновления куки в бакете.)<br>
О том, как создать бакет и настроить к нему доступ лучше почитать в документации [Yandex Object Storage](https://yandex.cloud/ru/docs/storage/operations/buckets/create)<br>
Также есть видео от Яндекса, в котором всё достаточно подробно объясняется - [Используем Yandex Cloud Functions в работе с Object Storage](https://www.youtube.com/watch?v=_d-EPZ-X_Qo&ab_channel=YandexCloud)<br>
Если вы запускаете только один скрипт с куки Ozon, то можно обойтись без бакета и указывать куки напрямую в скрипте переменной.


## Настройка триггера

Создать триггер, который будет запускать функцию каждые 15 минут (время на ваше усмотрение)<br>
![image](https://github.com/user-attachments/assets/84fcbbf3-58c6-4e24-9e97-7a6b8b90fa14)


## Запуск скрипта

Для запуска скрипта необходимо:
1.	Зайти на [Yandex Cloud Functions](https://console.yandex.cloud/folders) 
2.	Перейти в триггеры <br>
![image](https://github.com/user-attachments/assets/c133a1b2-3391-412f-ad8c-d323d5c13b1f)

3.	Кликнуть по триггеру <br>
![image](https://github.com/user-attachments/assets/022810c2-777f-4802-8244-7c61007b2f22)

4.	В правом верхнем углу нажать кнопку «Запустить»: <br>
![image](https://github.com/user-attachments/assets/96b367a9-c0ab-48a2-950a-5b31ea64a328) <br>
Подтвердить действие: <br>
![image](https://github.com/user-attachments/assets/96f6b7ff-4808-4a87-afa2-d34546aa0464)
5.	Скрипт запущен (будет проверять почту на новые письма каждые 15 минут, при нахождении нужного письма отправлять ответ на вопрос по API Ozon)


## Как работает скрипт
Чтение cookie из Yandex Object Storage:
* Скрипт читает файл с куки из облачного хранилища Yandex (S3).
* Если файл успешно прочитан и куки корректны, скрипт переходит к следующему шагу.

Подключение к почтовому серверу:
* Скрипт подключается к почтовому серверу и проверяет входящие письма.
* Письма фильтруются по отправителю (`trusted_mail`).

Обработка писем:
* Скрипт извлекает текст письма, удаляет HTML-теги и разделяет содержимое на части.
* Если письмо содержит текст ответа, скрипт отправляет ответ через API Ozon.

Отправка ответа через API:
* Скрипт отправляет ответ на вопрос через API Ozon.
* Если отправка ответа завершается ошибкой, письмо помечается как непрочитанное.

Завершение работы:
* После обработки всех писем скрипт завершает работу и отключается от почтового сервера.

## Обработка ошибок
Если скрипт не может прочитать файл с куки, он завершает работу с сообщением об ошибке.<br>
Если отправка ответа через API завершается ошибкой, скрипт делает до 3 попыток с задержкой в 10 секунд.<br>
Если все попытки отправки ответа завершились неудачно, письмо помечается как непрочитанное.<br>

## Важные замечания
Убедитесь, что куки актуальны. Если куки истекли, скрипт не сможет отправить ответ через API.<br>
Скрипт обрабатывает только письма от доверенного отправителя (`trusted_mail`).<br>
Скрипт делает паузы между запросами, чтобы избежать блокировки со стороны Ozon.
