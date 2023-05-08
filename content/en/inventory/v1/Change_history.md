---
title: "Change_history"
linkTitle: "Change_history"
weight: 3
bookFlatSection: true
---
# [Change_history](#Change_history)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Change_history


**ChangeHistory Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./ChangeHistory#list) | [ChangeHistoryQuery](ChangeHistory#changehistoryquery) | [ChangeHistoryInfo](./ChangeHistory#changehistoryinfo) |
| [**stat**](./ChangeHistory#stat) | [ChangeHistoryStatQuery](ChangeHistory#changehistorystatquery) | [Struct](./ChangeHistory#struct) |



    
<br>

### list

> **POST** /inventory/v1/change-history/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/change-history/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ChangeHistoryInfo
* **results** (RecordInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### ChangeHistoryQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    
* **action** (RecordAction)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **collector_id** (string)  `Required` 

  *is_required: false*

    
* **job_id** (string)  `Required` 

  *is_required: false*

    
* **updated_by** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ChangeHistoryStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    <br>

### RecordInfo
* **record_id** (string)  `Required` 

    
* **cloud_service_id** (string)  `Required` 

    
* **action** (RecordAction)  `Required` 

    
* **diff** (ListValue)  `Required` 

    
* **diff_count** (int32)  `Required` 

  *repeated RecordDiff diff = 4;*

    
* **user_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **job_id** (string)  `Required` 

    
* **updated_by** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>
