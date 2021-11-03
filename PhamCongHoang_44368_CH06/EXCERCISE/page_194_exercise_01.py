"""
Author: pham cong hoang
Date: 22/10/2021
Problem:Where are module variables, parameters, and temporary variables introduced and
initialized in a program?
Solution:
TEMPORARY VARIABLES :

INTRODUCED : inside a block, they have very short lifetime and hold data that can be discarded or is later stored in a permanent variable

INITIALIZED : temporary variables can be initialized anywhere inside the block where they are declared.

PARAMETERS:

INTRODUCED : parameters are declared inside the parenthesis of the function definition

INITIALIZED : parameters can be initialized where they are declared or can be declared in the parenthesis of the function call

MODULE VARIABLE :

INTRODUCED : A module-level variable is declared for a particular module. It is available to all procedures within that module but not to the rest of the application. Module-level variables remain in existence for the lifetime of the application and preserve their values.

INITIALIZED : module variable gets initialized where they are declared inside the module. it is initialized to 0 by default.

"""