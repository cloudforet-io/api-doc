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
| [**list**](./Log#list) | [LogRequest](Log#logrequest) | [LogsDataInfo](./Log#logsdatainfo) |



    
<br>

### list










    


<br>
<br>

## Message



### LogRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **query** (Struct)  `Required` 

  *is_required: true*

    
* **keyword** (string)  `Required` 

  *is_required: false*

    
* **start** (string)  `Required` 

  *is_required: true*

    
* **end** (string)  `Required` 

  *is_required: true*

    
* **sort** (Sort)  `Required` 

  *is_required: false*

    
* **limit** (int32)  `Required` 

  *is_required: false*

    <br>

### LogsDataInfo
* **results** (Struct)  `Required` 

    <br>

### Sort
* **key** (string)  `Required` 

    
* **desc** (bool)  `Required` 

    <br>
