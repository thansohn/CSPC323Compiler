from enum import Enum
from collections import namedtuple

TokenRecord = namedtuple("TokenRecord", "lexeme, token")

#token types
class LexerToken(Enum):
    KEYWORD = 1,
    OPERATOR = 2,
    SEPERATOR = 3,
    INTEGER = 4,
    REAL = 5,
    IDENTIFIER = 6,
    INVALID = 7,

#states
class LexerState(Enum):
    START = 0,
    INTEGER = 1,
    REAL = 2,
    ALPHABETIC = 3,
    OPERATOR = 4,
    COMMENT = 5,
    INVALID = 6

class Constants(object):
    VALID_OPERATORS = ["+", "-", "=", "*", "/", "%", "<", ">"]
    VALID_SEPERATORS = ["(", ")", "[", "]", "{", "}", ",", ";", "'", ".", ":"]
    
    VALID_KEYWORDS = ["int", "float", "bool", "if", "else", "then", "do", "while", "whileend", "do", 
                    "doend", "for", "and", "or", "function"]

    VALID_IDENTIFIER_SYMBOLS = ["$"]

    DECIMAL = '.'
    COMMENT_START = "!"
    COMMENT_END = "!"
    


