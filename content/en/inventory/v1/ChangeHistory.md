---
title: "ChangeHistory"
linkTitle: "ChangeHistory"
weight: 3
bookFlatSection: true
---
# [ChangeHistory](#ChangeHistory)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## ChangeHistory





**ChangeHistory Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./ChangeHistory#list) | [ChangeHistoryQuery](ChangeHistory#changehistoryquery) | [ChangeHistoryInfo](ChangeHistory#changehistoryinfo) |
| [**stat**](./ChangeHistory#stat) | [ChangeHistoryStatQuery](ChangeHistory#changehistorystatquery) | [Struct](ChangeHistory#struct) |



    
<br>

### list





> **POST** /inventory/v1/change-history/list
>






    
<br>

### stat





> **POST** /inventory/v1/change-history/stat
>






    


<br>
<br>

## Message



### ChangeHistoryInfo
* **results** (RecordInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### ChangeHistoryQuery
* **cloud_service_id** (string)   `Required` 

    
* **query** (Query)  

    
* **action** (RecordAction)  

    
* **user_id** (string)  

    
* **collector_id** (string)  

    
* **job_id** (string)  

    
* **updated_by** (string)  

    <br>

### ChangeHistoryStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **cloud_service_id** (string)   `Required` 

    <br>

### RecordInfo
* **record_id** (string)   `Required` 

    
* **action** (RecordAction)   `Required` 

    
* **diff** (ListValue)   `Required` 

    
* **diff_count** (int32)   `Required` 

    
* **updated_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **cloud_service_id** (string)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **job_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>
