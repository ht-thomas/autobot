from ..objects import BaseObject, PhotoSize, MessageEntity, User, Animation
from typing import Optional

class Game(BaseObject):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    https://core.telegram.org/bots/api#game

    Args:
        `title (str)`: Title of the game

        `description (str)`: Description of the game

        `photo (list[PhotoSize])`: Photo that will be displayed in the game message in chats.

        `text (Optional[str])`: Optional. Brief description of the game or high scores included in the game message. 
        Can be automatically edited to include current high scores for the game when the bot calls setGameScore, 
        or manually edited using `editMessageText`. 0-4096 characters.

        `text_entities (Optional[list[MessageEntity]])`: Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.

        `animation (Optional[Animation])`: Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    """
    
    __slots__ = ("title",
                "description",
                "photo",
                "text",
                "text_entities",
                "animation",
                )

    def __init__(self, title: str, description: str, photo: list[PhotoSize]) -> None:
        self.title = title
        self.description = description
        self.photo = photo
        self.text: Optional[str] = None
        self.text_entities: Optional[list[MessageEntity]] = None
        self.animation: Optional[Animation] = None


class GameHighScore(BaseObject):
    """
    This object represents one row of the high scores table for a game.
    https://core.telegram.org/bots/api#gamehighscore

    Args:
        `position (int)`: Position in high score table for the game

        `user (User)`: User

        `score (int)`: Score
    """
    
    __slots__ = ("position",
                "user",
                "score",
                )

    def __init__(self, position: int, user: User, score: int) -> None:
        self.position = position
        self.user = user
        self.score = score




        