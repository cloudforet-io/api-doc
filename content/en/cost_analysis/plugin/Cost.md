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
| [**get_linked_accounts**](./Cost#get_linked_accounts) | [GetLinkedAccountsRequest](Cost#getlinkedaccountsrequest) | [AccountsInfo](Cost#accountsinfo) |
| [**get_data**](./Cost#get_data) | [GetDataRequest](Cost#getdatarequest) | [CostsInfo](Cost#costsinfo) |



    
<br>

### get_linked_accounts










    
<br>

### get_data










    


<br>
<br>

## Message



### AccountInfo
* **account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    <br>

### AccountsInfo
* **results** (AccountInfo)  `Repeated`    `Required` 

    <br>

### CostInfo
* **cost** (double)   `Required` 

    
* **usage_quantity** (double)   `Required` 

    
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

### GetLinkedAccountsRequest
* **options** (Struct)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>
