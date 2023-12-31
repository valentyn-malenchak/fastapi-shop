"""Module that contains base service abstract class."""

import abc
from typing import Any

from bson import ObjectId


class BaseService(abc.ABC):
    """Base service for encapsulating business logic."""

    @abc.abstractmethod
    async def get_item_by_id(self, id_: ObjectId) -> Any:
        """Retrieves an item by its unique identifier.

        Args:
            id_ (ObjectId): The unique identifier of the item.

        Returns:
            Any: The retrieved item or None if not found.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def create_item(self, item: Any) -> Any:
        """Creates a new item.

        Args:
            item (Any): The data for the new item.

        Returns:
            Any: The created item.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def update_item_by_id(self, id_: ObjectId, item: Any) -> Any:
        """Updates an item by its unique identifier.

        Args:
            id_ (ObjectId): The unique identifier of the item.
            item (Any): Data to update item.

        Returns:
            Any: The updated item.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_item_by_id(self, id_: ObjectId) -> Any:
        """Deletes an item by its unique identifier.

        Args:
            id_ (ObjectId): The unique identifier of the item.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError
