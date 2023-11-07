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
| [**get_data**](./Cost#get_data) | [GetDataRequest](Cost#getdatarequest) | [CostsInfo](Cost#costsinfo) |



    
<br>

### get_data










    


<br>
<br>

## Message



### CostInfo
* **cost** (float)   `Required` 

    
* **usage_quantity** (float)   `Required` 

    
* **usage_unit** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **region_code** (string)   `Required` 

    
* **product** (string)   `Required` 

    
* **usage_type** (string)   `Required` 

    
* **resource** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **billed_date** (string)   `Required` 

    <br>

### CostsInfo
* **results** (CostInfo)  `Repeated`    `Required` 

    <br>

### GetDataRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **schema** (string)  

    
* **task_options** (Struct)  

    <br>
