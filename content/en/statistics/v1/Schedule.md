---
title: "Schedule"
linkTitle: "Schedule"
weight: 3
bookFlatSection: true
---
# [Schedule](#Schedule)
A Schedule is a time schedule of when a User will use a query.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Schedule





**Schedule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./Schedule#add) | [AddScheduleRequest](Schedule#addschedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**update**](./Schedule#update) | [UpdateScheduleRequest](Schedule#updateschedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**enable**](./Schedule#enable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**disable**](./Schedule#disable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**delete**](./Schedule#delete) | [ScheduleRequest](Schedule#schedulerequest) | [Empty](Schedule#empty) |
| [**get**](./Schedule#get) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**list**](./Schedule#list) | [ScheduleQuery](Schedule#schedulequery) | [SchedulesInfo](Schedule#schedulesinfo) |
| [**stat**](./Schedule#stat) | [ScheduleStatQuery](Schedule#schedulestatquery) | [Struct](Schedule#struct) |



    
<br>

### add

Adds a new Schedule. When creating, `topic` and queries to be used should be specified. The time interval of the Schedule should be also specified to run queries repeatedly. The run set by Schedule starts every hour on the hour.



> **POST** /statistics/v1/schedule/add
>






    
<br>

### update

Updates a specific Schedule. You can make changes in Schedule settings, including time intervals.



> **POST** /statistics/schedule/update
>






    
<br>

### enable

Enables a specific Schedule. If a Schedule is enabled, the query usage will be scheduled by the time interval specified.



> **POST** /statistics/v1/schedule/enable
>






    
<br>

### disable

Disables a specific Schedule. If a Schedule is disabled, the query usage will not be scheduled.



> **POST** /statistics/v1/schedule/disable
>






    
<br>

### delete

Deletes a specific Schedule. You must specify the `schedule_id` of the Schedule to delete.



> **POST** /statistics/v1/schedule/delete
>






    
<br>

### get

Gets a specific Schedule. Prints detailed information about the Schedule, including the schedule interval and `state`.



> **POST** /statistics/v1/schedule/get
>






    
<br>

### list

Gets a list of all Schedules. You can use a query to get a filtered list of Schedules.



> **POST** /statistics/v1/schedule/list
>






    
<br>

### stat





> **POST** /statistics/v1/schedule/stat
>






    


<br>
<br>

## Message



### AddScheduleRequest
* **topic** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **tags** (Struct)  

    <br>

### QueryOption
* **aggregate** (StatAggregate)   `Required` 

    
* **page** (StatPage)  

    <br>

### ScheduleInfo
* **schedule_id** (string)   `Required` 

    
* **topic** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_scheduled_at** (string)   `Required` 

    <br>

### ScheduleQuery
* **query** (Query)  

    
* **schedule_id** (string)  

    
* **topic** (string)  

    
* **state** (string)  

    <br>

### ScheduleRequest
* **schedule_id** (string)   `Required` 

    <br>

### ScheduleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### Scheduled
* **cron** (string)   `Required` 

    
* **interval** (int32)   `Required` 

    
* **minutes** (int32)  `Repeated`    `Required` 

    
* **hours** (int32)  `Repeated`    `Required` 

    <br>

### SchedulesInfo
* **results** (ScheduleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateScheduleRequest
* **schedule_id** (string)   `Required` 

    
* **schedule** (Scheduled)  

    
* **tags** (Struct)  

    <br>
