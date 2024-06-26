from dataclasses import dataclass
from pathlib import Path, PurePath

import pygame


@dataclass
class Parameters:
    # Game Parameters
    name = "PianoHero"

    # Screen Parameters
    full_screen: bool = False
    resolution: tuple = (1280, 720)

    # Interface Parameters
    scale: float = 1

    # Appearance
    title_colour: str = "#b68f40"
    font_base_colour: str = "#d7fcd4"
    font_hover_colour: str = "White"
    padding: int = 10
    alpha: int = 10

    def __post_init__(self) -> None:
        # Assets
        # Asset path.
        self.assets = {}
        asset_path = Path("assets")
        self.assets["path"] = asset_path

        # Font path.
        font_path = Path("font.ttf")
        self.assets["font_path"] = PurePath(asset_path, font_path)

        # Background.
        background_path = "main_menu.jpg"
        comb_path = PurePath(asset_path, background_path)
        self.assets["background"] = pygame.image.load(comb_path)

        # Icon.
        icon_path = "logo_small.jpg"
        comb_path = PurePath(asset_path, icon_path)
        self.assets["icon"] = pygame.image.load(comb_path)
