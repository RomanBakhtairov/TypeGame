# Как работает игра?
> Всё просто - запускаешь файл game.py и наблюдаешь как поехали шрифты!
Если игра не понравилась - жми esc
# Разбор кода для ценителей:
Главный класс - game, в его конструкторе запускаются основные настройки + бесконечный цикл игры

>В общем я хотел сделать удобную систему с разделением сцен и т.п, для чего создал класс Scene (он лежит в файле scenes py)
> Этот класс Имеет только 3 метода Update, Start, 
> To_Next_Scene и конструктор. Update будет запускаться 
>каждый цикл класса game для текущей сцены (current
>scene), метод start же запустится только в начале
>Внутри них можно напрямую писать код для каждой сцены.

Класс scene пользуется объектами класса GameObject по простому - координаты и картинка. 
# важное замечание. Если добавишь объекты GameObject(или его наследников) в переменную self.objects, то объект начнёт отрисовываться или даже выполнять какие то дейсвия!

Короче, в сыром виде я его не использую, класс сцены наследуется другими, в котороых уже и происходит вся магия. Именно в файлах game_scene.py и open_scene.py это и происходит. Наследуем -> перегружаем -> Всё работает. 
Если во время игры нужно переключить сцену, то можно внутри объекта Scene дернуть переключатель self.TriggerFlag. Тогда игра переключиться на сцену, которая была создана после этой( т.е порядок создания сцен важен!)
#Продолжение следует...