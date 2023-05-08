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




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/schedule/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /cost-analysis/v1/schedule/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /cost-analysis/v1/schedule/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/schedule/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/schedule/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/schedule/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/schedule/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateScheduleRequest
* **name** (string)  `Required` 

  *is_required: false*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **schedule_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

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

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
