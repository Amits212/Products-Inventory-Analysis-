from pydantic import BaseModel
from typing import Dict
from datetime import datetime


class Product(BaseModel):
    name: str
    description: str
    quantity: int
    analysis: Dict[str, dict] = {}

    def subtract_from_quantity(self, quantity: int):
        self.quantity -= quantity

    def save_analysis(self, time: str, quantity: int):
        self.analysis[time] = {
            "Purchase Quantity": quantity,
            "Quantity After Purchase": self.quantity
        }

