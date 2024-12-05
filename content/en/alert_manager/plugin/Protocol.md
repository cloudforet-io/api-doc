---
title: "Protocol"
linkTitle: "Protocol"
weight: 3
bookFlatSection: true
---
# [Protocol](#Protocol)
A Collector is a plugin collecting data of external infrastructure resources.


>  **Package : spaceone.api.alert_manager.plugin**

<br>
<br>

## Protocol





**Protocol Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Protocol#init) | [InitRequest](Protocol#initrequest) | [PluginInfo](Protocol#plugininfo) |
| [**verify**](./Protocol#verify) | [VerifyRequest](Protocol#verifyrequest) | [Empty](Protocol#empty) |



    
<br>

### init










    
<br>

### verify










    


<br>
<br>

## Message



### InitRequest
* **options** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)   `Required` 

    <br>

### VerifyRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>
