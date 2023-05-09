---
title: "Collector"
linkTitle: "Collector"
weight: 3
bookFlatSection: true
---
# [Collector](#Collector)
desc: A Collector is a plugin collecting data of external infrastructure resources.


>  **Package : spaceone.api.inventory.plugin**

<br>
<br>

## Collector





**Collector Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Collector#init) | [InitRequest](Collector#initrequest) | [PluginInfo](./Collector#plugininfo) |
| [**verify**](./Collector#verify) | [VerifyRequest](Collector#verifyrequest) | [Empty](./Collector#empty) |
| [**collect**](./Collector#collect) | [CollectRequest](Collector#collectrequest) | [ResourceInfo](./Collector#resourceinfo) |



    
<br>

### init

desc: Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.
request_example: >-
{

}
response_example: >-
{

}








    
<br>

### verify

desc: Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.
request_example: >-
{

}
response_example: >-
{

}








    
<br>

### collect

desc: Collects data of external infrastructure resources by a specific Collector.
request_example: >-
{

}
response_example: >-
{

}








    


<br>
<br>

## Message



### CollectRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **filter** (Struct)  `Required` 

  *is_required: true*

    <br>

### CollectorVerifyInfo
* **options** (Struct)  `Required` 

    <br>

### InitRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### ResourceInfo
* **state** (State)  `Required` 

    
* **message** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **match_rules** (Struct)  `Required` 

    
* **resource** (Struct)  `Required` 

    
* **options** (Struct)  `Required` 

    <br>

### VerifyRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    <br>
