# SCADA Tank Farm
This project has been develop as a final submission for a SCADA course (2020, Fall)
____

## Introduction

This text aims to provide information about Standard Operational Procedures that were considered during the development process of the SCADA project. Firstly, the author will introduce a brief explanation of the Tank Farm, after which the components and instructions of the software will be discussed. 

## Tank Farm Process Description 

The tank farm has three slaves and one master tank where the master tank's fullness is prioritized. Automatic alarm systems triggering by the predefined alarm threshold in both slave and master tanks send information to the corresponding (Pump110A for slaves, Pump770 for master) pumps and valves to start the filling process. Moreover, to provide flexibility over the process, an authorized operator can also control the process manually. Having filled master tank is waiting for the discharge of product until order is received.

![Figure 1](https://i.imgur.com/5GQsLwu.png "Title")

## Design Parameters

Several parameters have been taken into account during the designing process of the tanks, valves, and pumps. These include but are not limited to Tank capacities, High/Low alarm trigger levels, Maximum pump pressure.

|               | Tank 140 | Tank 150 |  Tank 160 | Tank 170 |
|---------------|----------|----------|-----------|----------|
| Tank Capacity | 1500     | 2500     | 3000      | 10000    |
| High Level    | 1350     | 2250     | 2700      | 9000     |
| Low level     | 200      | 200      | 200       | 1000     |

As pumps can be fragile to certain high-pressure levels (~1000 PSI), discharge selenoid valves (SV1x02) have been added to the tanks to provide maximum safety. 

## Software Overview
Concerning the safety measures, the software includes its so called Main Page to allow only authorized users to interfere with the process's control. Users can be classified as Administrators and Operators. Their privileges and pre-defined credentials are written in the table below.

|               | Can change users' credentials | Can monitor/control the process | Username   | Password  |
|---------------|-------------------------------|---------------------------------|------------|-----------|
| Administrator | Yes                           | No                              | admin_1    | 1234      |
| Operator      | No                            | Yes                             | operator_1 | Salam1234 |
