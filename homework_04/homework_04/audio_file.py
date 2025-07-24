"""
Module: audio_file
Description:
    Класс для работы со звуковыми файлами.
"""
from .media_file import MediaFile

class AudioFile(MediaFile):
    # Дочерний класс
    def __init__(self, name, format, metadata, cloud = None, size = None, created_at = None, created_by = None, owner = None):
        super().__init__(name, cloud, size, created_at, created_by, owner)  # Вызов конструктора родительского класса
        self._format = format
        self.__metadata = metadata

    def create(self, name, format, metadata, cloud = None, credentials = None) -> bool:
        """
        Создаёт аудифайл определенного формата (mp3, wav, ...), заполняет атрибуты и метаданные (автор, продолжительность, ...).
        
        Parameters
        ----------
        name : str
            Имя файла
        format : str
            Формат для аудиофайла (mp3, wav, ...)
        metadata : dict
            Метаданные (автор, продолжительность, ...)
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
        Обновляет аудиофайл после редактирования
        
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
        Открывает аудиофайл
        
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
        Сохраняет аудиофайл
        
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
        Преобразует медиафайл в новый формат
        
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
