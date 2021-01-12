# SCADA Tank Farm
This project has been developed as a final submission for a SCADA course using TIA Portal Software Platform (2020, Fall)
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
In individual pages, an operator can view/change the statuses of pumps and valves using the faceplates provided. Faceplates will show up when a correspondingly named button is clicked and will hide by clicking on X. 

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


## Startup Procedure

Regarding the priority of filling the master tank first, as long as there is at least one slave tank available (not having a low alarm), Pump770A will automatically start to fill the master. To fill a slave tank, it is enough to activate Pump100A. Before starting the filling process, it is essential to check the valves' performance to avoid overpressure/pump fault. They can be checked by sending commands using faceplates. 

Valve Faceplate            |  Pump Faceplate
:-------------------------:|:-------------------------:
![](https://i.imgur.com/RDfsCBL.png) |  ![](https://i.imgur.com/7Bxmou5.png)


## Normal Operations

*x = 4,..,7*

| Tag Name | Device                | Mission                                   |
|----------|-----------------------|-------------------------------------------|
| SV1x01   | Inlet Selenoid Valve  | Will open during filling of the Tank1x0   |
| SV1x02   | Outlet Selenoid Valve | Will open during discharge of the Tank1x0 |
| LT1x01   | Level Transmitter     | Measures (4-20 mA) level of the Tank1x0   |
| Pump110A | Pump                  | To fill the slave tanks                   |
| Pump770A | Pump                  | To Fill the master tank                   |
| Pump771A | Pump                  | To discharge the master tank              |


## Logic of Operation


**Valves**

|        | Open                                                                                                                       | Close                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| SV1x01 | - Tank is NOT Full and Open Valve command received<br>- Tank is Low                                                        | - Tank is NOT Low and Close Valve command received<br>- Slave (x = 4,5,6) tank fills the master (x=7) tank |
| SV1x02 | - Tank is NOT Low and Close Valve command received<br>- Slave (x = 4,5,6) tank is NOT Low AND the master (x=7) tank is Low | - Tank is Low<br>- Master tank is NOT Low AND Close Valve command recieved                                 |


**Pumps**

|          | Start                                                                                                                                                   | Stop                                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Pump100A | - Any of Slave tanks is Low<br>- Inlet valve of a slave tank is Open and Start Pump command recieved                                                    | - All slave tank inlet valves are closed<br>- A slave tank is not low and Stop Pump command received                               |
| Pump770A | - Outlet valve of a slave and inlet valve of master tank is open and Start Pump command received<br>- Any slave tank is not low and master tank is low  | - Master tank's inlet valve closed<br>- Master tank is being discharged<br>- Master tank is not Low and Stop Pump command received |
| Pump771A | - Master tank is not low and outlet valve is opened and start pump command received                                                                     | - Master Tank is low<br>- Master tank's outlet valve closed                                                                        |

## Shut Down procedures

This process includes discharge of all the tanks till there is no liquid in any of them. 

1. Pump110A is deactivated
2. Pump77A are activated to discharge master
3. Draining master will get all the liquid from slave tanks
