from typing import *

something_else : int = lambda x = int : x
a = something_else(1);
print(f"a is {a}")

def logging_wrapper(func: Callable):
    def new_func(*args, **kwargs):
        print(f"{func.__name__} was called with arguments: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return new_func


@logging_wrapper
def add(x: int, y: int) -> int: return x + y;
# add_with_logging_wrapper = logging_wrapper(add);
@logging_wrapper
def sub(x: int, y: int) -> int: return x - y;
# sub_with_logging_wrapper = logging_wrapper(sub);
@logging_wrapper
def mul(x: int, y: int) -> int: return x * y;
@logging_wrapper
def div(x:int, y:int) -> int: return x / y;
def mod(x: int, y: int) -> int: return x % y;
@logging_wrapper
def int_as_str(x: int) -> str: return str(x);
@logging_wrapper
def power(x:int, y: int) -> int: return x ** y;

def do_math(x : int, y : int, operation_functions: Callable):
    print(f"{operation_functions.__annotations__}");
    if(len(operation_functions.__annotations__) == 2):
        result = operation_functions(x);
    else:
        result = operation_functions(x, y);
    return result;

op = "plus";
x = 2;
y = 2;

op_map = {
    "plus": add,
    "minus": sub,
    "mul": mul,
    "div": div,
    "mod": mod,
    "power": power,
    "str": int_as_str
}


result = do_math(x, y, op_map[op]);
print(f"result is {result}");

op = "minus"
result = do_math(x, y, op_map[op]);
print(f"result is {result}");
