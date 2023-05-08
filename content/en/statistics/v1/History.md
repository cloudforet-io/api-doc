---
title: "History"
linkTitle: "History"
weight: 3
bookFlatSection: true
---
# [History](#History)
desc: A History is a record of data collection based on a Schedule.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## History


**History Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./History#create) | [CreateHistoryRequest](History#createhistoryrequest) | [Empty](./History#empty) |
| [**list**](./History#list) | [QueryHistoryRequest](History#queryhistoryrequest) | [HistoryInfo](./History#historyinfo) |
| [**stat**](./History#stat) | [HistoryStatRequest](History#historystatrequest) | [Struct](./History#struct) |



    
<br>

### create

> **POST** /statistics/v1/history/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /statistics/v1/history/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /statistics/v1/history/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateHistoryRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### HistoryInfo
* **results** (HistoryValueInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### HistoryStatRequest
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### HistoryValueInfo
* **topic** (string)  `Required` 

    
* **values** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### QueryHistoryRequest
* **query** (Query)  `Required` 

  *is_required: false*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
