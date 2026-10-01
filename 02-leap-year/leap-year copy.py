
def leap_year(year):
    return False

def verify_leap_year(year, expectedResult):
    actualResult = leap_year(year)
    if actualResult != expectedResult:
        print("Zastřelit Honzíka, protože špatně určil přestupnost roku %i" % year)

verify_leap_year(2010, False)
verify_leap_year(2012, True)
verify_leap_year(1981, False)
verify_leap_year(2000, True)
verify_leap_year(1900, False)
verify_leap_year(1800, False)
verify_leap_year(1700, False)
verify_leap_year(1600, True)
verify_leap_year(1300, False)
verify_leap_year(1200, True)