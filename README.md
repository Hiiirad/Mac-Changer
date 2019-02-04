# Change Mac Address

Hi guys :)

 There are a lot of reasons to change mac address such as anonymity, sabotage in network etc.
 My program will provide a lot of options for you to change your interface(s)'s mac address.
 This program will only works on **Linux** systems.
 
> This program has a lot of versions and I will add them step by step.

> I will edit this readme file and make it better later.

> Program currently has stages 1, 2, 3, 4 (some part of it), 5.

*oui.csv file contains all of standard OUI (Organizationally Unique Identifier) part of a mac address (first half of a mac address or first 24bit of mac address)*

## Versions:
1) **1st Version**:
	Normal mac changer. User type new mac address and program will validate it with *Regular Expression (Regex)*.
	Everything in this program is in lowercase. So it is case-insensitive.
	This program has no problem working with uppercase letters, but output of program is always in lowercase.
2) **2nd Version**:
	Adding options to change different interfaces.
3) **3rd Version**:
	Adding option for users to change their mac address randomly. 
4) **4th Version**:
	Adding option for change mac to specific mac so that it will look like mac of other's vendor.
5) **5th Version**:
	Add some option for saving original mac address somewhere so that user can reverse mac address to normal whenever user wants. 
6) **6th Version**:
	Option for user to use this program in different versions of linux kernel.
	Commands have changed after kernel version 4.15 (After Ubuntu 18.04 released)
	So I think it is a good thing to add this option.
7) **7th Version**:
	I will implement *Fuzzy String Matching* for searching in OUIs. There are more than 17K names of organizations with different OUIs which is alot to process and show users to choose from them. I will add this feature soon...!
