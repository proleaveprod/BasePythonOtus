# Git official site
https://git-scm.com/downloads

# Git docs
https://git-scm.com/book/ru/v2

# gitignore
https://docs.gitignore.io/

При первом использовании Git необходимо представиться.  
Для этого нужно ввести в терминале 2 команды:
git config --global user.name «Ваше имя английскими буквами»  
git config --global user.email ваша почта@example.com

Основные команды Git

✦	git init – инициализация локального репозитория
✦	git status – получить информацию от git о его текущем состоянии
✦	git add – добавить файл или файлы к следующему коммиту
✦	git commit -m “message” – создание коммита.
✦	git log – вывод на экран истории всех коммитов с их хеш-кодами
✦	git checkout – переход от одного коммита к другому
✦	git checkout main – вернуться к актуальному состоянию и продолжить работу
✦	git diff – увидеть разницу между текущим файлом и закоммиченным файлом
✦	git branch new1 – создание новой ветки 


Синтаксис языка Markdown
Справочник по Markdown от Microsoft:
https://docs.microsoft.com/ru-ru/contribute/markdown-reference
 
✦	# Заголовок – выделение заголовков. Количество символов “#” задаёт уровень заголовка  (поддерживается 6 уровней).
✦	= или - – подчёркиванием этими символами (не менее 3 подряд) выделяют заголовки  первого (“=”) и второго (“-”) уровней.
✦	** Полужирное начертание** или __ Полужирное начертание__
✦	*Курсивное начертание* или _Курсивное начертание_
✦	***Полужирное курсивное начертание***
✦	~~Зачёркнутый текст~~
✦	* Строка – ненумерованные списки, символ “*” в начале строки
✦	1, 2, 3 … – нумерованные списки



ВАЖНО !!!
По паролю теперь нельзя входить.
Только по Токену
Как его получить?

Использование персонального токена доступа
Войдите в свой аккаунт на GitHub.
Перейдите в раздел "Settings" (находится в выпадающем меню, которое появляется при клике на вашем аватаре в верхнем правом углу экрана).
В левом меню выберите "Developer settings".
Затем выберите "Personal access tokens" и нажмите "Generate new token".
Укажите описание токена и выберите необходимые разрешения для него. Для клонирования репозитория обычно достаточно разрешения repo.
Нажмите "Generate token" и сохраните токен в надежном месте (его нельзя будет увидеть снова).

Теперь, при git push запросит логин и пароль
Вместо пароля вводите свой токен ;-)