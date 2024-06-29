from dataclasses import dataclass


@dataclass
class Settings:
    """General config file with defaults for the game."""
    user: str = "default"
    scale: str = "C"
    issharp: bool = False
    isminor: bool = False
    tempo: int = 60
    midi: bool = False
    ledger_lines: int = 0
