import pytest

from src.baseclasses.response import Response
from src.schemas.user import User
from src.schemas.computer import Computer
from example import computer


@pytest.mark.skip('Need another api')
def test_getting_user_list(get_users):
    """
    In this test we are checking that response code is 200 and validate that json
     have correct type of data in every argument

    This test will be failed
    """
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.skip('[ISSUE-2412] Issue with network connection')
def test_another():
    """
    In this test we are checking that 1 == 1

    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_valur, result', [
                (1, 2, 3),
                (-1, -2, -3),
                (-1, 2, 1),
                ('b', -2, None),
                ('b', 'b', None)
            ])
def test_calculator(first_value, second_valur, result, calculate):
    """
    In this test we give positive and negative parameters and checking how calculator take it
    """
    assert calculate(first_value, second_valur) == result


def test_pydantic_object():
    comp = Computer.model_validate(computer)
    print(comp.detailed_info.physical.color.as_rgb())

