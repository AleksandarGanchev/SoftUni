from typing import List

from project import Category
from project import Document
from project import Topic


class Storage:
    def __init__(self):
        self.categories: List = []
        self.topics: List = []
        self.documents: List = []

    @staticmethod
    def add_object(obj, collection):
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def get_object(searched_value, attr: str, collection: list):
        for obj in collection:
            if getattr(obj, attr) == searched_value:
                return obj

    def edit_object(self, id, collection,  *args):
        obj = self.get_object(id, "id", collection)
        obj.edit(*args)

    def delete_object(self, id, collection):
        obj = self.get_object(id, "id", collection)
        collection.remove(obj)

    def add_category(self, category: Category):
        self.add_object(category, self.categories)

    def add_topic(self, topic: Topic):
        self.add_object(topic, self.topics)

    def add_document(self, document: Document):
        self.add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete_object(document_id, self.documents)

    def get_document(self, document_id):
        return self.get_object(document_id,"id", self.documents)

    def __repr__(self):
        return '\n'.join(doc.__repr__() for doc in self.documents)














