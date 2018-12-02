"""
Author: Jose Pablo Murillo
File: homework1
Description: Use of if clause
Last update: 01/12/2018
Python version 3.6.4
"""

#Exercise 1
def miniCalculator(number1: int, number2: int, operation: str) -> int:
    """
    Inputs: first number, second number, operation code
    Output: arithmetic operation result or error
    Process: If for every specified operator, and do the
        corresponding operation
    Restrictions: First two parameters must be integers
    and third must be string
    """
    if (operation == '+'):
        return number1 + number2
    elif (operation == '-'):
        return number1 - number2
    elif (operation == '*'):
        return number1 * number2
    elif (operation == '/'):
        if (number2 != 0):
            return number1 // number2
        else:
            return "Error: cannot divide by 0"
    else:
        return "Error: operation not available, must be +, -, / or *"



#Exercise 2
def isLeap(year: int) -> bool:
    """
    Inputs: a year
    Output: boolean or error
    Process: Determines if year is a leap year by checking if the year is
    divisible by 4
    Restrictions: year must be an integer, year must be >= 2000 and have 4 digits
    """
    if (year < 2000 or year > 9999):
        return "Error: year not in permitted range"
    else:
        return (year % 4 == 0)



#Execise 3
def dateValid(date: int) -> bool:
    """
    Inputs: a date as int with format ddmmaaaa
    Output: boolean
    Process: the date is broken down into separate components day, month and year
    and performs the validation acording to the provided restrictions
    Restrictions: date must be int
    year must be >= 1900
    month must be between 1 and 12
    february has 29 days if year is leap, else it has 28
    january, march, may, july, august, october and december have 31 days
    april, june, september and november have 30 days
    """
    year:int = date % 10000
    date = date // 10000
    month:int = date % 100
    day:int = date // 100

    if (year >= 1900):
        if (month >= 1 and month <= 12):
            if (month == 2):
                if (isLeap(year)):
                    if (day >= 1 and day <= 29):
                        return True
                else:
                    if (day >= 1 and day <= 28):
                        return True
            else:
                if (month == 1 or month == 3 or month == 5 or month == 7 \
                    or month == 8 or month == 10 or month == 12):
                    if (day >= 1 and day <= 31):
                        return True
                else:
                    if (month == 4 or month == 9 or month == 11):
                        if (day >= 1 and day <= 30):
                            return True
    return False



#Exercise 4
def dateAsWords(date: int) -> str:
    """
    Inputs: date as int in format ddmmaaaa
    Output: Date as words or boolean
    Process: date is validated and then an if is done for the month to return the
    corresponding one in words
    Restrictions: date must be int
    """
    if (dateValid(date)):
        year:int = date % 10000
        date = date // 10000
        month:int = date % 100
        day:int = date // 100
        strMonth:str = ""
        if (month == 1):
            strMonth = "january"
        if (month == 2):
            strMonth = "february"
        if (month == 3):
            strMonth = "march"
        if (month == 4):
            strMonth = "april"
        if (month == 5):
            strMonth = "may"
        if (month == 6):
            strMonth = "june"
        if (month == 7):
            strMonth = "july"
        if (month == 8):
            strMonth = "august"
        if (month == 9):
            strMonth = "september"
        if (month == 10):
            strMonth = "october"
        if (month == 11):
            strMonth = "november"
        if (month == 12):
            strMonth = "december"
        return str(day) + " of " + strMonth + " " + str(year)
    else:
        return False



