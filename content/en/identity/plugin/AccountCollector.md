---
title: "AccountCollector"
linkTitle: "AccountCollector"
weight: 3
bookFlatSection: true
---
# [AccountCollector](#AccountCollector)



>  **Package : spaceone.api.identity.plugin**

<br>
<br>

## AccountCollector





**AccountCollector Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./AccountCollector#init) | [InitRequest](AccountCollector#initrequest) | [PluginInfo](AccountCollector#plugininfo) |
| [**sync**](./AccountCollector#sync) | [SyncRequest](AccountCollector#syncrequest) | [AccountsInfo](AccountCollector#accountsinfo) |



    
<br>

### init










    
<br>

### sync










    


<br>
<br>

## Message



### AccountInfo
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **location** (string)  `Repeated`    `Required` 

    <br>

### AccountsInfo
* **results** (AccountInfo)  `Repeated`    `Required` 

    <br>

### InitRequest
* **options** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)   `Required` 

    <br>

### SyncRequest
* **options** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **schema_id** (string)  

    
* **secret_data** (Struct)  

    <br>
