from functools import cached_property

from .base_logic import BaseLogic
from .received_logic import ReceivedLogicMixin
from ..stardew_rule import StardewRule
from ..strings.wallet_item_names import Wallet


class WalletLogicMixin(BaseLogic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wallet = WalletLogic(*args, **kwargs)


class WalletLogic(ReceivedLogicMixin):
    @cached_property
    def can_speak_dwarf(self) -> StardewRule:
        return self.received(Wallet.dwarvish_translation_guide)

    @cached_property
    def has_rusty_key(self) -> StardewRule:
        return self.received(Wallet.rusty_key)
