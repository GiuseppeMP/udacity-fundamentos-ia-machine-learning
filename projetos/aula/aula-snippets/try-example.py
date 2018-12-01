try:
    print("try")
except ValueError:
    print("valueError")
except KeyboardInterrupt:
    print("KeyboardInterrupt")


try:
    print("try2")
except ( ValueError, KeyboardInterrupt ):
    print("ValueError, KeyboardInterrupt")
