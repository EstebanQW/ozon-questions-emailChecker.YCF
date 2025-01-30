# Для функции answer_question
COMPANY_ID = "123456"  # id компании, можно посмотреть на странице компании (например https://www.ozon.ru/seller/ooo-mebelnaya-fabrika-volzhanka-1234/products/?miniapp=seller_1234 - id компании 1234)

# Параметры для подключения к почтовому серверу
IMAP_SERVER = "imap.mail.ru"
IMAP_USERNAME = (
    "example1@mail.ru"  # Почта, которую необходимо проверять на входящие письма
)
IMAP_PASSWORD = "password"  # Пароль от почты для сторонних приложений
TRUSTED_MAIL = "<example2@mail.ru>"  # Почта, с которой будут поступать письма, при заполнении переменной важно соблюдать регистр символов. Т.к. могут возникать ошибки <exaMple2@mail.ru> не то же самое, что <eXample2@mail.ru>

# Для функции read_cookie_bucket
BUCKET_NAME = "name"  # Название бакета
FILE_NAME = "name.txt"  # Название файла с куки в бакете
AWS_ACCESS_KEY_ID = "key-id"  # key id для доступа в бакет
AWS_SECRET_ACCESS_KEY = "key"  # key для доступа в бакет
REGION = "region"  # регион, обычно "ru-central1"
