def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('pin')}")

shipping_address("Ram", "deepak", "Mr.",
                 street = "ayyappa nagar",
                 city = "JPT",
                 state ="A.P",
                 pin = "521175")