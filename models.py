from typing import List, TypedDict


class Transaction(TypedDict):
    sender: str
    recipient: str
    amount: str


class Block(TypedDict):
    index: int
    timestamp: float
    transactions: List[Transaction]
    proof: int
    previous_hash: str
