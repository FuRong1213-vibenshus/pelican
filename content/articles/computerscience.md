Title: Computer Architecture
Author: Rong
Date: 2024-11-09
Tags: computer architecture, binary

## Objective 
+ What is computer (system)
    + History
+ Mordern computer system
    + Hardware, software
    + Basis of the Von Newmann Architecture
    + Key features of the fundamental design
    + Binary, Hexadecimal and decimal number system

## Videos and Reading Materials 
+ [Von Neumann Machine](https://www.britannica.com/technology/von-Neumann-machine)
+ [Computer architecture](https://www.youtube.com/watch?v=ckDb_W72__c&list=PLyHlkAMBPa9YsoSFSqZF7si5KH0nStEnH&index=2)
+ [System Bus](https://www.youtube.com/watch?v=alYwqzO6ZEQ)


## Binary and Hexadecimal
+ Python program to convert decimal to binary
```python  
# Function to convert Decimal number 
# to Binary number 
def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
  
# Driver code 
if __name__ == '__main__': 
    print(decimalToBinary(8)) 
    print(decimalToBinary(18)) 
    print(decimalToBinary(7)) 

```
+ Bitwise operator
```python
def dec2bin(number: int):
    ans = ""
    if ( number == 0 ):
        return 0
    while ( number ):
        ans += str(number&1)
        number = number >> 1
    
    ans = ans[::-1]

    return ans 
```
+ Python program to convert binary to hexadecimal

```python
def binToHexa(n):
  
    # convert binary to int
    num = int(n, 2)
    
    # convert int to hexadecimal
    hex_num = hex(num)
    return(hex_num)
```

## Further reading
[Computer number system](https://www.tutorialspoint.com/basics_of_computers/basics_of_computers_number_system.htm) 

## Do it yourself

+ Convert
    + Convert the hexadecimal number “1A” to decimal.
    + Change hexadecimal to decimal for the value “2F.”
    + How to change hex to decimal for the hexadecimal number “FFFF”?
    + How do you convert hex to decimal for the value “4A5”?
    + Convert the value “AA” from hexadecimal to decimal and then to binary.
+ Convert Decimal to Binary in Python Using While Loop, without using bin(), following these steps. 
    + Initialize an empty list to store binary digits.
    + Use a while loop to divide the number by 2 repeatedly.
    + Insert the remainder (either 0 or 1) at the beginning of the list.
    + Convert the list of characters back to a string.
+ Convert binary to hexadecimal in python (hint: function hex())? 

