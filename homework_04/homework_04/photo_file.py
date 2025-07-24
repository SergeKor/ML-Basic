"""
Module: photo_file
Description:
    Класс для работы с фото файлами.
"""
from .media_file import MediaFile

class PhotoFile(MediaFile):
    # Дочерний класс
    def __init__(self, name, format, metadata, cloud = None, size = None, created_at = None, created_by = None, owner = None):
        super().__init__(name, cloud, size, created_at, created_by, owner)  # Вызов конструктора родительского класса
        self._format = format
        self.__metadata = metadata

    def create(self, name, format, metadata, cloud = None, credentials = None) -> bool:
        """
        Создаёт фотофайл определенного формата (jpeg, png, ...), заполняет аттрибуты и метаданные (автор, размер изображения, ...).
        
        Parameters
        ----------
        name : str
            Имя файла
        format : str
            Формат изображения (jpeg, png, ...)
        metadata : dict
            Метаданные (автор, координаты, качество\размер изображения, ...)
        cloud : str
            Путь в облаке
        credentials : str
            Права доступа к облаку\системе (токен или что то ещё)

        Returns
        -------
        bool
            Статус\результат создания
        """
        pass
    
    def update(self, name, new_attr, new_metadata, cloud = None, credentials = None) -> bool:
        """
        Обновляет фотофайл после редактирования
        
        Parameters
        ----------
        name : str
            Имя файла
        cloud : str
            Путь в облаке
        credentials : str
            Права доступа к облаку\системе (токен или что то ещё)
        new_attr : dict
            Новые аттрибуты файла если небходимо их обновить
        new_metadata : dict
            Новые метаданные если небходимо их обновить

        Returns
        -------
        bool
            Статус\результат обновления
        """
        pass

    def open(self, name, cloud = None, credentials = None) -> bool:
        """
        Открывает фотофайл
        
        Parameters
        ----------
        name : str
            Имя файла
        cloud : str
            Путь в облаке
        credentials : str
            Права доступа к облаку\системе (токен или что то ещё)

        Returns
        -------
        bool
            Статус\результат открытия
        """
        pass

    def save(self, name, cloud = None, credentials = None) -> bool:
        """
        Сохраняет фотофайл
        
        Parameters
        ----------
        name : str
            Имя файла
        cloud : str
            Путь в облаке
        credentials : str
            Права доступа к облаку\системе (токен или что то ещё)

        Returns
        -------
        bool
            Статус\результат сохранения
        """
        pass

    def convert(self, name, new_name, new_format: str, cloud = None, credentials = None) -> bool:
        """
        Преобразует фотофайл в новый формат
        
        Parameters
        ----------
        name : str
            Имя исходного файла
        new_name : str
            Имя сконвертированного файла
        new_format : str
            Новый формат файла
        cloud : str
            Путь в облаке
        credentials : str
            Права доступа к облаку\системе (токен или что то ещё)

        Returns
        -------
        bool
            Статус\результат конвертации
        """
        pass

    def get_metadata(self) -> dict:
        """
        Выдаёт метаданные свойственные для определенного типа медиафайлов

        Returns
        -------
        dict
            Словарь с метаданными 
        """
        return self.__metadata
