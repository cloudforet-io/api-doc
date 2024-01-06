---
title: "History"
linkTitle: "History"
weight: 3
bookFlatSection: true
---
# [History](#History)
A History is a record of data collection based on a Schedule.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## History





**History Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./History#create) | [CreateHistoryRequest](History#createhistoryrequest) | [Empty](History#empty) |
| [**list**](./History#list) | [QueryHistoryRequest](History#queryhistoryrequest) | [HistoryInfo](History#historyinfo) |
| [**stat**](./History#stat) | [HistoryStatRequest](History#historystatrequest) | [Struct](History#struct) |



    
<br>

### create

Creates a new History. Gets a Schedule as an input and creates a History as an output. You can use this method to manually run a specific Schedule.



> **POST** /statistics/v1/history/create
>






    
<br>

### list

Gets a list of all Histories. You can use a query to get a filtered list of Histories.



> **POST** /statistics/v1/history/list
>






    
<br>

### stat





> **POST** /statistics/v1/history/stat
>






    


<br>
<br>

## Message



### CreateHistoryRequest
* **schedule_id** (string)   `Required` 

    <br>

### HistoryInfo
* **results** (HistoryValueInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### HistoryStatRequest
* **query** (StatisticsQuery)   `Required` 

    
* **topic** (string)  

    <br>

### HistoryValueInfo
* **topic** (string)   `Required` 

    
* **values** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### QueryHistoryRequest
* **query** (Query)  

    
* **topic** (string)  

    <br>
