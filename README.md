# SCADA Tank Farm
This project has been develop as a final submission for a SCADA course using TIA Portal Software Platform (2020, Fall)
____

## Introduction

This text aims to provide information about Standard Operational Procedures that were considered during the development process of the SCADA project. Firstly, the author will introduce a brief explanation of the Tank Farm, after which the components and instructions of the software will be discussed. 

## Tank Farm Process Description 

The tank farm has three slaves and one master tank where the master tank's fullness is prioritized. Automatic alarm systems triggering by the predefined alarm threshold in both slave and master tanks send information to the corresponding (Pump110A for slaves, Pump770 for master) pumps and valves to start the filling process. Moreover, to provide flexibility over the process, an authorized operator can also control the process manually. Having filled master tank is waiting for the discharge of product until order is received.


## Design Parameters

Several parameters have been taken into account during the designing process of the tanks, valves, and pumps. These include but are not limited to Tank capacities, High/Low alarm trigger levels, Maximum pump pressure.

|               | Tank 140 | Tank 150 |  Tank 160 | Tank 170 |
|---------------|----------|----------|-----------|----------|
| Tank Capacity | 1500     | 2500     | 3000      | 10000    |
| High Level    | 1350     | 2250     | 2700      | 9000     |
| Low level     | 200      | 200      | 200       | 1000     |

As pumps can be fragile to certain high-pressure levels (~1000 PSI), discharge selenoid valves (SV1x02) have been added to the tanks to provide maximum safety. 

## Software Overview

### Main Page

![Figure 1](https://i.imgur.com/zJwLoWh.png)

Concerning the safety measures, the software includes its so called Main Page to allow only authorized users to interfere with the process's control. Users can be classified as Administrators and Operators. Their privileges and pre-defined credentials are different and written in the table below.

|               | Can change users' credentials | Can monitor/control the process | Username   | Password  |
|---------------|-------------------------------|---------------------------------|------------|-----------|
| Administrator | Yes                           | No                              | admin_1    | 1234      |
| Operator      | No                            | Yes                             | operator_1 | Salam1234 |

### Tank Farm Page

![Imgur](https://i.imgur.com/1PBbXEq.png)

Having logged in as an operator, a user can view the Tank Farm page, which is intended only for monitoring purposes. Moreover, individual pages for each tank has been created to add safety/friction to the control. 

### Tank 1x0 Screens
In individual pages, an operator can change the statuses of pumps and valves using the faceplates provided. Faceplates will show up when a correspondingly named button is clicked and will hide by clicking on X. 

![Figure 1](https://i.imgur.com/i5hto8f.png)

### Trend Screen
Additionally, to ease monitoring the tanks' levels simultaneously, Trend Screen has been designed, and can be viewed by clicking the button in the right top corner of Tank Screen. 

![Imgur](https://i.imgur.com/ZIn2pdF.png)

### Alarm Screen
Last, to view and acknowledge the alarms, a TIA-Portal build-in floating button has been added and can be clicked irrespective of the screen. 

![Imgur](https://i.imgur.com/a6m9svx.png)

### Status Representation

- ![#ff7777](https://via.placeholder.com/15/ff7777/000000?text=+) Not operating
- ![#55ff56](https://via.placeholder.com/15/55ff56/000000?text=+) Operating

Once an alarm happened, the Alarm Screen Pops up, giving information about the cause and results in case of no action and cannot be moved aside without canceling the panel (by clicking x). Additionally, on the Tank Farm screen, flashing lights show a specific tank having an alarm. 

- Flashing ![#fedb58](https://via.placeholder.com/15/fedb58/000000?text=+) colored light - Low Alarm
- Flashing ![#e9305a](https://via.placeholder.com/15/e9305a/000000?text=+) colored light - High Alarm

By clicking the flashing light, a pop screen giving detailed information about the alarm will show up. 

![Imgur](https://i.imgur.com/r16dyIW.png)


