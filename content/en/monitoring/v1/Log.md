---
title: "Log"
linkTitle: "Log"
weight: 3
bookFlatSection: true
---
# [Log](#Log)



>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Log





**Log Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Log#list) | [LogRequest](Log#logrequest) | [LogDataInfo](./Log#logdatainfo) |



    
<br>

### list





> **POST** /monitoring/v1/log/list
>






    


<br>
<br>

## Message



### LogDataInfo
* **results** (ListValue)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### LogRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **resource_id** (string)  `Required` 

  *is_required: true*

    
* **keyword** (string)  `Required` 

  *is_required: false*

    
* **start** (string)  `Required` 

  *is_required: false*

    
* **end** (string)  `Required` 

  *is_required: false*

    
* **sort** (Struct)  `Required` 

  *is_required: false*

    
* **limit** (int32)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
