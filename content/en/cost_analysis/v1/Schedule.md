---
title: "Schedule"
linkTitle: "Schedule"
weight: 3
bookFlatSection: true
---
# [Schedule](#Schedule)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Schedule





**Schedule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Schedule#create) | [CreateScheduleRequest](Schedule#createschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**update**](./Schedule#update) | [UpdateScheduleRequest](Schedule#updateschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**enable**](./Schedule#enable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**disable**](./Schedule#disable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**delete**](./Schedule#delete) | [ScheduleRequest](Schedule#schedulerequest) | [Empty](./Schedule#empty) |
| [**get**](./Schedule#get) | [GetScheduleRequest](Schedule#getschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**list**](./Schedule#list) | [ScheduleQuery](Schedule#schedulequery) | [SchedulesInfo](./Schedule#schedulesinfo) |
| [**stat**](./Schedule#stat) | [ScheduleStatQuery](Schedule#schedulestatquery) | [Struct](./Schedule#struct) |



    
<br>

### create





> **POST** /cost-analysis/v1/schedule/create
>






    
<br>

### update





> **POST** /cost-analysis/v1/schedule/update
>






    
<br>

### enable





> **POST** /cost-analysis/v1/schedule/enable
>






    
<br>

### disable





> **POST** /cost-analysis/v1/schedule/disable
>






    
<br>

### delete





> **POST** /cost-analysis/v1/schedule/delete
>






    
<br>

### get





> **POST** /cost-analysis/v1/schedule/get
>






    
<br>

### list





> **POST** /cost-analysis/v1/schedule/list
>






    
<br>

### stat





> **POST** /cost-analysis/v1/schedule/stat
>






    


<br>
<br>

## Message



### CreateScheduleRequest
* **schedule** (Scheduled)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **options** (Struct) 

    
* **tags** (Struct) 

    <br>

### GetScheduleRequest
* **schedule_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### ScheduleInfo
* **schedule_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **schedule** (Scheduled)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_scheduled_at** (string)  `Required` 

    <br>

### ScheduleQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **schedule_id** (string) 

    
* **name** (string) 

    
* **state** (string) 

    
* **data_source_id** (string) 

    <br>

### ScheduleRequest
* **schedule_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ScheduleStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### Scheduled
* **cron** (string)  `Required` 

    
* **interval** (int32)  `Required` 

    
* **minutes** (int32)  `Required` 

    
* **hours** (int32)  `Required` 

    <br>

### SchedulesInfo
* **results** (ScheduleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateScheduleRequest
* **schedule_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **schedule** (Scheduled) 

    
* **options** (Struct) 

    
* **tags** (Struct) 

    <br>
