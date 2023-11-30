## EN

### Master Thesis Project on the impact of analyzing the communication of ordinary investors during herd events on trading.  

#### Objective
Based on the data on the number of unique investors of the Robinhood trading application who own at least one share of the company, to analyze the sentiment of communication of ordinary investors on the r/wallstreetbets forum (www.reddit.com/r/wallstreetbets) and its impact on investor behavior.

#### Description
Input data from the Robintrack service (www.robintrack.com), which parsed the data available through the Robinhood API between 02.05.2018 and 13.08.2020, when the Robinhood API was available for scraping
Data on the number of users who own at least one item. 
Retrieved comments for analysis using PRAW (Python Reddit API Wrapper) by searching relevant company tickers, in time frames coinciding with herd events topics and comments in relevant topics. Comments were cleaned of duplicates and deleted comments, then analyzed using the sentiment-analysis package VADER augmented to analyze financial-themed posts. 
Fractions of emotional tone of comments were determined .
The impact of different comment tones on the market behavior of common investors was analyzed. 

#### Technology Stack
Python, Pandas, PRAW, VADER, Seaborn, Matplotlib

## DE

### Masterarbeit über die Auswirkungen der Analyse der Kommunikation normaler Investoren während Herden-Ereignissen auf den Handel.  

#### Zielsetzung
Basierend auf den Daten über die Anzahl der einzigartigen Investoren der Robinhood Handelsanwendung, die mindestens eine Aktie des Unternehmens besitzen, soll die Stimmung der Kommunikation von gewöhnlichen Investoren im r/wallstreetbets Forum (www.reddit.com/r/wallstreetbets) und deren Auswirkung auf das Investorenverhalten analysiert werden.

#### Beschreibung
Eingabedaten vom Robintrack-Dienst (www.robintrack.com), der die über die Robinhood-API verfügbaren Daten zwischen dem 02.05.2018 und dem 13.08.2020 analysiert hat, als die Robinhood-API zum Scraping verfügbar war
Daten über die Anzahl der Nutzer, die mindestens einen Artikel besitzen. 
Abrufen von Kommentaren für die Analyse mithilfe von PRAW (Python Reddit API Wrapper) durch Suche nach relevanten Unternehmenstickern in Zeiträumen, die mit Herdenereignisthemen und Kommentaren in relevanten Themen zusammenfallen. Die Kommentare wurden von Duplikaten und gelöschten Kommentaren bereinigt und dann mit dem Sentiment-Analysepaket VADER analysiert, das für die Analyse von Beiträgen zum Thema Finanzen erweitert wurde. 
Es wurden die Anteile des emotionalen Tons der Kommentare bestimmt.
Die Auswirkungen verschiedener Kommentartöne auf das Marktverhalten von Anlegern wurden analysiert. 

#### Technologie-Stack
Python, Pandas, PRAW, VADER, Seaborn, Matplotlib

## RU 

### Магистерская дипломная работа по влиянию анализа общения простых инвесторов во время стадных событий на торги.  

#### Задача
На основе данных о количестве уникальных инвесторов торгового приложения Robinhood, владеющих как минимум одной акцией компании проанализировать сентимент общения простых инвесторов на форуме r/wallstreetbets (www.reddit.com/r/wallstreetbets) и его влияние на поведение инвесторов.

#### Описание
Входные данные от сервиса Robintrack (www.robintrack.com), который парсил доступные через API Robinhood данные в период с 02.05.2018 по 13.08.2020, когда API Robinhood был доступен для скрэппингаданных о количестве пользователей, которые владеют хотя бы одной позицией. 
Получены комментарии для анализа с помощью PRAW (Python Reddit API Wrapper) с помощью поиска по релевантным тикерам компаний, во временных рамках совпадающих со стадных событиями тем и комментариев в соответствующих темах. Комментарии очищены от дубликатов и удаленных комментариев, после чего проанализированы с помощью пакета для сентимент - анализа VADER с дополненным для анализа сообщений на финансовую тему сообщений. 
Определены доли эмоциональной тональности комментариев .
Проанализировано влияние различных тональностей комментариев на поведение простых инвесторов на рынке. 

#### Стек технологий
Python, Pandas, PRAW, VADER, Seaborn, Matplotlib