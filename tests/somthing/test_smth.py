import pytest
from src.generators.player_localization import PlayerLocalization

@pytest.mark.parametrize("status, balance, number",
[
    ("Asctive", 100, 1),
    ("Inactive", -9, 2),
    ("Deleted", 234, 3),
    ("Banned", 1000, 4)
])
def test_smth(status, balance, number, get_player_generator):
    print(get_player_generator.set_status(status).set_balance(balance).build())
    print(get_player_generator.update_inner_generator("localize", PlayerLocalization("fr_FR").set_number(number)).build())
