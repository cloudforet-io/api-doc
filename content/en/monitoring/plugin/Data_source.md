---
title: "Data_source"
linkTitle: "Data_source"
weight: 3
bookFlatSection: true
---
# [Data_source](#Data_source)
desc: A DataSource is a plugin instance receiving Metric and Log data from cloud services.


>  **Package : spaceone.api.monitoring.plugin**

<br>
<br>

## Data_source





**DataSource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./DataSource#init) | [InitRequest](DataSource#initrequest) | [PluginInfo](./DataSource#plugininfo) |
| [**verify**](./DataSource#verify) | [PluginVerifyRequest](DataSource#pluginverifyrequest) | [Empty](./DataSource#empty) |



    
<br>

### init

desc: Initializes a specific DataSource. During initialization, the DataSource information to be passed to the DataSource user is delivered as `metadata`. DataSource information includes its name and version.








    
<br>

### verify

desc: Verifies a specific DataSource. You must specify the parameter `secret_data`, encrypted account data of the DataSource to validate.








    


<br>
<br>

## Message



### InitRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### PluginVerifyRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    <br>
