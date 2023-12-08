
### sleep_in

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in( False, False )-> True
sleep_in( True, False )-> False
sleep_in( False, True )-> True

```python
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

```

### monkey_trouble

We have two monkeys, a and b. The parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither is smiling. Return True if we are in trouble.


```python
def monkey_trouble(a_smile, b_smile):
    if (not a_smile and not b_smile) or (a_smile and b_smile):
        return True
    else:
        return False

```

### sum_double

Given two into values, return their sum. Unless the two values are the same, then return double their sum.
```python
def sum_double(a, b):
  if (a !=b):
   return (a + b)
  else:
     return 2 * (a + b) #note: the multiplication has to be explicit (the *)
     
```
<strong>Another version:</strong>

```python
def sum_double(a, b):
    #store the sum in a local variable
    sum = a + b

    #double it if integers are same
    if a == b:
        sum = sum * 2
    return sum

```


### diff 21

Given an int `n`, return the absolute difference between `n` and 21, except return double the absolute difference if `n` is over 21.

```python
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

```
<strong>Another version:</strong>

```python
def diff21(n):
    difference = 21 - n
    if n < 21:
        return abs(difference)
    else:
        return 2 * abs(difference)
```


### parrot_trouble

We have a loud talking parrot. The "hour" parameter is the current hour in the range 0..23. We are in trouble if the parrot is talking and hte hour is before 7 or after 20. Return True if we are in trouble.

```python
def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else:
        return False

```

<strong>Another version:</strong>

```python
def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))

```


###