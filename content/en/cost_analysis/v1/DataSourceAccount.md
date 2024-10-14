---
title: "DataSourceAccount"
linkTitle: "DataSourceAccount"
weight: 3
bookFlatSection: true
---
# [DataSourceAccount](#DataSourceAccount)
A DataSourceAccount is a resource that for routing cost data from a specific account to a workspace, project, service account.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## DataSourceAccount





**DataSourceAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**update**](./DataSourceAccount#update) | [UpdateDataSourceAccountRequest](DataSourceAccount#updatedatasourceaccountrequest) | [DataSourceAccountInfo](DataSourceAccount#datasourceaccountinfo) |
| [**reset**](./DataSourceAccount#reset) | [ResetDataSourceAccountRequest](DataSourceAccount#resetdatasourceaccountrequest) | [Empty](DataSourceAccount#empty) |
| [**get**](./DataSourceAccount#get) | [DataSourceAccountRequest](DataSourceAccount#datasourceaccountrequest) | [DataSourceAccountInfo](DataSourceAccount#datasourceaccountinfo) |
| [**list**](./DataSourceAccount#list) | [DataSourceAccountQuery](DataSourceAccount#datasourceaccountquery) | [DataSourceAccountsInfo](DataSourceAccount#datasourceaccountsinfo) |
| [**analyze**](./DataSourceAccount#analyze) | [DataSourceAccountAnalyzeQuery](DataSourceAccount#datasourceaccountanalyzequery) | [Struct](DataSourceAccount#struct) |
| [**stat**](./DataSourceAccount#stat) | [DataSourceAccountStatQuery](DataSourceAccount#datasourceaccountstatquery) | [Struct](DataSourceAccount#struct) |



    
<br>

### update

Update a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.



> **POST** /cost-analysis/v1/data-source-account/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateDataSourceAccountRequest](./DataSourceAccount#updatedatasourceaccountrequest)

* **data_source_id** (string)   `Required` 


* **account_id** (string)   `Required` 

  *account_id is the unique identifier of each CSP account.(e.g. Azure Tenant ID)*


* **workspace_id** (string)  





{{< highlight json >}}
{
   "data_source_id": "ds-faaa11aa1111",
   "account_id": "111069360300",
   "workspace_id": "ws-aaaa11aa1111"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### reset

Reset a DataSourceAccount state and linked workspace with the specified DataSourceAccount ID related to the DataSource.



> **POST** /cost-analysis/v1/data-source-account/reset
>





 {{< tabs " reset " >}}

 {{< tab "Request Example" >}}



[ResetDataSourceAccountRequest](./DataSourceAccount#resetdatasourceaccountrequest)

* **data_source_id** (string)   `Required` 

  *data_source_id is the unique identifier of each data source.*


* **account_id** (string)  


* **reset_sync** (bool)  

  *if sync_state is true, it will reset the sync state of the data source account.*





{{< highlight json >}}
{
   "data_source_id": "ds-faaa11aa1111",
   "account_id": "111069360300",
   "sync_state": true
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Get a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.



> **POST** /cost-analysis/v1/data-source-account/get
>






    
<br>

### list





> **POST** /cost-analysis/v1/data-source-account/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[DataSourceAccountQuery](./DataSourceAccount#datasourceaccountquery)

* **query** (Query)  


* **data_source_id** (string)  


* **account_id** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **service_account_id** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### analyze





> **POST** /cost-analysis/v1/data-source-account/analyze
>






    
<br>

### stat





> **POST** /cost-analysis/v1/data-source-account/stat
>






    


<br>
<br>

## Message



### DataSourceAccountAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **account_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### DataSourceAccountInfo
* **account_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **is_sync** (bool)   `Required` 

    
* **is_linked** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **v_workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### DataSourceAccountQuery
* **query** (Query)  

    
* **data_source_id** (string)  

    
* **account_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **service_account_id** (string)  

    <br>

### DataSourceAccountRequest
* **data_source_account_id** (string)   `Required` 

    
* **account_id** (string)   `Required` 

    <br>

### DataSourceAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### DataSourceAccountsInfo
* **results** (DataSourceAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### ResetDataSourceAccountRequest
* **data_source_id** (string)   `Required` 

  *data_source_id is the unique identifier of each data source.*

    
* **account_id** (string)  

    
* **reset_sync** (bool)  

  *if sync_state is true, it will reset the sync state of the data source account.*

    <br>

### UpdateDataSourceAccountRequest
* **data_source_id** (string)   `Required` 

    
* **account_id** (string)   `Required` 

  *account_id is the unique identifier of each CSP account.(e.g. Azure Tenant ID)*

    
* **workspace_id** (string)  

    <br>
