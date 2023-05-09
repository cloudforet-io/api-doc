---
title: "Cost"
linkTitle: "Cost"
weight: 3
bookFlatSection: true
---
# [Cost](#Cost)



>  **Package : spaceone.api.cost_analysis.plugin**

<br>
<br>

## Cost





**Cost Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_data**](./Cost#get_data) | [GetDataRequest](Cost#getdatarequest) | [CostsInfo](./Cost#costsinfo) |



    
<br>

### get_data









 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[GetDataRequest](./Cost#getdatarequest)

* **options** (Struct)  `Required` 


* **secret_data** (Struct)  `Required` 


* **domain_id** (string)  `Required` 


* **schema** (string) 


* **task_options** (Struct) 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostsInfo](#COSTSINFO)
* **results** (CostInfo)  `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### CostInfo
* **cost** (float)  `Required` 

    
* **currency** (string)  `Required` 

    
* **usage_quantity** (float)  `Required` 

    
* **provider** (string)  `Required` 

    
* **region_code** (string)  `Required` 

    
* **category** (string)  `Required` 

    
* **product** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **usage_type** (string)  `Required` 

    
* **resource_group** (string)  `Required` 

    
* **resource** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **additional_info** (Struct)  `Required` 

    
* **billed_at** (string)  `Required` 

    <br>

### CostsInfo
* **results** (CostInfo)  `Required` 

    <br>

### GetDataRequest
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema** (string) 

    
* **task_options** (Struct) 

    <br>
