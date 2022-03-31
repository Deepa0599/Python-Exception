

try:
    age = 18
    if age < 18:
        raise ValueError("Not eligible for vote")
    else:
        print("Eligible for vote")

except ZeroDivisionError as e:
    print("Exception occured = >" +str(e) )
except ValueError as e:
    print("Exception occured = >" +str(e) )
except:
    print("Exception occured")
else:
    print("Program executed successfully....")
finally:
    print("Harman Ltd")

