---
title: "Collector"
linkTitle: "Collector"
weight: 3
bookFlatSection: true
---
# [Collector](#Collector)
A Collector is a plugin collecting data of external infrastructure resources.


>  **Package : spaceone.api.inventory.plugin**

<br>
<br>

## Collector





**Collector Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Collector#init) | [InitRequest](Collector#initrequest) | [PluginInfo](Collector#plugininfo) |
| [**verify**](./Collector#verify) | [VerifyRequest](Collector#verifyrequest) | [Empty](Collector#empty) |
| [**collect**](./Collector#collect) | [CollectRequest](Collector#collectrequest) | [ResourceInfo](Collector#resourceinfo) |



    
<br>

### init

Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.







 {{< tabs " init " >}}

 {{< tab "Request Example" >}}



[InitRequest](./Collector#initrequest)

* **options** (Struct)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **metadata** (Struct)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify

Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.







 {{< tabs " verify " >}}

 {{< tab "Request Example" >}}



[VerifyRequest](./Collector#verifyrequest)

* **options** (Struct)   `Required` 


* **secret_data** (Struct)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### collect

Collects data of external infrastructure resources by a specific Collector.







 {{< tabs " collect " >}}

 {{< tab "Request Example" >}}



[CollectRequest](./Collector#collectrequest)

* **options** (Struct)   `Required` 


* **secret_data** (Struct)   `Required` 


* **filter** (Struct)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    


<br>
<br>

## Message



### CollectRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **filter** (Struct)   `Required` 

    <br>

### CollectorVerifyInfo
* **options** (Struct)   `Required` 

    <br>

### InitRequest
* **options** (Struct)   `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)   `Required` 

    <br>

### ResourceInfo
* **state** (State)   `Required` 

    
* **message** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **match_rules** (Struct)   `Required` 

    
* **resource** (Struct)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>

### VerifyRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    <br>
