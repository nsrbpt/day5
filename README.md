

Emergency Resource Dispatch Analyzer

 About the Program

This program analyzes emergency resource requests given during a disaster drill. 
The user enters multiple request values, and the program classifies them as low, moderate, high, or invalid based on predefined conditions.

How It Works

All requests are stored in a list and processed using a loop. After classification, 
the program calculates the length of the user’s full name (excluding spaces) and finds the PLI value (L % 3). 
Based on this value, a specific demand category is removed from the final report.

What the Output Shows

The program displays the name length, PLI value, applied rule, total valid requests, number of removed requests, and 
the final categorized lists. This helped me better understand lists, loops, and conditional logic in Python.
