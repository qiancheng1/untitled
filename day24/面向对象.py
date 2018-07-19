class Chinese(object):
    party="gcd"

    def cha_dui():
        print("insert into queue")

    def chi_fan(self):
        print("chi,le,yicun,fan")


print(Chinese.__dict__["party"])
# print(Chinese.__dir__(Chinese))
# print(Chinese.__dict__["chi_fan"])
print(Chinese.__dict__)
Chinese.__dict__["cha_dui"]()
