from dataclasses import dataclass

@dataclass(frozen=True)
class Symbol:
    value: str

@dataclass(frozen=True)
class Quantity:
    value: float
    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Quantity must be > 0")

@dataclass(frozen=True)
class Price:
    value: float
    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Price must be > 0")