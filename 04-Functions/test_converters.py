# test_converters.py

from converters import m_to_cm, cm_to_m, cm_to_inches, feet_and_inches_to_cm

def test_converters():
    # Test m_to_cm
    assert m_to_cm(2) == 200, "2 meters should be 200 centimeters"

    # Test cm_to_m
    assert cm_to_m(532) == 5.32, "532 centimeters should be 5.32 meters"

    # Test cm_to_inches
    assert round((cm_to_inches(532)),3) == 209.449, "532 centimeters should be approximately 209.449 inches"

    # Test feet_and_inches_to_cm
    assert round((feet_and_inches_to_cm(5, 6)),2) == 167.64, "5 feet 6 inches should be 167.64 centimeters"

    print("All tests passed!")

if __name__ == "__main__":
    test_converters()