#Exercise 5
def deleteDigit(digit: int, number: int) -> int:
    """
    Inputs: a digit and a number 
    Output: number without the specified digit
    Process: the four digits are extracted from the number and then are added
    to the result if they are different than the digit we want to delete
    Restrictions: digit is between 0 and 9
    number must be positive and have four digits
    """
    numberRestriction:bool = (number >= 1000 and number <= 9999)
    digitRestriction:bool = (digit >= 0 and digit <= 9)
    errorMessage: str = ""

    if (not numberRestriction):
        errorMessage = "Error in number"

    if (not digitRestriction):
        if (errorMessage == ""):
            errorMessage = "Error in digit"
        else:
            errorMessage = errorMessage + " and in digit"
    if (errorMessage != ""):
            return errorMessage
    else:
        firstDigit = number // 1000
        number = number % 1000
        secondDigit = number // 100
        number = number % 100
        thirdDigit = number // 10
        fourthDigit = number % 10

        if (firstDigit == digit):
            firstDigit = 0
        if (secondDigit == digit):
            secondDigit = 0
        if (thirdDigit == digit):
            thirdDigit = 0
        if (fourthDigit == digit):
            fourthDigit = 0

        return firstDigit * 1000 + secondDigit * 100 + \
               thirdDigit * 10 + fourthDigit



#Exercise 6
def convertSeconds(seconds: int, unit: str) -> float:
    """
    Inputs: an amount of seconds and a unit of time
    Output: The amount of seconds converted into the unit specified
    Process: amount of seconds is divided according to corresposponding unit
    Restrictions: amount of seconds must be integer and unit of time
    must be: 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months'
    """
    errorMessage: str = ""
    if (seconds < 0):
        errorMessage = "Error in number"
        return errorMessage

    if (unit == "seconds"):
        return seconds
    if (unit == "minutes"):
        return seconds / 60
    if (unit == "hours"):
        return seconds / 3600
    if (unit == "days"):
        return seconds / 86400
    if (unit == "weeks"):
        return seconds / 604800
    if (unit == "months"):
        return seconds / 2628000

    if (errorMessage == ""):
        errorMessage = "Error in unit"
    else:
        errorMessage = errorMessage + " and in unit"
    return errorMessage

