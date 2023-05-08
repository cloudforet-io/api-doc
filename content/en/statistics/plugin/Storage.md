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
| [**init**](./Storage#init) | [InitRequest](Storage#initrequest) | [PluginInfo](./Storage#plugininfo) |
| [**verify**](./Storage#verify) | [VerifyRequest](Storage#verifyrequest) | [Empty](./Storage#empty) |
| [**export**](./Storage#export) | [ExportRequest](Storage#exportrequest) | [Empty](./Storage#empty) |



    
<br>

### init




 {{< tabs " init " >}}




{{< /tabs >}}

    
<br>

### verify




 {{< tabs " verify " >}}




{{< /tabs >}}

    
<br>

### export




 {{< tabs " export " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ExportRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    <br>

### InitRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### VerifyRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    <br>
