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
    # print(get_player_generator.set_status(status).set_balance(balance).build())
    object_to_send = get_player_generator.update_inner_value(
        ["loc"], PlayerLocalization("fr_FR")
        .set_number(number).build()).build()
    print(object_to_send)


@pytest.mark.parametrize("localization",
[
    ("AU"),
    ("GB"),
    ("US")
])
def test_localization(localization, get_player_generator):
    # print(get_player_generator.set_status(status).set_balance(balance).build())
    object_to_send = get_player_generator.update_inner_value(
        ["localization", localization], PlayerLocalization("ru")
        .build()).build()
    print(object_to_send)


