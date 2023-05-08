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

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **task_options** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
