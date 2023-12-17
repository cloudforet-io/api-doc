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
| [**list**](./Log#list) | [LogRequest](Log#logrequest) | [LogDataInfo](Log#logdatainfo) |



    
<br>

### list





> **POST** /monitoring/v1/log/list
>






    


<br>
<br>

## Message



### LogDataInfo
* **results** (ListValue)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### LogRequest
* **data_source_id** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    
* **keyword** (string)  

    
* **start** (string)  

    
* **end** (string)  

    
* **sort** (Struct)  

    
* **limit** (int32)  

    <br>
