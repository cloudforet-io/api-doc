---
title: "Storage"
linkTitle: "Storage"
weight: 3
bookFlatSection: true
---
# [Storage](#Storage)



>  **Package : spaceone.api.inventory.plugin**

<br>
<br>

## Storage





**Storage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Storage#init) | [InitRequest](Storage#initrequest) | [PluginInfo](Storage#plugininfo) |
| [**verify**](./Storage#verify) | [VerifyRequest](Storage#verifyrequest) | [Empty](Storage#empty) |
| [**export**](./Storage#export) | [ExportRequest](Storage#exportrequest) | [Empty](Storage#empty) |



    
<br>

### init










    
<br>

### verify










    
<br>

### export










    


<br>
<br>

## Message



### ExportRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **schema** (string)  

    <br>

### InitRequest
* **options** (Struct)   `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)   `Required` 

    <br>

### VerifyRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **schema** (string)  

    <br>
