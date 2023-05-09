---
title: "Data_source"
linkTitle: "Data_source"
weight: 3
bookFlatSection: true
---
# [Data_source](#Data_source)



>  **Package : spaceone.api.cost_analysis.plugin**

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









 {{< tabs " init " >}}

 {{< tab "Request Example" >}}



[InitRequest](./DataSource#initrequest)

* **options** (Struct)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **metadata** (Struct)  `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify










    


<br>
<br>

## Message



### InitRequest
* **options** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### PluginVerifyRequest
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema** (string) 

    <br>
