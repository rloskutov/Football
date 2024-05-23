from Champions import team_getter, league_getter, result_compare
import pytest

def test_team_getter():
    assert team_getter('PL') == 'It is Man City!'
def test_league_getter():
    assert league_getter('England') == 'PL'
    assert league_getter('  SPAIN  ') == 'PD'
def test_sysexit():
    with pytest.raises(SystemExit, match='Competition is not available, sorry!') as error:
        league_getter('Hogwarts')
    assert error.type == SystemExit
def test_result_compare():
    assert result_compare('It is Man City!') == 'Again!'
    assert result_compare('It is Barça!') == 'After some time! Finally!'