#exercise 7
def digitsInCommon(firstNumber: int, secondNumber: int) -> int:
    """
    Inputs: two integers between 1 and 999
    Outputs: a number composed of the digits in common
    Process: each number is broken down to its 3 digits, a check is done if
    any number digit matches the digit we are looking for
    Restrictions: numbers must be integers between 1 and 999
    """
    error = ""
    if (firstNumber < 1 or firstNumber > 999):
        error =  "Error in first number"

    if (secondNumber < 1 or secondNumber > 999):
        if (error == ""):
            error = "Error in second number"
        else:
            error = error + " and in second number"
    if (error != ""):
        return error
    else:
        firstNumberUnits = firstNumber % 10
        secondNumberUnits = secondNumber % 10

        firstNumberTens = (firstNumber // 10) % 10
        secondNumberTens = (secondNumber // 10) % 10

        firstNumberHundred = (firstNumber // 100)
        secondNumberHundred = (secondNumber // 100)

        result = 0
        if ((firstNumberUnits == 1 or firstNumberTens == 1 or firstNumberHundred == 1)\
            and (secondNumberUnits == 1 or secondNumberTens == 1 or secondNumberHundred == 1)):
            result = result * 10 + 1

        if ((firstNumberUnits == 2 or firstNumberTens == 2 or firstNumberHundred == 2)\
            and (secondNumberUnits == 2 or secondNumberTens == 2 or secondNumberHundred == 2)):
            result = result * 10 + 2

        if ((firstNumberUnits == 3 or firstNumberTens == 3 or firstNumberHundred == 3)\
            and (secondNumberUnits == 3 or secondNumberTens == 3 or secondNumberHundred == 3)):
            result = result * 10 + 3

        if ((firstNumberUnits == 4 or firstNumberTens == 4 or firstNumberHundred == 4)\
            and (secondNumberUnits == 4 or secondNumberTens == 4 or secondNumberHundred == 4)):
            result = result * 10 + 4

        if ((firstNumberUnits == 5 or firstNumberTens == 5 or firstNumberHundred == 5)\
            and (secondNumberUnits == 5 or secondNumberTens == 5 or secondNumberHundred == 5)):
            result = result * 10 + 5

        if ((firstNumberUnits == 6 or firstNumberTens == 6 or firstNumberHundred == 6)\
            and (secondNumberUnits == 6 or secondNumberTens == 6 or secondNumberHundred == 6)):
            result = result * 10 + 6

        if ((firstNumberUnits == 7 or firstNumberTens == 7 or firstNumberHundred == 7)\
            and (secondNumberUnits == 7 or secondNumberTens == 7 or secondNumberHundred == 7)):
            result = result * 10 + 7

        if ((firstNumberUnits == 8 or firstNumberTens == 8 or firstNumberHundred == 8)\
            and (secondNumberUnits == 8 or secondNumberTens == 8 or secondNumberHundred == 8)):
            result = result * 10 + 8

        if ((firstNumberUnits == 9 or firstNumberTens == 9 or firstNumberHundred == 9)\
            and (secondNumberUnits == 9 or secondNumberTens == 9 or secondNumberHundred == 9)):
            result = result * 10 + 9

        if ((firstNumberUnits == 0 or firstNumberTens == 0 or firstNumberHundred == 0)\
            and (secondNumberUnits == 0 or secondNumberTens == 0 or secondNumberHundred == 0)):
            result = result * 10
        if (result == 0):
            return False
        else:
            return result



#Exercise 8

def doubleOfOdd(number: int) -> bool:
    """
    Inputs:a number
    Outputs:a boolean
    Process:Returns true if it is the double of an odd number (remainder != 0)
    Restrictions:Number must be positive integer
    """
    return (number / 2) % 2 == 1



#Exercise 9

def reforestation(hectars: int) -> int:
    """
    Inputs: the quantity of hectars for reforestation (1 hectar = 10K m2)
    Outputs: The amount of pines, eucaliptus and cedar that are going to be planted
    Process: The surface available for each plant is calculated according
    to the queantity of hectars.
    The amount of plants that can be placed is calculated based on the surface
        available
    Restrictions:
    Amount of hectar must be positive integer
    if the area of reforestation is < 100000
        50% of the surface will be for pines
        30% of the surface will be for eucaliptus
        20% of the surface will be for cedar

    if the area of reforestation is >= 100000
        40% of the surface will be for pines
        25% of the surface will be for eucaliptus
        35% of the surface will be for cedar

    in 10 m^2 there can be 8 pines
    in 15 m^2 there can be 15 eucaliptus
    in 18 m^2 there can be 10 cedars
"""
    if (hectars < 0):
        return "Error in amount of hectars"
    else:
        amountInMeters = hectars * 10000
        percentForPines = 0
        percentForEucaliptus = 0
        percentForCedar = 0
        if (amountInMeters < 100000):
            percentForPines = 0.5
            percentForEucaliptus = 0.3
            percentForCedar = 0.2
        else:
            percentForPines = 0.4
            percentForEucaliptus = 0.25
            percentForCedar = 0.35

        surfaceForPines = amountInMeters * percentForPines
        surfaceForEucaliptus = amountInMeters * percentForEucaliptus
        surfaceForCedar = amountInMeters * percentForCedar

        pines = surfaceForPines // 10
        eucaliptus = surfaceForEucaliptus // 15
        cedars = surfaceForCedar // 18

        return pines, eucaliptus, cedars



#Exercise 10

def bankAccount(credit: int, operation: int, amount: int) -> bool:
    """
    Inputs:The current amount of credit, type of operation, amount for operation
    Outputs:Boolean for transacaction if it is possible
    Process: Data is verfified according to restrictions and operation type
    Amount is added or subtracted to credit
    Restrictions:credit must be positive integer, type of operation must be 1 or 2,
    amount for operation must be positive integer
    """
    if (amount <= 0):
        print("Error in amount for operation")
        return False
    else:
        if (credit < 0):
            print("Error in credit")
            return False
        else:
            if operation == 1:
                #deposit
                return True
            else:
                if operation == 2:
                    if (credit < amount):
                        print("Error insufficient credit")
                        return False
                    else:
                        return True
                else:
                    print("Invalid operation")
                    return False



#Exercise 11
def breakDown(amount: int) -> None:
    """
    Inputs: an amount of CRC (colones)
    Outputs: breakdown of corresponding bill presentations with the minimum amount
    Process: The amount is first broken down with the highest presentations and
    then is reduced to the remainder so that it is used for the calculation of the
    other presentations through division
    Restrictions:amount must be positive integer multiple of 5000
    Available presentations: 50000, 20000, 10000, 5000
    """

    if (amount < 0):
        return "Error in amount"
    else:
        amount50K = amount // 50000
        amount = amount % 50000
        amount20K = amount // 20000
        amount = amount % 20000
        amount10K = amount // 10000
        amount = amount % 10000
        amount5K = amount // 5000
        print("Bill breakdown:")
        if (amount50K > 0):
            print(str(amount50K) + " of 50,000\t" + str(50000 * amount50K))
        if (amount20K > 0):
            print(str(amount20K) + " of 20,000\t" + str(20000 * amount20K))
        if (amount10K > 0):
            print(str(amount10K) + " of 10,000\t" + str(10000 * amount10K))
        if (amount5K > 0):
            print(str(amount5K) + " of 5,000\t" + str(5000 * amount5K))
        print("----------")
        print("Total breakdown: " + str(50000 * amount50K + \
                                        20000 * amount20K + \
                                        10000 * amount10K + \
                                        5000 * amount5K))



#Exercise 12
def atm(credit: int, operation: int, amount: int) -> None:
    """
    Inputs:The current amount of credit, type of operation, amount for operation
    Outputs:prints new credit and breakdown in coins
    Process: data is verified and checked if transaction is possible, if true then
        it does the breakdown of the new credit
    Restrictions:credit must be positive integer, type of operation must be 1 or 2,
        amount for operation must be positive integer and multiple of 5000
    """
    if (credit < 0):
        return "Error in credit"
    if (amount <= 0 or (amount % 5000 != 0)):
        return "Error in amount"
    if (operation != 1 and operation != 2):
        return "Error in operation"
    if (bankAccount(credit, operation, amount)):
        if (operation == 1):
            credit = credit + amount
        else:
            credit = credit - amount
        print("New credit: " + str(credit))
        print(breakDown(credit))



#Exercise 13
def payCellphone(minutesUsedForCalling: int, textsSent: int, internetPlan: int) -> float:
    """
        Inputs: minutesUsedForCalling, amount of texts sent, and type of internet plan
        Outputs: The total to pay for fee
        Process: according to the provided data, the amount is calculated 
        Restrictions:
        minutesForCalling must be positive integer
            textsSEnt must be positive integer
            internetPlan must be one digit integer
            Basic fee is 2750
                includes 60 minutes, minimum that must be payed
            if more than 60 minutes and less than 121 pays base + 50 * additional minutes
            after 60
            if more than 120 minutes pays base + 60 minutes at 50 + 35 * additional minutes
            after 120

            cost per textMessage is 3
            Internet:
                0 : no use of internet
                1 : 12000
                2 : 15000
                3 : 25000
            include 13% for taxes and 200 for Red Cross
    """
    if (minutesUsedForCalling < 0):
        return "Error in minutes used for calling"
        
    if (textsSent < 0):
        return "Error in text sent"
    if (internetPlan != 0 and internetPlan != 1 and internetPlan != 2 and\
        internetPlan != 3):
        return "Error in internet plan"
    else:
        baseFee = 2750
        #minutes
        if (minutesUsedForCalling >= 60 and minutesUsedForCalling < 121):
            additionalMinutes = minutesUsedForCalling - 60
            baseFee = baseFee + 50 * additionalMinutes
        if (minutesUsedForCalling > 120):
            baseFee = baseFee + 50
            additionalMinutes = minutesUsedForCalling - 120
            baseFee = baseFee + 35 * additionalMinutes

        #text messages
        baseFee = baseFee + 3 * textsSent

        #internet
        if (internetPlan == 1):
            baseFee = baseFee + 12000
        if (internetPlan == 2):
            baseFee = baseFee + 15000
        if (internetPlan == 3):
            baseFee = baseFee + 25000
        #taxes
        taxes = baseFee * 0.13
        baseFee = baseFee + taxes
        #red cross
        baseFee = baseFee + 200
        return baseFee



#Exercise 14
def evenOdd(number: int) -> tuple:
    """
    Inputs:A number
    Outputs:the even digits and odd digits than appear in the number
    Process:A division is done to get all four digits if the number is still
        greater than 0 when diving, the digits are then added to the results
    Restrictions:number must be between 0 and 9999
    """
    if (number < 0 or number > 9999):
         return "Error in number"
    else:
        unitDigit = -1
        tenDigit = -1
        hundredDigit = -1
        thousandDigit = -1
        even = -1
        odd = 0
        if (number >= 0):
            unitDigit = number % 10
            number = number // 10
        if (number > 0):
            tenDigit = number % 10
            number = number // 10
        if (number > 0):
            hundredDigit = number % 10
            number = number // 10
        if (number > 0):
            thousandDigit = number % 10

        if (unitDigit != -1):
            if (unitDigit % 2 == 0):
                even = unitDigit
            else:
                odd = unitDigit

        if (tenDigit != -1):
            if (tenDigit % 2 == 0):
                if (even == -1):
                    even = tenDigit
                else:
                    if (even == 0):
                        even = tenDigit * 10
                    else:
                        even = even * 10
                        even =  even + tenDigit
            else:
                odd = odd * 10
                odd = odd + tenDigit

        if (hundredDigit != -1):
            if (hundredDigit % 2 == 0):
                if (even == -1):
                    even = hundredDigit
                else:
                    if (even == 0):
                        even = hundredDigit * 10
                    else:
                        even = even * 10
                        even = even + hundredDigit
            else:
                odd = odd * 10
                odd = odd + hundredDigit

        if (thousandDigit != -1):
            if (thousandDigit % 2 == 0):
                if (even == -1):
                    even = thousandDigit
                else:
                    if (even == 0):
                        even = thousandDigit * 10
                    else:
                        even = even * 10
                        even = even + thousandDigit
            else:
                odd = odd * 10
                odd = odd + hundredDigit

        if (even == -1):
            return ("none", odd)

        if (odd == -1):
            return (even, "none")

        return (even, odd)



#Exercise 15
def ascendingOrder(a: int, b: int, c: int) -> tuple:
    """
    Inputs: Three integer numbers
    Outputs:A tuple with numbers in ascending order
    Process:The first pair is compared and then the lower is compared with the third
    Restrictions: Inputs must be numbers
    """
    if (a < b):
        greatest = b
        lowest = a
    else:
        greatest = a
        lowest = b
        
    if (c <= lowest):
        return (c, lowest, greatest)
    else:
        if (c <= greatest):
            return (lowest, c, greatest)
        else:
            return (lowest, greatest, c)



#Execirse 16
def descendingOrder(a: int, b: int, c: int) -> tuple:
    """
    Inputs: Three integer numbers
    Outputs:A tuple with numbers in descending order
    Process:The first pair is compared and then the lowest is compared with the third
    Restrictions: Inputs must be numbers
    """
    if (a < b):
        greatest = b
        lowest = a
    else:
        greatest = a
        lowest = b
        
    if (c <= lowest):
        return (greatest, lowest, c)
    else:
        if (c <= greatest):
            return (greatest, c, lowest)
        else:
            return (c, greatest, lowest)
    
        
            
       
        
            
        
            
    
