"""
Module: media_file
Description:
    MediaFile - абстрактный класс для всех типов медиафайлов с набором методов которые должны быть реализованы в дочерних классах.
    Включены атрибуты общие для всех типов медиафайлов.
"""
from abc import ABC, abstractmethod

class MediaFile(ABC):

    def __init__(self, name, cloud = None, size = None, created_at = None, created_by = None, owner = None):
        self._name = name
        self._cloud = cloud
        self._size = size
        self._created_at = created_at
        self._created_by = created_by
        self._owner = owner

    def get_attr(self):
        """
        Выдаёт общие аттрибуты свойственные для любых файлов

        Returns
        -------
        dict
            Словарь с аттрибутами name, cloud, size, created_at, created_by, owner 
        """
        return dict(name=self._name, cloud = self._cloud, size = self._size, created_at = self._created_at, created_by = self._created_by, owner = self._owner)

    def read_attr_from_file_system(self):
        """
        Читает общие аттрибуты свойственные для любых файлов из файловой системы 
        и заполняет size, created_at, created_by, owner 
        """
        pass

    @abstractmethod
    def create(self, name, cloud = None, credentials = None) -> bool:
        """
        Создаёт медиафайл и заполняет общие аттрибуты.         
        
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
            Статус\результат создания
        """
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")
    
    @abstractmethod
    def update(self, name, new_attr, cloud = None, credentials = None, new_metadata = None) -> bool:
        """
        Обновляет медиафайл новыми аттрибутами и метаданными
        
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
            Новые метаданные присущие медиафайлу, например: автор, продолжительность, формат изображения, ...

        Returns
        -------
        bool
            Статус\результат обновления
        """
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")

    def delete(self, name, cloud = None, credentials = None) -> bool:
        """
        Удаляет медиафайл.
        Этот метод может быть реализован здесь т.к. удаления одинаковая для всех медиафалов операция
        
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
            Статус\результат удаления
        """
        pass

    @abstractmethod
    def open(self, name, cloud = None, credentials = None) -> bool:
        """
        Открывает медиафайл
        
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
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")

    @abstractmethod
    def save(self, name, cloud = None, credentials = None) -> bool:
        """
        Сохраняет медиафайл
        
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
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")

    @abstractmethod
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
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")

    @abstractmethod
    def get_metadata(self) -> dict:
        """
        Выдаёт метаданные свойственные для определенного типа медиафайлов

        Returns
        -------
        dict
            Словарь с метаданными 
        """
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")