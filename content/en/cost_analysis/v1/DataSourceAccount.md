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
| [**reset**](./DataSourceAccount#reset) | [ResetDataSourceAccountRequest](DataSourceAccount#resetdatasourceaccountrequest) | [DataSourceAccountsInfo](DataSourceAccount#datasourceaccountsinfo) |
| [**get**](./DataSourceAccount#get) | [DataSourceAccountRequest](DataSourceAccount#datasourceaccountrequest) | [DataSourceAccountInfo](DataSourceAccount#datasourceaccountinfo) |
| [**list**](./DataSourceAccount#list) | [DataSourceAccountQuery](DataSourceAccount#datasourceaccountquery) | [DataSourceAccountsInfo](DataSourceAccount#datasourceaccountsinfo) |
| [**stat**](./DataSourceAccount#stat) | [DataSourceAccountStatQuery](DataSourceAccount#datasourceaccountstatquery) | [Struct](DataSourceAccount#struct) |



    
<br>

### update

Update a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.



> **POST** /cost-analysis/v1/data-source-account/update
>






    
<br>

### reset





> **POST** /cost-analysis/v1/data-source-account/reset
>






    
<br>

### get

Get a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.



> **POST** /cost-analysis/v1/data-source-account/get
>






    
<br>

### list





> **POST** /cost-analysis/v1/data-source-account/list
>






    
<br>

### stat





> **POST** /cost-analysis/v1/data-source-account/stat
>






    


<br>
<br>

## Message



### DataSourceAccountInfo
* **account_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **is_sync** (bool)   `Required` 

    
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
* **data_source_account_id** (string)   `Required` 

    <br>

### UpdateDataSourceAccountRequest
* **data_source_id** (string)   `Required` 

    
* **account_id** (string)   `Required` 

  *account_id is the unique identifier of each CSP account.(e.g. Azure Tenant ID)*

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **service_account_id** (string)  

    <br>
