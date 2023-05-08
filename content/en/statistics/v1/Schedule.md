---
title: "Schedule"
linkTitle: "Schedule"
weight: 3
bookFlatSection: true
---
# [Schedule](#Schedule)
desc: A Schedule is a time schedule of when a User will use a query.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Schedule


**Schedule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./Schedule#add) | [AddScheduleRequest](Schedule#addschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**update**](./Schedule#update) | [UpdateScheduleRequest](Schedule#updateschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**enable**](./Schedule#enable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**disable**](./Schedule#disable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**delete**](./Schedule#delete) | [ScheduleRequest](Schedule#schedulerequest) | [Empty](./Schedule#empty) |
| [**get**](./Schedule#get) | [GetScheduleRequest](Schedule#getschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**list**](./Schedule#list) | [ScheduleQuery](Schedule#schedulequery) | [SchedulesInfo](./Schedule#schedulesinfo) |
| [**stat**](./Schedule#stat) | [ScheduleStatQuery](Schedule#schedulestatquery) | [Struct](./Schedule#struct) |



    
<br>

### add

> **POST** /statistics/v1/schedule/add
>




 {{< tabs " add " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /statistics/schedule/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /statistics/v1/schedule/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /statistics/v1/schedule/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /statistics/v1/schedule/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /statistics/v1/schedule/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /statistics/v1/schedule/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /statistics/v1/schedule/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### AddScheduleRequest
* **topic** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetScheduleRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### QueryOption
* **aggregate** (StatAggregate)  `Required` 

  *is_required: true*

    
* **page** (StatPage)  `Required` 

  *is_required: false*

    <br>

### ScheduleInfo
* **schedule_id** (string)  `Required` 

    
* **topic** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **schedule** (Scheduled)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_scheduled_at** (string)  `Required` 

    <br>

### ScheduleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **schedule_id** (string)  `Required` 

  *is_required: false*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ScheduleRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ScheduleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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

  *is_required: true*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
