---
title: "Log"
linkTitle: "Log"
weight: 3
bookFlatSection: true
---
# [Log](#Log)



>  **Package : spaceone.api.monitoring.plugin**

<br>
<br>

## Log





**Log Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Log#list) | [LogRequest](Log#logrequest) | [LogsDataInfo](Log#logsdatainfo) |



    
<br>

### list










    


<br>
<br>

## Message



### LogRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **query** (Struct)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **schema** (string)  

    
* **keyword** (string)  

    
* **sort** (Sort)  

    
* **limit** (int32)  

    <br>

### LogsDataInfo
* **results** (Struct)  `Repeated`    `Required` 

    <br>

### Sort
* **key** (string)   `Required` 

    
* **desc** (bool)   `Required` 

    <br>
