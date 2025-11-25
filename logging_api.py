import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calc(num1, num2, op):
    logging.info(f"Call: {num1} {op} {num2}")
    
    # Direct expressions
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    
    if op == "+":
        return add
    
    elif op == "-":
        return sub
    
    elif op == "*":
        return mul

    elif op == "/":
        if num2 == 0:
            logging.error("Divide by zero")
            return "error"
        div = num1 / num2
        return div
    
    else:
        logging.warning("Invalid operator")
        return "error"


# Test
print(calc(10, 5, "+"))
print(calc(10, 5, "-"))
print(calc(10, 5, "*"))
print(calc(10, 5, "/"))
print(calc(10, 0, "/"))
print(calc(10, 5, "$"))

