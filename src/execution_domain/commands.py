from dataclasses import dataclass
from .enums import Side, OrderType, TimeInForce
from .value_objects import Symbol, Quantity, Price

@dataclass(frozen=True)
class SubmitOrder:
    symbol: Symbol
    side: Side
    order_type: OrderType
    quantity: Quantity
    price: Price | None = None
    time_in_force: TimeInForce = TimeInForce.GTC
    venue: str | None = None